#!/bin/bash

# File that builds EPICS base and synApps from scratch with one call

# First we clone all of the modules
echo "Cloning and checking out all repos"
python3 clone_and_checkout.py

# first build the dependencies
echo "Install the dependencies"
./installDependencies.sh

# Python script for compiling EPICS and SynApps
echo "Starting compilation"
python3 buildEPICS.py

# Python script that autogenerates install and uninstall scripts for all selected packages
echo "Creating install.sh and uninstall.sh in directory autogenerated/"
python3 autogenerate_scripts.py