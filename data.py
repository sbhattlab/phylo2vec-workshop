"""
Script to zip the data directory into a zip file using Typer CLI.
"""

import os
import zipfile
from pathlib import Path
from typing import Optional

import typer


def zip_directory(source_dir, output_filename, verbose=True):
    """
    Zip a directory and all its contents with optional verbose output.
    
    Args:
        source_dir (str or Path): Path to the directory to zip
        output_filename (str or Path): Name of the output zip file
        verbose (bool): Whether to print verbose output
    """
    source_path = Path(source_dir)
    output_path = Path(output_filename)
    
    # Check if source directory exists
    if not source_path.exists():
        raise FileNotFoundError(f"Source directory '{source_path}' does not exist")
    
    if not source_path.is_dir():
        raise NotADirectoryError(f"'{source_path}' is not a directory")
    
    if verbose:
        print(f"Creating zip archive: {output_path}")
        print(f"Source directory: {source_path}")
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all files and directories in source_dir
        for root, dirs, files in os.walk(source_path):
            for file in files:
                file_path = Path(root) / file
                # Calculate the archive name (relative path from source_dir)
                arcname = file_path.relative_to(source_path.parent)
                if verbose:
                    print(f"Adding: {arcname}")
                zipf.write(file_path, arcname)
    
    if verbose:
        print(f"Successfully created zip file: {output_path}")
        print(f"Zip file size: {output_path.stat().st_size:,} bytes")


def unzip_archive(zip_file, extract_to, verbose=True):
    """
    Unzip an archive to a specified directory.
    
    Args:
        zip_file (str or Path): Path to the zip file to extract
        extract_to (str or Path): Directory to extract files to
        verbose (bool): Whether to print verbose output
    """
    zip_path = Path(zip_file)
    extract_path = Path(extract_to)
    
    # Check if zip file exists
    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file '{zip_path}' does not exist")
    
    if not zip_path.is_file():
        raise ValueError(f"'{zip_path}' is not a file")
    
    # Create extraction directory if it doesn't exist
    extract_path.mkdir(parents=True, exist_ok=True)
    
    if verbose:
        print(f"Extracting zip archive: {zip_path}")
        print(f"Destination directory: {extract_path}")
    
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        # Get list of files in the archive
        file_list = zipf.namelist()
        
        if verbose:
            print(f"Found {len(file_list)} files in archive")
        
        # Extract all files
        for file_info in zipf.infolist():
            if verbose:
                print(f"Extracting: {file_info.filename}")
            zipf.extract(file_info, extract_path)
    
    if verbose:
        print(f"Successfully extracted {len(file_list)} files to: {extract_path}")


app = typer.Typer(help="Utility script for working with workshop data archives")


@app.command()
def zip(
    source_dir: Optional[Path] = typer.Argument(
        None,
        help="Source directory to zip. Defaults to 'data' directory in script location."
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output zip file path. Defaults to '<source_dir>.zip'."
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet",
        "-v/-q",
        help="Enable verbose output showing files being added."
    )
):
    """
    Zip a directory and all its contents.
    
    If no source directory is provided, it will zip the 'data' directory
    in the same location as this script.
    """
    script_dir = Path(__file__).parent
    
    # Set default source directory if not provided
    if source_dir is None:
        source_dir = script_dir / "data"
    
    # Set default output filename if not provided
    if output is None:
        outdir = script_dir / "dist"
        outdir.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists
        output = outdir / f"{source_dir.name}.zip"
    
    # Enable/disable verbose output in zip_directory function
    try:
        zip_directory(source_dir, output, verbose)
        typer.echo(f"✅ Successfully created: {output}", color=True)
    except (FileNotFoundError, NotADirectoryError) as e:
        typer.echo(f"❌ Error: {e}", err=True, color=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"❌ Unexpected error: {e}", err=True, color=True)
        raise typer.Exit(1)


@app.command()
def unzip(
    zip_file: Optional[Path] = typer.Argument(
        None,
        help="Zip file to extract. Defaults to 'data.zip' in script location."
    ),
    extract_to: Optional[Path] = typer.Option(
        None,
        "--extract-to",
        "-e",
        help="Directory to extract files to. Defaults to 'data' directory."
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet",
        "-v/-q",
        help="Enable verbose output showing files being extracted."
    )
):
    """
    Unzip an archive file.
    
    If no zip file is provided, it will extract 'data.zip' to the 'data' directory
    in the same location as this script.
    """
    script_dir = Path(__file__).parent
    
    # Set default zip file if not provided
    if zip_file is None:
        zip_file = script_dir / "dist" / "data.zip"
    
    # Set default extraction directory if not provided
    if extract_to is None:
        # If zip_file is data.zip, extract to data directory
        # Otherwise, extract to a directory with the same name as the zip file (without extension)
        extract_to = script_dir
    
    try:
        unzip_archive(zip_file, extract_to, verbose)
        typer.echo(f"✅ Successfully extracted to: {extract_to}", color=True)
    except (FileNotFoundError, ValueError) as e:
        typer.echo(f"❌ Error: {e}", err=True, color=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"❌ Unexpected error: {e}", err=True, color=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
