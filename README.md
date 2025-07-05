# Invoker.py

Invoker.py is a python port of Invoker tool which lets you invoke actions on different contexts/environments.

# Installation

Run the following commands to install your python dependencies
> pip install -r requirements.txt

# Running the application

> python3 run.py

# Creating custom invokes and step definitions

The invoke buttons are loaded from the yaml files located under 'invokes' folder and the python step definition are
located under 'step_definitions' pacakge. Refer to the samples and add as needed and restart your application.

# Creating installer

## Pre-requisites

If building installer for python 9, make sure libpython3.9 is installed on the system.<br>
e.g. For Ubuntu:<br>
> sudo apt install libpython3.
<br>

To clean up the build and dist directories, run the following command:
> rm -rf build dist

## Running the installer build

> ./create_installer.sh

## Running the binary

> ./dist/invoker/invoker