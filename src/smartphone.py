class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def send_message(self, message):
        print(f"Sending message: '{message}' from {self.brand} {self.model}")