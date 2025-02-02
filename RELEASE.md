# installSynApps Releases

<!--RELEASE START-->

## R2-0 (???-June-2019)

* Rework of installSynApps with code readability and cross-platform support in mind.
* Legacy scripts still included, with slight edits  to support new configure format
* New installSynApps python module - allows for importing into other code.
* Modular solution - Easy port to CLI and GUI versions
    * DataModel/ViewModel
* New GUI version, with ability to edit almost all config options.
* Tested an working on windows systems as well as linux - bash dependencies removed.

## R1-0 (30-May-2019)

* Initial release of installSynApps
* Based around a series of scripts
* Reliant on bash - only ran on Linux-based systems
* Included scripts
    * auto_build.sh - guided process through running remaining scripts
    * installSynApps.sh - top level script that ran the remaining ones sequentially
    * dependencyInstall.sh - Script for installing dependency packages
    * read_install_config.py - Script for reading provided configure folder
    * clone_and_checkout.py - script for cloning and checking out all modules
    * ad_config_setup.py - port of adConfigSetup module - allowed for auto-config of areaDetector files
    * update_release_file.py - top level script for updating configuration options
    * buildEPICS.py - script for calling build commands
    * script_generator.py - autogenerates some helpful information about build
* Limitations:
    * Required constant edits of configure/INSTALL_CONFIG file.
    * No support for multiple configure directories
    * Code readability issues - arrays used to represent installation modules
    * Limited customizability
    * Issues when running scripts individually
