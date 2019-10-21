class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True

class Lannister(GotCharacter):
    """Because it's nicer when you're the king"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Je suis le roi"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False