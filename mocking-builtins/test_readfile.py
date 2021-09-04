# The code to test
from readfile import printlines

# Required to mock calls to open() and print()
from mockito import when, unstub, verify
from io import StringIO
import builtins

def test_printlines():
    ## Mock open and print with the exact arguments we expect.
    when(builtins).open('myfile.txt').thenReturn(StringIO("Hello,\nworld!\n"))
    when(builtins).print('Hello,\n').thenReturn(None)
    when(builtins).print('world!\n').thenReturn(None)

    ## Call the function under test.
    assert printlines() == None

    # Call worked, but were the mocked calls actually called?
    # Let's check.
    verify(builtins,times=1).open('myfile.txt')
    verify(builtins,times=1).print('Hello,\n')
    # times=1 is the default, so this works too.
    verify(builtins).print('world!\n')
    unstub()
