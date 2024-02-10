import pytest
from hash import MyHash


def test_basic():
    phonebook = MyHash(max_size=15)
    phonebook.add("loki", "1999")
    assert phonebook.get("loki") == "1999"
    with pytest.raises(ValueError):
        phonebook.add("loki", "1999")
    with pytest.raises(ValueError):
        phonebook.add("loki", "1231")
    phonebook.add("olegan", "2000")
    phonebook.add("petr", "1000")
    assert phonebook.get("loki") == "1999"
    assert phonebook.get("petr") == "1000"
    assert phonebook.get("semen", '1477') == "1477"
    assert phonebook.get("oleg", '1477') == "1477"
