# Lab 07: Virtual Environments

A Python virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. It is a way of creating isolated environments for Python projects. There are several tools available for creating virtual environments in Python, such as `venv`, `Pipenv`, `Conda`, and `Poetry`.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice
- (For venv) Python 3.3 or later installed on your system
- (For pipenv) [Pipenv installed on your system](https://pipenv.pypa.io/en/latest/installation.html#installing-pipenv)
- (For conda) [Conda installed on your system](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- (For poetry) [Poetry installed on your system](https://python-poetry.org/docs/#installation)


## Instructions

### For [venv](https://docs.python.org/3/library/venv.html)

1. Create a new directory for this lab and navigate to it.
2. Create a virtual environment by running the following command:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

4. Install a package in the virtual environment:

```bash
pip install requests
```

5. Deactivate the virtual environment:

```bash
deactivate
```

---

### For [Pipenv](https://pipenv.pypa.io/)

1. Create a new directory for this lab and navigate to it.
2. Create a virtual environment by running the following command:

```bash
pipenv install
```

3. Activate the virtual environment:

```bash
pipenv shell
```

4. Install a package in the virtual environment:

```bash
pipenv install requests
```

5. Deactivate the virtual environment:

```bash
exit
```

---

### For [Conda](https://conda.io/)

1. Create a new directory for this lab and navigate to it.
2. Create a virtual environment by running the following command:

```bash
conda create --name myenv
```

3. Activate the virtual environment:

```bash
conda activate myenv
```

4. Install a package in the virtual environment:

```bash
conda install requests
```

5. Deactivate the virtual environment:

```bash
conda deactivate
```

---

### For [Poetry](https://python-poetry.org/)

**Attention**: We already used Poetry in the previous labs and the course will always rely on it. So, guarantee that you are able to use it from now on.

1. Create a new directory for this lab and navigate to it.
2. Create a virtual environment by running the following command:

```bash
poetry init
```

3. Install a package in the virtual environment:

```bash
poetry add requests
```

4. Activate the virtual environment:

```bash
poetry shell
```

5. Deactivate the virtual environment:

```bash
exit
```
