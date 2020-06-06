from hello import say_hello

e = say_hello()
def test_sayhello_no_params():
    assert e == "Hello, World"



def test_sayhello_with_param():
    assert say_hello("Everybody") == "hello, Everybody!"
