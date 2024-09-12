#!/usr/bin/env python3
"""A module for authentication functions
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password and returns bytes
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
