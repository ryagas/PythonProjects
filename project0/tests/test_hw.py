import hello_world


def test_hw(capsys):
    hello_world.main([])
    out, err = capsys.readouterr()
    assert "Hello, World!" in out


def test_hw_arg(capsys):
    hello_world.main([__name__, "--who", "John"])
    out, err = capsys.readouterr()
    assert "Hello, John!" in out


def test_hw_arg2(capsys):
    hello_world.main([__name__])
    out, err = capsys.readouterr()
    assert "World" in out
