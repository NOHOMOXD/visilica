import random
import wordsAll
from colors import colors
from lives import lives

separateLine = colors.OKBLUE + "_____________________________________________\n"
existedCharacters = colors.OKBLUE + "Введенные буквы:"
insertCharacter = colors.OKCYAN + 'Введите букву: '
answerYN = colors.OKGREEN + 'Ответ: '
answerFull = colors.HEADER + \
    "Отгадываемое слово: ['б', 'а', 'б', '_', '_', '_']"

# Получим слово
randomObj = random.SystemRandom()
word = randomObj.choice(wordsAll.words)
print(word)
listWord = list(word)

lenWord = len(word)
CUR_HEALTH = len(lives) - 1

usedLetters = []
slashesWord = []
correctLetters = []
# Заполнение листа слэшей
for el in range(lenWord):
    slashesWord += "_"

while (listWord != slashesWord) and (CUR_HEALTH > 0):
    print(separateLine)
    print(existedCharacters, usedLetters)

    INPUT_ERROR = False
    # Цикл ввода буквы
    while True:
        letters = input(insertCharacter).lower()

        for letter in letters:
            if letter not in usedLetters:
                usedLetters += letters
        break

    # когда буква получена ее необходимо проверить на правильность
    if (letters in word):
        keyChar = 0
        for char in word:
            for letter in letters:
                if letter == char:
                    slashesWord[keyChar] = letter
                    correctLetters += letter
            keyChar += 1
        print(answerYN, 'Правильно (^_^)')
    else:
        CUR_HEALTH -= 1
        print(answerYN, f'{colors.WARNING}НЕ правильно (X_X)')
        
    # подсказки
    if (CUR_HEALTH > 0): 
        print(f'{colors.HEADER}Текущие совпадения:', slashesWord)
        print(colors.OKGREEN, lives[CUR_HEALTH])

if(listWord == slashesWord):
    print('')
    print(f'Вы выиграли! Отгадываемое слово:{colors.HEADER} {word.upper()}')
else:
    print('')
    print(f'{colors.FAIL}Вы проиграли :(')

print(separateLine)


