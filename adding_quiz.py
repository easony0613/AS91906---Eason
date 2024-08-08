import json

''''''
# creating the dictionary
quiz = dict()

# creating the keys
question = "question"
choice = "choices"
answer = "answer"

# raising the flag
again = True

# this variable keep track of how many question is already in the GUI so that the new question added will be question counter + 1
counter = 24

# this list keep track of the new choices the user inputs for their new question
given_choice = []

with open("quiz.json") as f:
    quiz = json.load(f)

# raising the flag
while again != False: 
    
    user_question = input("Please enter your question: ").capitalize()
    for i in range(4): # the loop will repeat 4 times because the user will only input 4 choices
        user_choice = input("Please enter your choice: ").title()
        given_choice.append(user_choice)

    user_answer = input("Please enter your answer for the question: ").capitalize()
    counter +=1 # after the user inputed their choices and answers, counter will increase to indicate a new question has been added

    # putting the key and values into the quiz dictionary
    quiz[f"question{counter}"] = {question: user_question, choice: given_choice, answer: user_answer}

    more_question = input("Do you want to add more questions(yes/no): ").lower()
    while more_question not in ["yes", "no"]:
        print("please select yes or no")
        more_question = input("Do you want to add more questions(yes/no): ").lower()

    if more_question == "yes":
        again = True # if the user want to continue then the loop will continue
        
        with open("quiz.json", "w") as f: # dumping their previous question into the json file first before taking the next
            json.dump(quiz, f, indent=2)
        given_choice.clear() # clearing the existing choices and make the list empty for the next choices

    else:
        
        again = False # once the user is done adding questions, the program will dump their question into a json file


# when the user does not want to add anymore questions, the quiz dictionary will be dumped into a json file
with open("quiz.json", "w") as f:
    json.dump(quiz, f, indent=2)

