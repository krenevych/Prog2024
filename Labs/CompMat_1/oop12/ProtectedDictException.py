# raise ValueError("Ключ має бути цілого типу")
# raise ValueError("Такий ключ вже є у словнику")

class ProtectedDictError(Exception):
    pass

class ProtectedDictIntError(ProtectedDictError):
    def __init__(self,  key,
                 value,
                 message = "Ключ має бути цілого типу",
              ):
        super().__init__()
        self.message = message
        self.key = key
        self.value = value


    def __str__(self):
        return f"{self.message=}, {self.key}={self.value}"

class ProtectedDictKeyAlreadyExists(ProtectedDictError):
    def __init__(self,
                 key,
                 value,
                 message="Такий ключ вже є у словнику"):
        super().__init__()
        self.message = message
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.message=}, {self.key}={self.value}"

