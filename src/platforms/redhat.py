# future home for redhat updates and handling rpm

from src.core import logging
import subprocess

# this will do updates and installations
def base_install_modules(module_name):

    # if there is a , theres multiple modules
    if "," in module_name:
        module_name = module_name.split(",")
        # this will combine everything
        combined_modules = ""
        # iterate through tuple
        for modules in module_name:
            combined_modules = combined_modules + " " + modules

        subprocess.Popen("yum   install -y %s" % (combined_modules), shell=True).wait()

    else:
        # if its just one module
        if len(module_name) > 1:
            subprocess.Popen("yum  install -y " + module_name, shell=True).wait()

