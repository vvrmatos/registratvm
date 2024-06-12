# Registratvm

Registratvm is a simple time-tracking Python tool designed to help users commit their task progress effectively.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Compilation](#compilation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Registratvm aims to provide a straightforward solution for individuals or teams to track their time spent on various tasks. It offers a minimalist interface and essential functionalities to record task durations and progress updates.

## Installation

To install Registratvm, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/vvrmatos/registratvm
    ```

2. Navigate to the project directory:

    ```bash
    cd Registratvm
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

After installation, you can execute registratvm using either of the following methods:

- Execute the main script using Python:

    ```bash
    python main.py
    ```

- If `main.py` is executable (has appropriate permissions), you can run it directly:

    ```bash
    chmod a+x main.py
    ./main.py
    ```

Follow the prompts to start tracking your tasks.

## Compilation

To compile registratvm into an executable, you can use py2app. Here's how:

1. Navigate to the project directory:

    ```bash
    cd registratvm
    ```

2. Run py2app:

    ```bash
    python setup.py py2app
    ```

This will generate a standalone application in the `dist` directory.

## Contributing

Contributions to registratvm are welcome! If you have any ideas, bug fixes, or feature enhancements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/vvrmatos/registratvm).

## License

This project is licensed under the terms of the [MIT License](LICENSE).
