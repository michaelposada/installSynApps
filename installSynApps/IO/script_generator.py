#
# Class responsible for generating bash build scripts once the top level scripts are run
#
# Author: Jakub Wlodek
#


import os
import shutil
import datetime
import installSynApps.DataModel.install_config as IC


class ScriptGenerator:
    """
    Class responsible for auto-generating install, uninstall, and README files for a given install config

    Attributes
    ----------
    install_config : InstallConfiguration
        currently loaded install configuration
    message : str
        Simple autogenerated message at the top of scripts

    Methods
    -------
    initialize_dir()
        Creates autogenerated directory
    generate_install()
        generates install bash script
    generate_uninstall()
        generates an uninstall bash script
    generate_readme()
        generates readme based on install config
    autogenerate_all()
        calls all other generation methods
    """


    def __init__(self, install_config):
        """ Constructor for ScriptGenerator """

        self.install_config = install_config
        self.message = "# This script was autogenerated by installSynApps on {}\n# The script is available at https://github.com/epicsNSLS2-deploy/installSynApps\n\n".format(datetime.datetime.now())


    def initialize_dir(self):
        """ Function that creates an autogenerated directory """

        if os.path.exists("autogenerated/"):
            shutil.rmtree("autogenerated/")
        
        os.mkdir("autogenerated")


    def generate_install(self):
        """ Function that generates an install file based on currently loaded install_config """

        install_fp = open("autogenerated/install.sh", "w+")
        install_fp.write("#!/bin/bash\n")
        
        install_fp.write(self.message)

        for module in self.install_config.get_module_list():
            if module.build == "YES":
                install_fp.write("{}={}\n".format(module.name, module.abs_path))

        for module in self.install_config.get_module_list():
            if module.build == "YES":
                install_fp.write("cd ${}\n".format(module.name))
                install_fp.write("make -sj\n")


    def generate_uninstall(self):
        """ Function that generates an uninstall file based on currently loaded install_config """

        uninstall_fp = open("autogeneratd/uninstall.sh", "w+")
        uninstall_fp.write("#!/bin/bash\n")

        uninstall_fp.write(self.message)

        modules = self.install_config.get_module_list()
        modules = modules.reverse()

        for module in modules:
            if module.build == "YES":
                uninstall_fp.write("{}={}\n".format(module.name, module.abs_path))

        for module in modules:
            if module.build == "YES":
                uninstall_fp.write("cd ${}\n".format(module.name))
                uninstall_fp.write("make clean uninstall\n")
                uninstall_fp.write("make clean uninstall\n")


    def generate_readme(self):
        """
        Function that takes the currently loaded install configuration, 
        and writes a readme file describing modules and versions
        """

        if os.path.exists(self.install_config.install_location + "/INSTALL_README.txt"):
            os.remove(self.install_config.install_location + "/INSTALL_README.txt")
        readme_fp = open(self.install_config.install_location + "/INSTALL_README.txt", "w+")
        readme_fp.write("Autogenerated installSynApps README file created on {}\n".format(datetime.datetime.now()))
        readme_fp.write("https://github.com/epicsNSLS2-deploy/installSynApps\n")
        readme_fp.write("-------------------------------------------------------\n")
        readme_fp.write("The following modules were installed with the following version numbers:\n\n")
        for module in self.install_config.get_module_list():
            if module.build == "YES":
                readme_fp.write("{} -> {}\n".format(module.name, module.version))
        
        readme_fp.write("-------------------------------------------------------\n")
        readme_fp.write("The following modules were cloned with the given versions but not auto-built\n\n")
        
        for module in self.install_config.get_module_list():
            if module.build == "NO" and module.clone == "YES":
                readme_fp.write("{} -> {}\n".format(module.name, module.version))


    def autogenerate_all(self):
        """ Top level function that calls all autogeneration functions """

        self.initialize_dir()
        self.generate_install()
        self.generate_uninstall
        self.generate_readme()