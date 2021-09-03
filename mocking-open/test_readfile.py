# The code to test
from readfile import printlines

# Required to mock calls to open() and print()
from mockito import when, unstub
from io import StringIO
import builtins

def test_printlines():
    ## Mock open and print with the exact arguments we expect.
    when(builtins).open('myfile.txt').thenReturn(StringIO("Hello,\nworld!\n"))
    when(builtins).print('Hello,\n').thenReturn(None)
    when(builtins).print('world!\n').thenReturn(None)
    ## Call the function under test.
    assert printlines() == None
    unstub()
