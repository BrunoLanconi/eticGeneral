# simple_click #

A sample project.

### What is this repository for? ###

* Groups all necessary files to perform simple_click actions
* Groups all necessary files to perform...
* Groups all necessary files to perform...

### What do I need? ###

* Python 3.10+;
* PIP package installer.

### How do I get set up? ###

* Install the `.tar` package.
```shell
pip3 install simple_click-0.1.0.tar
```

### Commands ###

* Prints context variable and argument.
```shell
simple_click first command-argument ARGUMENT
```
* Prints option value and welcome message.
```shell
simple_click first command-option -ok OPTION_VALUE
```

### Usage sample ###

* Prints context variable and argument with verbosity.
```shell
simple_click -v first command-argument ARGUMENT
```

### How does it work? ###

1) The script will...
2) Then the script will...

### Logging ###

All logs are created on `~/.simple_click/logs`.

### Documenting and testing ###

You may access the QuickGuide for more detailed explanations.

* To create a new environment based on pyproject.toml:
```shell
make install
```
* To run make install and activate environment:
```shell
make activate
```
* To run texts with pytest:
```shell
make test
```
* To create technical documentation with pdoc:
```shell
make docs
```
* To create a release:
```shell
make build
```

### Who do I talk to? ###

* Bruno Lançoni Neto <bruno.lanconi.neto@devoteam.com>
