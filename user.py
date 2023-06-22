class User():
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password


    def __str__(self) -> str:
        return f'User ID: {self.id}'