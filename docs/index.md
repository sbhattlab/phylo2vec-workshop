# Phylo2Vec Workshop

## Abstract

Phylogenetic trees are diagrams that illustrate species' shared evolutionary history. Represented as bifurcating binary trees, these trees also represent similar relationships such as tracing the similarities between languages.

Given the importance of this data structure, a plethora of corresponding software currently exists. However, the current standard for representing a phylogenetic tree is a string via the Newick format. Conversely, phylo2vec represents phylogenetic trees as integer vectors. This representation requires substantially less storage, and thus enables more efficient tree operations.

Our latest contributions have completely rewritten the core component of phylo2vec in Rust, boosting both performance and memory efficiency—while still maintaining the Python and R APIs. We’ve also implemented several optimizations to reduce time complexity.

Whether you’re a phylogenetics enthusiast or simply curious about developing scientific packages, using Rust, using GitHub Actions, or performing proper benchmarking, join our workshop and experience it firsthand! The session will last 1 hour 30 minutes, and all participants will receive a £10 lunch voucher afterward. Please bring a laptop so you can follow along and try things out yourself!

The workshop is co-organised by the University of Copenhagen, the eScience institute, and the Statistics Section of the Department of Mathematics at Imperial College London.

## Learning Goals

* Learning the basics of the phylo2vec representation
* Getting familiar with commonly used development tools for Python software: pixi, pytest, pytest-benchmark

## Workshop Logistical Information

* Date: 19 September 2025
* Time: 11:00 AM - 12:30 PM
* Location: Huxley 410, Imperial College London, London, UK

## Preliminary Agenda

**Note:** Subject to change

| Time      | Topic/Activity       |
|-----------|-----------------------------|
| 11:00-11:15 | Welcome and Introductions |
| 11:15-11:30 | Overview of Phylo2Vec and its Applications |
| 11:30-12:00 | Tutorial |
| 11:00-12:30 | Exercise |

## List of Exercises

[UPDATE THIS SECTION WITH ACTUAL EXERCISE NAMES AND DESCRIPTIONS]

## Running the Exercises

The quickest way to get started without manual installation is to use
[GitHub Codespaces](https://github.com/features/codespaces) - "a development environment that's hosted in the cloud". This allows you to run the workshop exercises directly in your browser without needing to set up a local environment.
In order to access the Codespace, you need to register an account with [GitHub](https://github.com).

:::{important}
When clicking the button below, if you have any current codespace,
we recommend deleting it to ensure you have the latest
changes from the workshop repository.

Additionally, once codespace is rendered,
please wait until the `README.md` file is loaded
to ensure that setup is complete.
:::

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sbhattlab/phylo2vec-workshop?quickstart=1)

☝️ Click the button above to go to options window to launch a GitHub Codespace.
