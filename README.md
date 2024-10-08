# pybo

Flask-based web application for Python beginners


## Installation

1. Install Miniforge
    ```bash
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

2. Clone the repository
    ```bash
    rm -rf pybo*
    git clone git@github.com:chrisjihee/pybo.git
    cd pybo*
    ```

3. Create a new environment
    ```bash
    mamba create -n pybo python=3.11 -y
    mamba activate pybo
    ```

4. Install the required packages
    ```bash
    pip install -U -r requirements.txt
    pip list
    ```


## Execution

1. Show help
    ```bash
    python -m flask --help
    ```

2. Run command
  * Initialize Database
    ```bash
    flask --app pybo db init
    flask --app pybo db migrate
    flask --app pybo db upgrade
    ```

  * Run the application
    ```bash
    flask --app pybo run
    ```


## Reference

* https://github.com/pahkey/jump2flask
