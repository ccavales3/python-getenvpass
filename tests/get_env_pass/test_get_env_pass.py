"""
This file unittests the get_env_pass/__init__.py with pytest.

Methods:
    test_call_get_env_pass_with_var
    test_call_get_env_pass_with_var_doesnt_exist
    test_call_get_env_pass_no_args
    test_call_get_env_pass_more_args
"""
import os
import unittest
from unittest.mock import patch

import pytest

from get_env_pass import get_env_pass


class TestInitSbt(unittest.TestCase):
    """
    Creating a basic test class in order to test get_env_pass/__init__.py script
    """

    def test_call_get_env_pass_with_var(self):
        """
        Should return environment value
        """
        os.environ['TEST_VAR'] = 'TestVar'
        sys_var = get_env_pass('TEST_VAR')

        self.assertEqual(sys_var, 'TestVar')

        del os.environ['TEST_VAR']

    @patch('get_env_pass.getpass', return_value='does_not_exist')
    def test_call_get_env_pass_with_var_doesnt_exist(self, sys_var):
        """
        Should return getpass value if environment variable does not exist
        """
        sys_var = get_env_pass('TEST_VAR')

        self.assertEqual(sys_var, 'does_not_exist')

    @patch('get_env_pass.getpass', return_value='no_args')
    def test_call_get_env_pass_no_args(self, sys_var):
        """
        Should return getpass value if no argument(s) is passed in get_env_pass
        """
        sys_var = get_env_pass()

        self.assertEqual(sys_var, 'no_args')

    def test_call_get_env_pass_more_args(self):
        """
        Should return appropriate error when more than required arguments are passed in
        """
        with pytest.raises(TypeError) as type_error:
            # pylint: disable=too-many-function-args, unused-variable
            sys_var = get_env_pass('arg1', 'arg2')

        self.assertEqual('get_env_pass() takes from 0 to 1 positional arguments but 2 were given',
                         str(type_error.value))
