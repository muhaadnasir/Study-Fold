import uuid

class Card:
    def __init__(self, question, answer, course, topic):
        self.id = str(uuid.uuid4())
        self.question = question
        self.answer = answer
        self.course = course
        self.topic = topic
        self.rating = None

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "course": self.course,
            "topic": self.topic,
            "rating": self.rating
        }
    
    @classmethod
    def from_dict(cls, d):
        card = cls(d["question"], d["answer"], d["course"], d["topic"])
        card.id = d["id"]
        card.rating = d["rating"]
        return card