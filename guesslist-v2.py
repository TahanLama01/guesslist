from random import choice, randrange
from time import sleep
from os import system

class GuessList:

    number          = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    correct_amount  = 0
    wrong_amount    = 0

    list_number     = [[1,2,3],[4,5,6],[7,8,9]]

    def __init__(self, questions=1) -> None:
        self.questions = questions
        
        dict_menu = {1: self.start, 2: exit}
        self.dict_menu = dict_menu

    def start(self):
        self.default_config()
        self.this_questions()
        self.end()
        self.again()

    def default_config(self):
        self.correct_amount = 0
        self.wrong_amount   = 0

    def this_questions(self):
        for i in range(self.questions):
            system("cls")

            choice_line = randrange(0, 3)
            choice_column = randrange(0, 3)

            print("=" * 30)
            print(f"Question to {i + 1}\n")
            print(f"Line  : {choice_line + 1}")
            print(f"Column: {choice_column + 1}")
            print("=" * 30)

            self.checking(choice_line, choice_column)
            self.loading(i)

    def checking(self, choice_line, choice_column):
            while True:
                try:
                    your_guess = int(input("\nYour Answer:\n > "))
                    
                except(ValueError):
                    print(" >! Enter numbers from 1 - 9, not letters")
                    continue
                else:
                    if self.list_number[0][0] <= your_guess < self.list_number[2][2]:
                        if your_guess == self.list_number[choice_line][choice_column]:
                            print("\n >^ Your guess is Correct")
                            self.correct_amount += 1
                        else:
                            print("\n >> Your guess is Wrong")
                            print(f" >^ The correct answer is = {self.list_number[choice_line][choice_column]}")
                            self.wrong_amount += 1
                    else:
                        print(" >! Enter numbers from 1-9")
                        continue
                    break
        
    def loading(self, i):
        if i + 1 == self.questions:
            print("\n ># Loading game results... (3 sec)")
        else:
            print("\n ># Next question loading... (3 sec)")
        sleep(3)
    
    def end(self):
        print(f"""

    Number of Questions : {self.questions}
    Correct amount      : {self.correct_amount}
    Wrong amount        : {self.wrong_amount} 
    
    """)

    def menu(self):
        self.intro()
        while True:
            try:
                choice = int(input("\nMenu: \n > "))
                self.dict_menu[choice]()
                break
            except(KeyError):
                print(f" >! Please choice 1 - {len(self.dict_menu)}")
                continue
        self.menu()

    def again(self):
        while True:
            again = input("Want to play again? [yes/no]\n > ").lower()
            if again == "yes" or again == "no":
                break

        if again == "yes":
            self.start()

    def intro(self):
        system("cls")
        print("""Guess List""")
        for i in self.list_number:
            print(i)
        print("\n 1) Start Game\n 2) Exit")

if __name__ == '__main__':
    play = GuessList()
    play.menu()