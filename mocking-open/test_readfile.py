# The code to test
from readfile import printlines

# Required to mock calls to open() and print()
from mockito import when, unstub
from io import StringIO
import builtins

def test_printlines():
    when(builtins).open('myfile.txt').thenReturn(StringIO("Hello\nWorld!\n"))
    when(builtins).print('Hello\n').thenReturn(None)
    when(builtins).print('World!\n').thenReturn(None)
    assert printlines() == None
    unstub()
