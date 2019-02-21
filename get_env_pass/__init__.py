"""
get_env_pass module
"""
from getpass import getpass
import os

def get_env_pass(env_var):
    """
    get_env_pass function
    """
    return os.environ[env_var] if env_var in os.environ else getpass()
