import random

class Die:
    def __init__(self):
        pass

    def roll(self, num):
        dice = []
        for i in range(num):
            dice.append(random.randint(1, 6)) # To test yahtzee code replace this with 1 number
        return dice

    def rollAllDice(self):
        roll = self.roll(5)
        rollSet = set(roll)
        for i in roll:
            print(f"({i})", end = ' ')
        if len(rollSet) == 1:
            return print("\nYAHTZEE!!!")
        return False


dice = Die()
dice.rollAllDice()


# ⚀
# ⚁
# ⚂
# ⚃
# ⚄
# ⚄