import json
from deck import Deck
from card import Card

class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self, deck):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)

                for d in data:
                    deck.add_card(Card.from_dict(d))
        except FileNotFoundError:
            pass

    def save(self, deck):
        with open(self.filepath, "w") as file:
            json.dump([card.to_dict() for card in deck.cards], file, indent=2)