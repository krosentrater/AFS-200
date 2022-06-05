from flask import Flask, json, render_template
from flask import request
import requests
import triviaquestion
import triviagame

app = Flask(__name__)

def getData():
    URL = 'https://opentdb.com/api.php?amount=5&category=18&type=multiple'
    try:
        response = requests.get(URL, timeout = 5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

triviaInfo = getData()
myTriviaG = triviagame.TriviaGame()


for question in triviaInfo["results"]:
    newQuestion = triviaquestion.TriviaQuestion(
        question["question"],
        question["category"],
        question["difficulty"],
        question["correct_answer"],
        question["incorrect_answers"]
    )
    newQuestion.getShuffledAnswers()
    newQuestion.getCorrectAnswer()
    newQuestion.getIncorrectAnswers()
    myTriviaG.addTriviaQuestion(newQuestion)

@app.route('/')
def hello():
    category = 'Science: Computers'
    # return json.dumps([question.__dict__ for question in myTriviaG.getAllQuestions()])
    return render_template('index.html', questions = myTriviaG.getAllQuestions(), category = category)

@app.route('/score', methods = ['GET', 'POST'])
def score():
    if request.method == 'POST':
        inputAnswer = request.form.get(newQuestion.id)
        print(inputAnswer)
        return render_template('score.html', input_ans = inputAnswer, questions = myTriviaG.getAllQuestions())
    else:
        return "You have failed!"
    

if __name__ == "__main__":
    app.run()


## {{ question.getShuffledAnswers() }} 'module' object is not callable

## How do I get the shuffled answers and add an individual radio button to each one? 
## Am I getting the values of the radio buttons correctly? 
## How to fix the html codes in questions?

## Form in index.html, second route method post, loop through questions and compare questions CANS to input
## Seperate incorrect/correct answers, local arrays (2), save whole question


## Need access to questions, need access to answers from input, question answers. Compare what correct answer to input answer, if correct
## Need to display questions, need access to answers from input, question's answers. 





## export FLASK_ENV=development
