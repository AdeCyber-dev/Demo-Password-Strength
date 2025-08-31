def check_password_strength(password: str) -> str:
    """Simple password strength checker."""
    if len(password) < 6:
        return "Weak"
    if password.isalpha():
        return "Weak"
    if any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(not c.isalnum() for c in password):
        return "Strong"
    return "Medium"
