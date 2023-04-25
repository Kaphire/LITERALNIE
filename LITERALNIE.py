##      Game rules:    1. Generate random polish 5 letter word and keep it hidden
##                     2. Give a user 6 chances to guess the word
##                     3. Everytime a user takes a guess tell him if any letter in a current guess is included in the destination word if so,
##                        tell if it is in a correct position or wrong position

print('Game rules: blablabla')

##      ***DICTIONARY OF 5 LETTER WORDS***

# Wygenerowanie losowej liczby porządkowej słowa z pliku excel
class backend:
    def __init__(self):    
        import random
        l_porzadkowa = random.randint(1,5)

        # Podczyt słowa 5 literowego z excela

        from openpyxl import load_workbook
        wb = load_workbook('SLOWA 5 LITEROWE.xlsx')
        sheet = wb.active
        szukane_słowo = sheet.cell(row = l_porzadkowa, column = 2).value

        print(szukane_słowo, len(szukane_słowo), 'Generating sucessful')

        #stworzenie listy z szukanym słowem
        global lista_szukane
        lista_szukane = []
        for x in szukane_słowo:
            lista_szukane.append(x)
        print(lista_szukane)

    ##      ***GAME LOGIC***

    def Logika_gry():
        # zabezpieczenie przed wpisaniem złego słowa
        while True: 
            global guess_1
            guess_1 = input('Type your guess: ')
            if len(guess_1) == 5:
                print("Word lenght correct")
                break    
            print("Wrong word lenght, input 5 letter word.")

        #stworzenie listy ze zgadywanym słowem 1
        global lista_guess_1
        lista_guess_1=[]
        for x in guess_1:
            x = x.upper()
            lista_guess_1.append(x)
        print(lista_guess_1)

        #porównywanie liter w obydwu słowach
        szukane_słowo_podpowiedź = ['_','_','_','_','_']

        i=0
        while i<=4:
            for x in lista_guess_1:
                if x == lista_szukane[i]:
                    szukane_słowo_podpowiedź[i] = x
            i=i+1

        print('Poszukiwane słowo jest postaci: ', szukane_słowo_podpowiedź)

##      *** VISUAL INTERFACE ***
class frontend(backend):
    def __init__(self):
        from PyQt6 import QtWidgets
        from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
        import sys

        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(200, 200, 500, 500)
        win.setWindowTitle('LITERALNIE')

        label = QtWidgets.QLabel(win)
        label.setText('Guess the 5 letter word in the least number of tries')
        label.move(100,50)

        self.input = QLineEdit(win) #user input guess_1
        self.input.move(100,100)
        win.show()
        sys.exit(app.exec())


window = frontend()
logika = backend()
backend.Logika_gry()


