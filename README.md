# Overengineered-server

## Introduction

The goal of this repository is to trial and showcase solid DevOps practices for a very simple server

## Elements

### CI Pipeline

The CI pipeline, required on each commit and also on pull request for branches dev and main, run the following stages:
- Checkouts out branch
- Sets up a Python environment and installs dependecies
- Runs a linter (flake8)
- Runs unit tests (pytest)

### Main Branch Protections

The main branch is protected through a rule. It requires the CI Pipeline to pass. 
