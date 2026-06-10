from greet import greet


def test_greet_returns_hello():
    assert greet("world") == "Hello, world!"


def test_greet_uses_given_name():
    assert greet("Claude") == "Hello, Claude!"
