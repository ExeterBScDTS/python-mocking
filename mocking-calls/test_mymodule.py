from mockito import when, unstub

def test_myfunction():

    import myimport

    when(myimport).anotherfunction(1).thenReturn('A')
    when(myimport).anotherfunction(2).thenReturn('B')

    import mymodule

    assert mymodule.myfunction(1,2) == ['A','B']

    unstub()