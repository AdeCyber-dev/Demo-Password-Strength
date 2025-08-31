from app.utils import check_password_strength

def test_short_password():
    assert check_password_strength("abc") == "Weak"

def test_alpha_only():
    assert check_password_strength("abcdef") == "Weak"

def test_medium_password():
    assert check_password_strength("abc123") == "Medium"

def test_strong_password():
    assert check_password_strength("Abc123!") == "Strong"
