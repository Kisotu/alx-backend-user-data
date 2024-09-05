#!/usr/bin/env python3
"""DB User session module.
"""
from models.base import Base


class UserSession(Base):
    """Db user session class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Initializes a User session instance in db.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
