class Missing(Exception):
    """누락된 데이터"""

    def __init__(self, message: str):
        self.message = message


class Duplicate(Exception):
    """중복된 데이터"""

    def __init__(self, message: str):
        self.message = message
