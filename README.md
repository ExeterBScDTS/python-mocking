# python-mocking
Python mockito examples


## mocking-requests

## mocking-builtins

Where a builtin function takes time to run it should be mocked, the most likely candidate is
opening a file and the subsequent reads and writes.

Other candidates for mocking are print() and input() in order to automate the testing.

The ```readfile.py``` example also shows how mockito verify() is used to check that a mocked
function is called.  This is important in TDD where tests are written before
the implementation and can ensure the implementation actually does what is required. 
