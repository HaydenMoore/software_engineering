from evaluate import *

def setup_module(module):
    print("\nsetup_module\n")
    """ setup any state specific to the execution of the given module."""

def teardown_module(module):
    print("\nteardown_module\n")
    """ teardown any state that was previously setup with a setup_module
    method.
    """

def test_parse_integer():
    print("\ntest_parse_integer\n")
    for i in range(0,1000):
        s = str(i)
        assert parse_integer(s) == i
    assert parse_integer(8347128311) == 8347128311

def test_parse_integer2():
    print("\ntest_parse_integer2\n")
    for i in range(0,1000):
        s = str(i)
        assert parse_integer(s) == i
