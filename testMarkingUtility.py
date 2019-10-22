
import keyboard
import time
import sys

NUMBER_OF_QUESTIONS = 4
STARTING_QUESTION = 1
run_once = False
pupil_name = ""

#Calculates the scores of the student
def display_Scores(scores_list, student_name):
    print("The highest score for "+student_name+" is " + str(max(scores_list)))
    print("The lowest score for "+student_name+" is " + str(min(scores_list)))
    print("The average score for "+student_name+" is " + str(sum(scores_list) / NUMBER_OF_QUESTIONS))

    process_again = input("Do you want to process more scores y/n? \n")
    if yes_or_no(process_again):
        add_Scores([], 1)
    else:
        print("Program closing \n")
        time.sleep(2)
        sys.exit()

#Module for user input - takes number of qustions as arguement
def add_Scores(marks_Scored, x):
    another_question = True
    while another_question:
            current_score = (input("What did the pupil score on question "+ str(x) + "? \n"))
            if current_score.isdigit():
                marks_Scored.append(current_score)
            else:
                escape_function(marks_Scored)
            time.sleep(0.2)
            x += 1
            marks_Scored = [int(i) for i in marks_Scored]  # Parse array to integer



def escape_function(marks_Scored):
    if len(marks_Scored) == 0:
        print("You have entered no data please enter some data and try again!\n")
        add_Scores(marks_Scored, STARTING_QUESTION)
    else:
        add_another_score = input("Are you sure that you dont want to add another score to the test? Y/N \n").lower().strip()
        print(marks_Scored)
        if yes_or_no(add_another_score):
            ask_for_name()
            display_Scores(marks_Scored, pupil_name)
        else:
            add_Scores(marks_Scored, len(marks_Scored)+1)

def yes_or_no(user_answer):
    user_answer.strip().lower()
    if user_answer[0] == "y":
        return True
    elif user_answer[0] =="n":
        return False
    else:
        print("Please enter y or n")
        yes_or_no()

def on_start():
    if run_once == True:
        return
    else:
        add_Scores([],STARTING_QUESTION)
        print("Here we go")
        time.sleep(1)

def ask_for_name():
   global pupil_name
   pupil_name= input("What is the name of this pupil? \n")


on_start()






