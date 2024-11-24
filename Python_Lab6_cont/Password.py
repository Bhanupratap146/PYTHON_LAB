class PasswordManager:
    def _init_(self):
      self.__password = None
    def set_password(self, password):
      self.__password = password
    def get_password(self):
      return self.__password
password_manager = PasswordManager()
password_manager.set_password("mySecretPassword123")
print("Password is:", password_manager.get_password())
