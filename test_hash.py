import pytest
from hash import MyHash


def test_basic():
    phonebook = MyHash()
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


def test_set():
    phonebook = MyHash()
    phonebook.add("loki", "1999")
    assert phonebook.get("loki") == "1999"
    phonebook.seti("loki", "999")
    phonebook.add("petr", "100")
    assert phonebook.get("petr") == "100"
    phonebook.seti("petr", "666")
    assert phonebook.get("petr") == "666"
    assert phonebook.get("loki") == "999"


def test_pop():
    phonebook = MyHash()
    phonebook.add("loki", "1")
    assert phonebook.pop("loki") == "1"

    with pytest.raises(ValueError):
        phonebook.get("loki")

    phonebook.add("oleg", "2")
    phonebook.add("thor", "3")

    assert phonebook.get("oleg") == "2"
    assert phonebook.get("thor") == "3"
    assert phonebook.pop("oleg") == "2"
    assert phonebook.pop("thor") == "3"
    with pytest.raises(ValueError):
        phonebook.get("thor")
        phonebook.get("oleg")
    phonebook.add("loki", "666")
    assert phonebook.get("loki") == "666"


def test_keys():
    phonebook = MyHash()
    d = ["zero", "loki", "oleg", "joe", "max", "leha", "sveta", "pumba"]
    for c in d:
        phonebook.add(c, c)
    assert set(phonebook.keys()) == set(d)


def test_values():
    phonebook = MyHash(max_size=2)
    d = ["zero", "loki", "oleg", "joe", "max", "leha", "sveta", "pumba"]
    for c in d:
        phonebook.add(c, c)
    assert set(phonebook.values()) == set(d)

    phonebook = MyHash(max_size=6)
    d = ["zero", "loki", "oleg", "joe", "max", "leha", "sveta", "pumba"]
    for c in d:
        phonebook.add(c, c)
    assert set(phonebook.values()) == set(d)
