
# Phylo2Vec Workshop Release Notes

**Release Date:** 2025-09-17

**Workshop Website**: [phylo2vec-workshop.readthedocs.io](https://phylo2vec-workshop.readthedocs.io)

## Overview

This release contains materials and resources for the Phylo2Vec Workshop, a hands-on session on encoding, manipulating, and analyzing binary phylogenetic trees using Phylo2Vec.

Phylogenetic trees are commonly represented as Newick strings; Phylo2Vec instead represents trees as compact integer vectors. This greatly reduces storage needs and enables faster tree operations. The core has been rewritten in Rust for major performance and memory gains while preserving the Python and R APIs.

## What's Included

### Workshop Materials

- Tutorial notebook: `docs/tutorial.ipynb` (introduction and guided walkthrough)
- Exercise notebook: `docs/exercise.ipynb` (hands-on problems and solutions)
- Workshop site content: `docs/` (MyST Markdown / Jupyter Book v2)
- Environment files: `pixi.toml`, `pixi.lock` for reproducible setup

### Learning Objectives

Participants will:

- Learn the basics of the Phylo2Vec representation
- Get familiar with common Python dev tools used in the project: pixi, pytest, pytest-benchmark

## System Requirements

### Software Dependencies

- Operating System: Linux, macOS
- Software: [Pixi](https://pixi.sh) (v0.50.0 or later)

### Hardware Recommendations

- Memory: Minimum 8 GB RAM
- Disk Space: Minimum 2 GB free space

## Installation Instructions

### Quick Start

The easiest way to get started is to use [GitHub Codespaces](https://github.com/features/codespaces), which provides a cloud-hosted development environment. You can run the workshop exercises directly in your browser without local setup. Register for a GitHub account if you don't have one.

[Launch GitHub Codespaces](https://codespaces.new/sbhattlab/phylo2vec-workshop?quickstart=1)

☝️ Click the link above to launch a GitHub Codespace for this workshop.

Tips:

- If you have an existing codespace for this repo, delete it first to ensure you get the latest changes.
- After the codespace opens, wait for the `README.md` to load to ensure setup completes.

## List of Exercises

All materials are located in the `docs` directory. Start with the tutorial, then complete the exercises:

- Tutorial: `docs/tutorial.ipynb` — overview of Phylo2Vec and basic operations
- Exercise 1: build an adjacency matrix from a phylo2vec vector
- Exercise 2: visualise a tree from a phylo2vec vector or matrix

## Data and Examples

### Current Datasets

The `data/` directory is currently a placeholder and does not include real datasets (see `data/README.md`). Examples are embedded within the notebooks.

## Additional Resources

### Documentation

- [Phylo2Vec Documentation](https://phylo2vec.readthedocs.io)

### Support and Community

- **Bug Reports:** If you encounter issues, please open an issue on the [Phylo2Vec Workshop Repository](https://github.com/sbhattlab/phylo2vec-workshop/issues/new/choose).

## Acknowledgments

Co-organised by the University of Copenhagen, the eScience Institute, and the Statistics Section of the Department of Mathematics at Imperial College London. We also thank the UW eScience Scientific Software Engineering Center for infrastructure and contributions.

## License

This workshop content is released under the BSD 3-Clause License. You are free to use, modify, and distribute the materials as long as you adhere to the license terms. See the `LICENSE` file for details.
