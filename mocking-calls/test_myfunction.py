from mockito import when, unstub

def test_myfunction():

    import mymodule

    when(mymodule).anotherfunction(1).thenReturn('A')
    when(mymodule).anotherfunction(2).thenReturn('B')

    import myfunction

    assert myfunction.myfunction(1,2) == ['A','B']

    unstub()