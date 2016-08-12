from django.db import models

# Create your models here.
class Question(object):
    """docstring for Question."""

    def __init__(self, question, answers):
        self.question_text = question
        self.answers = answers




class Answer(object):
    """docstring for Answer."""

    def __init__(self, text, img_url, correct=False):
        self.text = text
        self.img_url = img_url
        self.is_correct = correct
        self.selected=False
