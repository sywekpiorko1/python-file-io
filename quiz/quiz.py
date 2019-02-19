import difflib

def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Quit game")
    
    option = input("Enter option: ")
    return option
    
def ask_questions():
    questions = []
    answers = []
    
    # we using 'with' block as it handles lot of thinks for us, i.e. we dont have to worry about closing file when exiting 'with' block
    with open("questions.txt", "r") as file:
        # 'splitlines()' function split file into lines
        lines = file.read().splitlines()
        
    # we using 'enumerate' which turn each of these lists into a tuple with a line number stored in 'i' and the text in 'text', so if 'i' is even then we say that's the question, if 'i' is odd that's the answer
    for i,text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
            
    number_of_questions = len(questions)
    # we use zip to link two lists into one tuple in memory, see example below
    questions_and_answers = zip(questions, answers)
    # print(list(questions_and_answers))
    # [('My name', 'Sylwester'), ('Capital of Ireland ?', 'Dublin'), ('Capital of Poland ?', 'Warsaw')]
    
    score = 0
      
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("right")
            print(score)
        else:
            if (sum([i[0] != ' ' for i in difflib.ndiff(guess, answer)]) / 2) <= 2:
                print(sum([i[0] != ' ' for i in difflib.ndiff(guess, answer)]))
                print("Spelled wrong, but wright!")
                score += 1
                print(score)
            else:
                print("wrong!")

    print("You got  {0} correct out of {1}".format(score, number_of_questions))


def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))

    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
    
    
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option. Try again ...")
        print("")
            
game_loop()