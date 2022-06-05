class TriviaGame:
    def __init__(self):
        self.questions = []

    def addTriviaQuestion(self, triviaQuestion):
        self.questions.append(triviaQuestion)
    
    def getAllQuestions(self):
        return self.questions