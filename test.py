import json
import pytest
from main import load_passwords, save_passwords

@pytest.fixture
def passwords_fixture(tmp_path):
    passwords = [{"service": "Service1", "username": "User1", "password": "Password1"}]
    file_path = tmp_path / "test_passwords.json"
    with open(file_path, "w") as file:
        json.dump(passwords, file)
    return file_path
    print(file_path)

def test_load_passwords(passwords_fixture):
    passwords = load_passwords(passwords_fixture)
    assert passwords == [{"service": "Service1", "username": "User1", "password": "Password1"}]

def test_save_passwords(passwords_fixture):
    passwords = [{"service": "Service2", "username": "User2", "password": "Password2"}]
    save_passwords(passwords, passwords_fixture)
    with open(passwords_fixture, "r") as file:
        saved_passwords = json.load(file)
    assert saved_passwords == passwords
