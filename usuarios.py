class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

# Usuarios de ejemplo
users = {
    "usuario1": User(username="usuario1", password="contraseña1"),
    "usuario2": User(username="usuario2", password="contraseña2")
}

