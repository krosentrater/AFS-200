import itertools

class TriviaQuestion:
    id_iter = itertools.count()
    def __init__(self, question, category, diff, cAn, iAns):
        self.question = question
        self.category = category
        self.diff = diff
        self.cAn = cAn
        self.iAns = iAns
        self.id = next(self.id_iter)
        self.ans = []

    def __str__(self):
        return f"{self.question} {self.category} {self.diff} {self.cAn} {self.iAns}"

    def getCategory(self):
        return self.category
    
    def getIncorrectAnswers(self):
        return self.iAns

    def getCorrectAnswer(self):
        return self.cAn

    def getShuffledAnswers(self):
        self.ans = [self.cAn, * self.iAns]
        return self.ans
    
    def getId(self):
        return self.id