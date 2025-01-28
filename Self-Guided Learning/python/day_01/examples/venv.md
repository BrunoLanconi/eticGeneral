## [Using venv](https://docs.python.org/3/library/venv.html)

To create a virtual environment using `venv` module:

1. Open a terminal or command prompt.
2. Navigate to the folder where you want to create the virtual environment.
3. Run the following command to create a virtual environment:

```bash
python3 -m venv myenv
```

Replace `myenv` with the desired name for your virtual environment.

4. Activate the virtual environment by running:

- For Windows:

```bash
myenv\Scripts\activate
```

- For macOS and Linux:

```bash
source myenv/bin/activate
```

You are now inside the virtual environment. Install any required packages using `pip` and run your Python scripts within this environment.

To deactivate the virtual environment, simply run:

```bash
deactivate
```

## [Using Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

`Poetry` is a dependency management and packaging tool for Python. To use `Poetry` in your project, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the folder where you want to create the virtual environment.
3. Run the following command to initialize a new `Poetry` project:

```bash
poetry init
```

This will guide you through creating a `pyproject.toml` file, where you can specify your project's dependencies and other settings.

4. To add a new dependency to your project, use the following command:

```bash
poetry add package_name
```

Replace `package_name` with the name of the package you want to add.

5. `Poetry` will automatically manage your project's virtual environment. To activate the virtual environment, simply run:

```bash
poetry shell
```

You are now inside the virtual environment and can run your Python scripts or use the installed packages.

To deactivate the virtual environment:

```bash
exit
```

# Troubleshooting

The virtual environment may not be created successfully because `ensurepip` may not be available. 
On Debian/Ubuntu systems, you need to install the `python3-venv` package using the following command.

```bash
apt install python3.10-venv
```

You may need to use sudo with that command. After installing the `python3-venv` package, recreate your virtual environment.