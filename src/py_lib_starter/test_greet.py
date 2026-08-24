from py_lib_starter import greet


def test_greet_returns_greeting_for_provided_name() -> None:
    assert greet("Carl") == "Hello Carl"
