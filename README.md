# GDSC UvA Bot

A social media bot for the Google Developer Student Club of the University of Amsterdam (GDSC UvA).

## Requirements

We use python version `3.10.x` currently, since some dependencies do not have `wheels` available for versions `>3.10.x`.

You will propably use a virtual environment to seperate dependencies in your system. To create a virtual environment for python version `3.10.x` run the following commands.

```bash
# Make sure you have python-3.10 installed.
$ python --list
 -V:3.10 # Or something similar

# Installs 'virtualenv'.
$ py -V:3.10 -m pip install virtualenv
...

# Creates a virtual environment in the current directory called 'venv'.
$ py -V:3.10 -m virtualenv venv
...

# Activate the virtual environment.
# NOTICE: This will only activate the virtual environment for the current terminal window.
$ ./venv/Scripts/activate
(venv) $ ...

# Inside the virtual environment, install the requirements from 'requirements.txt'.
$ pip install -r ./requirements.txt
...
```

## Styling

For styling python, we use [black](https://github.com/psf/black), just run the following command when you have it installed:

```bash
$ python -m black
...
```

This will automatically reformat files that are not properly styled.

## Discord

The discord bot is primarly used for many things:

TODO: Add list of things discord bot can do.

The bot requires `administrator` permissions on server.

## Running

Make sure you have all environment variables set:

### Linux

```bash
$ export GDSC_DISCORD_TOKEN=<token>
...
```

### Windows (powershell)

```powershell
PS > $env:GDSC_DISCORD_TOKEN=<token>
```
