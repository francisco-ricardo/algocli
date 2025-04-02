# Algocli Repository

This repository contains a collection of coding challenges and algorithmic 
solutions. It includes a **Command-Line Interface (CLI)** application 
to run algorithms directly, making it easy to test and explore solutions.

---

## 🚀 Overview

This repository serves as a collection of algorithmic challenges and their 
solutions. It includes Python implementations for common coding problems, 
organized to provide clarity and scalability. Each problem solution includes a 
description, complexity analysis, and Python code, which is neatly documented 
for easy understanding.

The **CLI application** (`algocli`) is the centerpiece of this repository, 
allowing users to execute algorithms and run unit tests directly from the 
command line.

---

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

- **`src/bin/algocli`**: A CLI tool to test algorithms directly from the 
  command line.
- **`src/python/algorithms`**: Contains Python implementations of algorithmic 
  solutions.
- **`src/test`**: Unit tests for validating the correctness of the solutions.
- **`Dockerfile`**: Defines the container for executing the code.
- **`Makefile`**: Simplifies project setup and execution with predefined 
  commands.
- **`compose.yaml`**: Configures the Docker environment for consistent 
  execution.

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
   git clone https://github.com/francisco-ricardo/algocli.git
   cd algocli
   ```

2. **Build and run the container using Docker Compose**:
   ```bash
   make up
   ```

---

## 💻 Using the CLI App (`algocli`)

The **CLI application** (`algocli`) is the easiest way to interact with the 
algorithms in this repository. It allows you to run algorithms and unit tests 
directly from the command line.

### Running an Algorithm

To run an algorithm, use the following command:

```bash
docker exec -it algocli python src/bin/algocli <algorithm_name> <arguments>
```

Replace `<algorithm_name>` with the name of the algorithm and `<arguments>` 
with the required inputs.

### Examples:

1. **Run `non_constructible_change`**:
   ```bash
   docker exec -it algocli python src/bin/algocli non_constructible_change "1,2,5"
   ```
   Output:
   ```
   Minimum non-constructible change: 4
   ```

2. **Run `two_numbers_sum`**:
   ```bash
   docker exec -it algocli python src/bin/algocli two_numbers_sum "3,5,-4,8,11,1,-1,6" 10
   ```
   Output:
   ```
   Indices of the two numbers that sum to the target: [0, 4]
   ```

3. **Run `is_valid_subsequence`**:
   ```bash
   docker exec -it algocli python src/bin/algocli is_valid_subsequence "1,2,3,4" "2,4"
   ```
   Output:
   ```
   Is valid subsequence: True
   ```

---

## 🧪 Running Unit Tests

Unit tests are included to validate the correctness of the implemented 
algorithms. You can run all unit tests using the following command:

```bash
docker exec -it algocli python src/bin/algocli test
```

This command will execute all the test cases defined in the `src/test` 
directory and display the results.

---

## 📈 Algorithms Included

This repository includes the following algorithms, all of which can be 
executed using the CLI app:

1. **is_valid_subsequence**: Checks if a sequence is a valid subsequence of 
   another sequence.
   - Example:
     ```bash
     docker exec -it algocli python src/bin/algocli is_valid_subsequence "1,2,3,4" "2,4"
     ```

2. **non_constructible_change**: Finds the minimum non-constructible change 
   that cannot be created with given coins.
   - Example:
     ```bash
     docker exec -it algocli python src/bin/algocli non_constructible_change "1,2,5"
     ```

3. **sorted_squared_array**: Returns a sorted array of the squares of the 
   input array.
   - Example:
     ```bash
     docker exec -it algocli python src/bin/algocli sorted_squared_array "-4,-1,0,3,10"
     ```

4. **two_numbers_sum**: Finds two numbers in the list that sum to the target 
   value.
   - Example:
     ```bash
     docker exec -it algocli python src/bin/algocli two_numbers_sum "3,5,-4,8,11,1,-1,6" 10
     ```

5. **tournament_winner**: Determines the winner of a tournament based on 
   competition results.
   - Example:
     ```bash
     docker exec -it algocli python src/bin/algocli tournament_winner -i "HTML,CSS,0" -i "CSS,Python,1" -i "Python,HTML,1"
     ```

---

## 🌟 Why This Repository?

This repository demonstrates:

- **Problem-Solving Skills**: Solutions to real-world algorithmic challenges.
- **Clean Code Practices**: Adherence to Python standards and best practices.
- **Scalability**: Modular structure for easy extension and maintenance.
- **Testing**: Comprehensive unit tests to ensure correctness and reliability.
- **DevOps Integration**: Dockerized environment for consistent execution.
- **Ease of Use**: A CLI app for quick and intuitive interaction with 
  algorithms.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new 
algorithms to add, feel free to open an issue or submit a pull request.

---

## 📜 License

This repository is licensed under the MIT License. You are free to clone, 
modify, and contribute to this project. See the [LICENSE](LICENSE) file for 
more details.

---

### 🚧 Under Construction

This repository is actively being developed, and new algorithms will be added 
regularly. Stay tuned for updates, and feel free to suggest algorithms or 
improvements by opening an issue or submitting a pull request.

---

## 📬 Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [francisco-ricardo](https://github.com/francisco-ricardo)
- **Email**: franciscoricardo.dev@gmail.com
- **LinkedIn**: [francisco-aguiar](www.linkedin.com/in/francisco-aguiar-3ab650a0)

