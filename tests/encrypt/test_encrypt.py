from pytest import raises

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with raises(TypeError):
        encrypt_message("test", "3")

    assert encrypt_message("test", 7) == "tset"

    assert encrypt_message("test", 3) == "set_t"

    assert encrypt_message("test", 2) == "ts_et"
