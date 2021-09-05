# python-mocking

Python mocking examples

There are several reasons why we mock functions when testing our code, but at the heart of this
is one fundamental reason - we want our tests to pass when our code is correct, and fail when
it is not. We don't want tests that might sometimes fail for other reasons, such as a slow
internet connection.

## mocking-calls

Many of the functions we write will call other functions.  Perhaps these other functions haven't
even be written yet. Whether they are available or not, when we test a function we ideally
should test only that function and not other parts of our program.

## mocking-requests

The requests library enables calls to web APIs.  We want to know that our function makes the
correct call, and also that it handles HTTP errors correctly.  Using mocks makes our tests
much faster and consistent, and allows easy testing of error handling.

## mocking-builtins

Where a builtin function takes time to run it should be mocked, the most likely candidate is
opening a file and the subsequent reads and writes.

Other candidates for mocking are print() and input() in order to automate the testing.

The ```readfile.py``` example also shows how mockito verify() is used to check that a mocked
function is called.  This is important in TDD where tests are written before
the implementation and can ensure the implementation actually does what is required.
