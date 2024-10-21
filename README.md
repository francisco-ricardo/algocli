# Algorithms Repository

This repository contains a collection of coding challenges and algorithmic solutions, structured and optimized for ease of use and scalability. It is designed to be flexible, with Docker integration for consistent development and execution environments.

## Overview

This repository serves as a collection of algorithmic challenges and their solutions. It includes a set of Python implementations for common coding problems, organized to provide clarity and scalability. Each problem solution includes a description, complexity analysis, and Python code, which is neatly documented for easy understanding.

## Project Structure

```bash

├── Dockerfile
├── README.md
├── Makefile
├── bin
│   └── non_constructible_change
├── compose.yaml
├── scripts
│   ├── docker-cmd-script.sh
│   └── docker-entrypoint.sh
├── src
│   └── python
│       ├── is_valid_subsequence
│       │   ├── __init__.py
│       │   └── solution.py
│       ├── non_constructible_change
│       │   ├── __init__.py
│       │   └── solution.py
│       ├── sorted_squared_array
│       │   ├── __init__.py
│       │   └── solution.py
│       ├── tournament_winner
│       │   ├── __init__.py
│       │   └── solution.py
│       └── two_numbers_sum
│           ├── __init__.py
│           └── solution.py

```

- Dockerfile: Defines the container for executing the code.

- Makefile: Provides commands for building and running the project.

- compose.yaml: Configures the Docker container and environment.

- src/python: Contains the algorithmic solutions in Python. Each directory in src/python corresponds to a specific coding challenge. Each problem is self-contained, with its solution located inside its own folder.

- bin: Contains the program to test the algorithm from the command line. The name of the program correponds to the specific coding challege.

## Getting Started

To get started with this repository, follow these steps:

### Prerequisites

- Docker
- Python 3.x

### Setup instructions

- Clone the repository:

```bash
git clone https://github.com/francisco-ricardo/algorithms.git
cd algorithms
```

- Build and run the container using Docker Compose:

```bash
make run
```

### Usage

Once the Docker container is up, you can execute any of the solutions directly by running the respective Python scripts inside the container.

Example:

```bash
docker exec -it algorithms python bin/non_constructible_change

```

This will run the `non_constructible_change` algorithm solution.

## Technologies Used

- Python: Core language used for solving algorithmic challenges.

- Docker: To provide an isolated, consistent execution environment.

- Makefile: To simplify commands and workflow automation.

- Shell scripts: For container entrypoint and command execution.

## License

This repository is licensed under the MIT License, allowing you to freely clone, modify, and submit improvements. Feel free to contribute or customize it as needed! See the LICENSE file for more details.
