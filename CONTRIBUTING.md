# Contributing to Phylo2vec Workshop

To contribute to the Phylo2vec Workshop, you must have [Pixi](https://pixi.sh) installed.

## Setting Up Your Environment

1. **Clone the Repository**: Start by cloning the Phylo2vec Workshop repository to your local machine.

   ```bash
   git clone https://github.com/sbhattlab/phylo2vec-workshop.git
   ```

2. **Install Pixi Environment**: Ensure you have the Pixi environment set up. You can do this by running the following command in your terminal:

   ```bash
   pixi install --all
   ```

At this point, you should have all the necessary dependencies installed for the Phylo2vec Workshop.

## Contributing to the content

All of the content for the Phylo2vec Workshop is stored in the `docs` directory.
You can edit the content using your preferred text editor or IDE.
The technology we use to render the content is [Jupyter Book v2](https://next.jupyterbook.org) and you can add content in the form of [Myst Markdown](https://next.jupyterbook.org/tutorial/mystmd)
or [Jupyter Notebooks](https://mystmd.org/guide/quickstart-jupyter-lab-myst).

You can preview your changes locally by running the following command in the root of the repository:

```bash
pixi run -e site start
```

This will start a local jupyterbook server, and you can view the workshop at the url given in the terminal output, typically `http://localhost:3000`.
*This server will automatically reload when you make changes to the content*.

After you are satisfied with your changes, you can commit them,
and then create a pull request to the `main` branch of the repository.
This will allow [ReadtheDocs](https://readthedocs.org) to generate a preview of your changes.

## Release Process

The release process for the Phylo2vec Workshop is a manual process that involves the following steps.

### 1. Updating the codebase

**NOTE: The release versioning follows the format `YYYY.M.D`, where `YYYY` is the year, `M` is the month, and `D` is the day of the release.**

0. **Create a Release Branch**: Create a new branch for the release, typically named `release/YYYY.M.D`.

1. **Update the Version**: Update the version in `pixi.toml` to reflect the new release version.

2. **Update the Release Notes**: Update the `RELEASE.md` file with the new release date and any relevant changes or updates to the workshop content.

3. **Commit Your Changes**: Commit your changes to the repository with a meaningful commit message, such as "Release version YYYY.M.D".

4. **Make a pull request**: Push your changes to the remote repository and create a pull request to merge your changes into the `main` branch.

### 2. Updating the data and create a release

1. **Setup Github Token**: Ensure you have a GitHub token set up in your environment for release.
If you don't have a token yet, you can follow the [instruction provided by Github](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
Once you have your token, you need to set it in your environment:

   ```bash
   export GH_TOKEN=your_github_token
   ```

   Replace `your_github_token` with your actual GitHub token.

2. **Zip and Release the Data**: Run the following command to zip and release the data directory:

   ```bash
   pixi run -e data release
   ```

   This will create a `data.zip` file in a `./dist` directory. After that, the script will upload the `data.zip` file to the GitHub release.

### Optional: Updating the data once released

You have the option to update the data after it has been released.
To do this, you can run the following command:

```bash
pixi run -e data update-release-data
```

This command will update the data in the existing release without creating a new release by zipping the `data` directory with the latest data and uploading it to the existing GitHub release.

## Delete a Release (Optional)

If you need to delete a release for any reason, you can do so by running the following command:

```bash
pixi run -e data delete-release
```
