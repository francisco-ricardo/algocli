# Algorithms Repository

This repository contains a collection of coding challenges and algorithmic solutions, structured and optimized for ease of use and scalability. It is designed to be flexible, with Docker integration for consistent development and execution environments.

## 🚀 Overview

This repository serves as a collection of algorithmic challenges and their solutions. It includes a set of Python implementations for common coding problems, organized to provide clarity and scalability. Each problem solution includes a description, complexity analysis, and Python code, which is neatly documented for easy understanding.

## 📂 Project Structure

```bash
.
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── compose.yaml
├── scripts
│   ├── docker-cmd-script.sh
│   └── docker-entrypoint.sh
└── src
    ├── bin
    │   └── algocli
    └── python
        ├── algorithms
        │   ├── __init__.py
        │   ├── is_valid_subsequence.py
        │   ├── non_constructible_change.py
        │   ├── sorted_squared_array.py
        │   ├── tournament_winner.py
        │   ├── two_numbers_sum.py
        │   └── two_numbers_sum_2.py
        └── test
            ├── __init__.py
            └── cases.py

```

### Key Components:

- **`Dockerfile`**: Defines the container for executing the code.
- **`Makefile`**: Simplifies project setup and execution with predefined commands.
- **`compose.yaml`**: Configures the Docker environment for consistent execution.
- **`src/python/algorithms`**: Contains Python implementations of algorithmic solutions.
- **`src/bin/algocli`**: A CLI tool to test algorithms directly from the command line.
- **`src/test`**: Unit tests for validating the correctness of the solutions.

---

## 🛠️ Technologies Used

- **Python**: Core language for solving algorithmic challenges.
- **Docker**: Ensures a consistent and isolated execution environment.
- **Makefile**: Automates workflows and simplifies project commands.
- **Shell Scripts**: Handles container entrypoints and command execution.

---

## 🏁 Getting Started

Follow these steps to set up and explore the repository:

### Prerequisites

- Docker
- Python 3.x

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/francisco-ricardo/algorithms.git
   cd algorithms
   ```

2. **Build and run the container using Docker Compose**:
   ```bash
   make up
   ```
---

## 💻 Usage

Once the Docker container is running, you can execute any of the solutions directly using the CLI tool or Python scripts.

### Example: Running the CLI Tool

```bash
docker exec -it algorithms python src/bin/algocli non_constructible_change "1,2,5"
```

This will execute the `non_constructible_change` algorithm and display the result.

---

## 🧪 Running Unit Tests

Unit tests are included to validate the correctness of the implemented algorithms. 
You can run all unit tests using the following command:

```bash
docker exec -it algorithms python src/bin/algocli test
```

This command will execute all the test cases defined in the `src/test` directory and display the results.

---

# 📈 Algorithms Included

This repository is a work in progress, and new algorithms will be added over time. 
Below is the current list of implemented algorithms:

1. **is_valid_subsequence**: Checks if a sequence is a valid subsequence of another sequence.
   - Example:
     ```bash
     python src/bin/algocli is_valid_subsequence "1,2,3,4" "2,4"
     ```

2. **non_constructible_change**: Finds the minimum non-constructible change that cannot be created with given coins.
   - Example:
     ```bash
     python src/bin/algocli non_constructible_change "1,2,5"
     ```

3. **sorted_squared_array**: Returns a sorted array of the squares of the input array.
   - Example:
     ```bash
     python src/bin/algocli sorted_squared_array "-4,-1,0,3,10"
     ```

4. **two_numbers_sum**: Finds two numbers in the list that sum to the target value.
   - Example:
     ```bash
     python src/bin/algocli two_numbers_sum "3,5,-4,8,11,1,-1,6" 10
     ```

5. **tournament_winner**: Determines the winner of a tournament based on competition results.
   - Example:
     ```bash
     python src/bin/algocli tournament_winner -i "HTML,CSS,0" -i "CSS,Python,1" -i "Python,HTML,1"
     ```

---

## 🌟 Why This Repository?

This repository demonstrates:

- **Problem-Solving Skills**: Solutions to real-world algorithmic challenges.
- **Clean Code Practices**: Adherence to Python standards and best practices.
- **Scalability**: Modular structure for easy extension and maintenance.
- **Testing**: Comprehensive unit tests to ensure correctness and reliability.
- **DevOps Integration**: Dockerized environment for consistent execution.

---

## 📜 License

This repository is licensed under the MIT License. You are free to clone, modify, and contribute to this project. See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new algorithms to add, feel free to open an issue or submit a pull request.

---

### 🚧 Under Construction

This repository is actively being developed, and new algorithms will be added regularly. Stay tuned for updates, and feel free to suggest algorithms or improvements by opening an issue or submitting a pull request.

