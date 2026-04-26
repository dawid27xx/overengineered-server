# Overengineered-server

## Introduction

The goal of this repository is to trial and showcase solid DevOps practices for a very simple Python server.

The server itself is intentionally small. The main focus of the project is the surrounding workflow: CI, branch protection, deployment to AWS EC2, and running the app as a Linux service.

## Elements

### CI Pipeline

The CI pipeline runs on pushes and pull requests targeting the `main` and `dev` branches.

It runs the following stages:

- Checks out the repository
- Sets up a Python 3.11 environment
- Installs project dependencies
- Runs linting with `flake8`
- Runs type checking with `mypy`
- Runs unit tests with `pytest`

This helps catch code quality issues, type errors, and failing tests before changes are merged.

### Main Branch Protection

The `main` branch is protected using a GitHub ruleset.

The rule requires the CI pipeline to pass before changes can be merged into `main`. This prevents broken code from being merged if linting, type checking, or tests fail.

### CD Pipeline

The CD pipeline runs only after a successful push to `main`.

It depends on the CI job, meaning deployment only happens if all CI checks pass.

The CD stage:

- Connects to the EC2 instance using SSH
- Pulls the latest code from the `main` branch
- Activates the Python virtual environment
- Updates dependencies from `requirements.txt`
- Restarts the running server service using `systemd`
- Checks the service status after restart

Secrets such as the EC2 host, username, and private SSH key are stored in GitHub Actions secrets.

### AWS EC2 Deployment

The app is hosted on an AWS EC2 instance using Amazon Linux 2023.

The instance was configured with:

- A security group for SSH access
- A security group rule for accessing the server port
- A Python virtual environment
- The project repository cloned onto the instance
- Dependencies installed from `requirements.txt`

### Gunicorn

The Flask app is served using Gunicorn rather than the Flask development server.

Gunicorn runs the Flask app using:

```bash
gunicorn -w 2 -b 0.0.0.0:5000 server:app
