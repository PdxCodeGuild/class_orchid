import random
from api import questions


print('Hello and welcome to Quizzar! ')

user_name = input('Please enter your name below \n: ').title()

starter = print(f'Hello {user_name}! Lets begin the game!\n\n')

total = 0
for question in questions['results']:
    #i used the for loop in order to be able to loop through each question
    while True:
        # i used the while loop so i can run things seperately from the for loop
        # and allow it to run as many times as it needs to to get the correct input before moving forward
        print(question['question'].replace('&quot;', '"').replace('&#039;', "'"))
        #where i print the questions
        correct_answer = question['correct_answer'].replace('&amp', '&').replace('&quot;', '"').replace('&#039;', "'")
        #how i grab the correct answer from my api
        incorrect_answers = question['incorrect_answers']
        #how i grab the incorrect answers from my api
        if len(incorrect_answers) < 4:
            # i did <4 because i only want four items in one list c/i answers
            incorrect_answers.append(correct_answer)
            #appending the correct answers to the incorrect answers list
            random.shuffle(incorrect_answers)
            #i used the random.shuffle to shuffle the answers everytime they are printed
            print(incorrect_answers)
            # i printed the incorrect answers list so the user can see the options
        choice = input(f'Please enter your selection below! \n: ')
        #this is where the user inputs their choice
        if choice.lower() == correct_answer.lower():
            #i .lowered here so that the output can be untouched
                total += 1
                #i kept a running of sum of how many questions the user got correct
                print(f"{correct_answer} was the correct answer! Congrats you've earned 1 point!\n\n")
                # this is where i tell the user that they earned a point for the correct answer
                break
            # i end the loop here to move forward with the question
        elif choice.lower() in [answer.lower() for answer in incorrect_answers]:
            # i did a list comprehension here in or to get the lower cased version of the incorrect answers without changing its output
                print(f'{choice} was not the correct answer. You have earned 0 points. \n\n')
                #this is where i tell the user they did not answer correctly and earned 0 points
                break
            #i break here to move forward to the next question
        else:
            print('invalid input  please try again')
            # this is where i inform the user of the error and allow them to start again
print(f"You have scored a total of {total}/{len(questions['results'])}")
#this is where i print the final total




