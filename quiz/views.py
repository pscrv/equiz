from django.shortcuts import render

# Test area
from .models import Question, Answer

answer1 = Answer("Answer 1", "http://www.tierliebe.co/wp-content/uploads/2015/11/coon3.jpg", True)
answer2 = Answer("Answer 2", "https://www.royalcanin.com/~/media/Royal-Canin/Subpage-Hero-Images/150327_Hero_kit.ashx")
answer3 = Answer("Answer 3", "http://i.dailymail.co.uk/i/pix/2016/03/10/16/321177F500000578-3485975-image-a-63_1457625965529.jpg")
answer4 = Answer("Answer 4", "http://www.hscalumet.org/App_downloads/feral%20cat.png")

question1 = Question(
    "Which of these cats is a Maine Coon?",
    [answer1, answer2, answer3, answer4])

answer1 = Answer("Answer 1", "http://www.tierliebe.co/wp-content/uploads/2015/11/coon3.jpg")
answer2 = Answer("Answer 2", "https://www.royalcanin.com/~/media/Royal-Canin/Subpage-Hero-Images/150327_Hero_kit.ashx")
answer3 = Answer("Answer 3", "http://i.dailymail.co.uk/i/pix/2016/03/10/16/321177F500000578-3485975-image-a-63_1457625965529.jpg", True)
answer4 = Answer("Answer 4", "http://www.hscalumet.org/App_downloads/feral%20cat.png")
question2 = Question(
    "Which of these cats is a Siamese?",
    [answer1, answer2, answer3, answer4])


questions =  [question1, question2]

# End test


# Create your views here.
def start_page(request):
    return render(request, 'quiz/start_page.html', {})

def question_page(request, pk, clicked=None):
    key = int(pk)
    question = questions[key]

    if clicked:
        question.answers[int(clicked)].selected = True

    next = key + 1
    if next == len(questions):
        next = 0
    return render (
        request,
        'quiz/question_page.html',
        {   "question": questions[key].question_text,
            "showing": key,
            "question_number": key+1,
            "answers": questions[key].answers,
            "next": next})
