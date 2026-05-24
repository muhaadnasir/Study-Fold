import json
from deck import Deck
from card import Card

class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self, deck):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                content = file.read().strip()

                if not content:
                    return

                data = json.loads(content)

                for d in data:
                    deck.add_card(Card.from_dict(d))

        except FileNotFoundError:
            pass

    def save(self, deck):
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(
                [card.to_dict() for card in deck.cards],
                file,
                indent=2
            )

