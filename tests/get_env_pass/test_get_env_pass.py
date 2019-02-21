"""
This file unittests the get_env_pass/__init__.py with pytest.

Methods:
    test_call_get_env_pass_with_var
    test_call_get_env_pass_without_var
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
        Calling get_env_pass with a system variable
        """
        os.environ['TEST_VAR'] = 'TestVar'
        sys_var = get_env_pass('TEST_VAR')

        self.assertEqual(sys_var, 'TestVar')

        del os.environ['TEST_VAR']

    @patch('get_env_pass.getpass', return_value='does_not_exist')
    def test_call_get_env_pass_with_var_doesnt_exist(self, sys_var):
        """
        test
        """
        sys_var = get_env_pass('TEST_VAR')

        self.assertEqual(sys_var, 'does_not_exist')


    def test_call_get_env_pass_without_var(self):
        """
        test
        """
        with pytest.raises(TypeError) as type_error:
            sys_var = get_env_pass()  # pylint: disable=no-value-for-parameter, unused-variable

        self.assertEqual('get_env_pass() missing 1 required positional argument: \'env_var\'',
                         str(type_error.value))
