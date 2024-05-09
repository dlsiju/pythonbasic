# Quiz Program
import string

dict = {
    "Which one is the capital of India": "New Delhi",
    "who was the first prime minister of india": "Jawahar Lal Nehru",
    "In which year india become independent": "1947",
    "Which one is the television channel owned by government of india": "Doordarshan"
}

questionTuple = (
    ("Which one is the capital of India", ("Kolkata", 'New Delhi', 'Hyderabad', 'San Francisco')),
    ("who was the first prime minister of india",
     ("Rajendra Prasad", 'Rajiv Gandhi', 'Jawahar Lal Nehru', 'Morarji desai')),
    ("In which year india become independent", ("1925", '1934', '1867', '1947')),
    ("Which one is the television channel owned by government of india",
     ("StartSports", 'Doordarshan', 'BBC', 'AnimalPlanet')),
)
alphabetList = list(string.ascii_uppercase)
print("started the quiz")
print('Follow each question and select your option')
print('Type A if your answer is option A Or B if answer is option B adn so on')
pts = 0
for questionNumber in range(len(questionTuple)):
    print('questionNumber=', questionNumber)
    print(questionNumber + 1, '.', questionTuple[questionNumber][0], "?")
    print('\t\t', alphabetList[0], ')', questionTuple[questionNumber][1][0],
          '\t\t', alphabetList[1], ')', questionTuple[questionNumber][1][1],
          '\t\t', alphabetList[2], ')', questionTuple[questionNumber][1][2],
          '\t\t', alphabetList[3], ')', questionTuple[questionNumber][1][3]
          , sep='')
    selectedOption = ''
    while 1:
        selectedOption = input().upper()
        if selectedOption not in ['N', 'Q', 'A', 'B', 'C', 'D']:
            print('Invalid Option=', selectedOption)
        else:
            break
    if selectedOption == 'N':
        continue
    if selectedOption == 'Q':
        print('you have decided to quite')
        break
    selectedAnswerIndex = alphabetList.index(selectedOption)
    pts = (pts + 1) if dict[questionTuple[questionNumber][0]] == questionTuple[questionNumber][1][
        selectedAnswerIndex] else (pts - 1)

print("completed quiz program")
print('Total points=', pts)
