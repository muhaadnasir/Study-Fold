from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    
    def get_by_course(self, course):
        return [card for card in self.cards if card.course == course]

    def get_by_topic(self, course, topic):
        return [card for card in self.cards if card.course == course and card.topic == topic]

    def all_courses(self):
        return sorted(set(card.course for card in self.cards))

    def all_topics(self, course):
        return sorted(set(card.topic for card in self.cards if card.course == course))

    def update_rating(self, card_id, rating):
        for card in self.cards:
            if card.id == card_id:
                card.rating = rating
                break