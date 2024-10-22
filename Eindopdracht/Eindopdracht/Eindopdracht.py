#Youssef Abrazi eindopdracht fitness tracker

from datetime import date
import time
from collections import defaultdict
import statistics

training_list = []
time_exit = 10
min_weight = 30
max_weight = 300
training_start = input("Do you want to start a new training? (Y/N): ").lower()
EMPTY_LIST = 0
NOT_EMPTY = 1

#This while loop checks if the input given is valid. If not it will keep asking to type in a valid answer.
while training_start != "y" and training_start != "n":
    training_start = input("Your input was invalid. Please answer with either \"Y\" for Yes or \"N\" for No: ").lower()

#If the user decides not to start a new training session, 
#the user gets asked if he wants to check his training history
if training_start == "n":
    check_list = input("Do you want to check you training history?: (Y/N) ").lower()

    #This while loop checks if the input given is valid. If not it will keep asking to type in a valid answer.
    while check_list != "y" and check_list != "n":
        check_list = input("Your input was invalid. Please answer with either \"Y\" for Yes or \"N\" for No: ").lower()

    #If the user decides to check the training history, the list will be printed or else the program will terminate
    #If there are no items in the list then the program will show a message & the program will terminate after 10 secs
    if check_list == "y":
        if len(training_list) < NOT_EMPTY:
            print("Sorry! Unable to print training history, because there is no training history yet")
            time.sleep(time_exit)
            exit()
        else:
            check_list(training_list)
    else:
        exit()

person_weight = input("How much do you weigh in KG?: ")

#Checks whether the input is a valid input. First of all whether it's a digit or a string and
#if it's a digit and within a logical range or else it ask for another input until it get's a correct value
while person_weight.isdigit() == False or int(person_weight) < min_weight or int(person_weight) > max_weight:
    person_weight = input("Your input was invalid. Please answer with a number between \"" + 
                          str(min_weight) + "\" and \"" + str(max_weight) + "\": ")

#This function is to calculate the total time from start to end
def total_time(time_start, time_end):

    total_time = round(time_end - time_start)

    return total_time

#This function calculates the total calories burnt by every workout by using the persons weight as an argument 
#and it returns also information about the workout like the date, type of workout and 
#total time (by using the total_time function)
def training(weight_in_kg):

    max_decimals = 3
    CONVERT_SECS_TO_HOURS = 3600
    training_day = date.today()
    person_kg = float(weight_in_kg)
    training_type = input("What type of training are you doing?: (Cardio/Weight) ").lower()
    met_weight_light = 3
    met_weight_medium = 4
    met_weight_heavy = 6
    met_cardio_walking = 3.5
    met_cardio_running = 8
    met_cardio_cycling = 7.5
    
    #This while loop checks if the input given is valid. If not it will keep asking to type in a valid answer.
    while training_type != "cardio" and training_type != "weight":
        training_type = input("Your input was invalid. Please answer with either \"Cardio\" or \"Weight\": ").lower()
    
    #This if statement checks the type of training to eventually return the selected workout and also to be able to
    #measure the MET-value which will be needed to calculate the burnt calories which also will be returned
    if training_type == "weight":
        weight_intensity = input("What is the intensity of your workout?: (Light/Medium/Heavy) ").lower()
        
        #This while loop checks if the input given is valid. If not it will keep asking to type in a valid answer.
        while weight_intensity != "light" and weight_intensity != "medium" and weight_intensity != "heavy":
            weight_intensity = input("Your input was invalid."
                                        "Please answer with either \"Light\", \"Medium\" or \"Heavy\": ").lower()
        
        #This if statement checks the intensity of the weight training to eventually return the intensity workout and
        #also to be able to measure the MET-value which will be needed to calculate the burnt calories 
        #which also will be returned
        if weight_intensity == "light":
            met_value = met_weight_light
        elif weight_intensity == "medium":
            met_value = met_weight_medium
        elif weight_intensity == "heavy":
            met_value = met_weight_heavy

        #Returns the workout type as a string based on the values given as input
        workout_type = weight_intensity + " " + training_type

    #This if statement checks the type of training to eventually return the selected workout and also to be able to
    #measure the MET-value which will be needed to calculate the burnt calories which also will be returned
    elif training_type == "cardio":
        cardio_type = input("What kind of cardio will you be doing?: (Walking/Running/Cycling) ").lower()
        
        while cardio_type != "walking" and cardio_type != "running" and cardio_type != "cycling":
            cardio_type = input("Your input was invalid."
                                "Please answer with either \"Walking\", \"Running\" or \"Cycling\": ").lower()
        
        #This if statement checks the type of cardio to eventually return the selected workout and also to be able to
        #measure the MET-value which will be needed to calculate the burnt calories which also will be returned
        if cardio_type == "walking":
            met_value = met_cardio_walking
        elif cardio_type == "running":
            met_value = met_cardio_running
        elif cardio_type == "cycling":
            met_value = met_cardio_cycling

        #Returns the type of cardio as workout_type to be able to return the workout type regardless if it's a weighted
        #or cardio training
        workout_type = cardio_type

    #The time of the start of the training will be measured to be able to use the function total_time() later
    #to measure and return the total time spent in training which also be used to calculate the burnt calories
    #also the line "Training is running" is printed to give the user feedback    
    training_in_progress = True
    begin_time = time.time()
    print("\nTraining is running\n")

    #When the training starts, the variable "training_is_running" is set to "True" and
    #while it's set to True the user is able to give input to stop the training at any time
    while training_in_progress == True:
        stop_training = input("Type in \"stop\" to stop the training ").lower()

        #If the user decides to stop the training by typing "stop", the variable "training_in_progress" will be set to
        #False to end the current training session and the end time of the training will be recorded and then used
        #together with the begin time as parameters to use the function total_time() and converted into hours and
        #rounded into 3 decimals. Also the calories burnt will be calculated by using the met value, the weight of
        #the user and the total training time in hours
        if stop_training == "stop":
            training_in_progress = False
            end_time = time.time()
            training_in_hours = round((total_time(begin_time, end_time) / CONVERT_SECS_TO_HOURS), max_decimals)
            calories_burnt = met_value * person_kg * training_in_hours

            #The user will be asked if he wants to add a new training (i.e. he wants to switch from weight to cardio)
            continue_training = input("Do you want to start a new training?: (Y/N) ").lower()

            #This while loop checks if the input given is valid. If not it will keep asking to type in a valid answer.
            while continue_training != "y" and continue_training != "n":
                continue_training = input("Your input was invalid."
                                          "Please answer with either \"Y\" for \"Yes\" or \"N\" for \"No\": ").lower()
            
            #If the user decides to continue the training, a new training will be started by invoking 
            #the training() function and adding it also to the list "training_list[]".
            if continue_training == "y":
                training_list.append(training(person_weight))
    #The date, type of workout, total time in training and the calories burnt of this training session of the user will
    #be returned as a tuple
    return (training_day, workout_type, training_in_hours, calories_burnt)

def check_list(workout_list):

    checking_list = workout_list

    #The dictionary is used to be able to store the amount of calories and also
    #to find the training_days easier than with a list
    total_calories = defaultdict(float)
    total_workouts = 0
    CONVERT_TO_MINS = 60
    new_list = []

    #This for-loop is used to convert training _in_hours to minutes and add it to a new list
    for workout in checking_list:
        training_day, workout_type, training_in_hours, calories_burnt = workout
        training_in_minutes = training_in_hours * CONVERT_TO_MINS

        new_list.append((training_day, workout_type, training_in_minutes, calories_burnt))

    #This for-loop is used to calculate the total calories for each day (every day can have multiple training sessions) 
    #and to count the amount of trainingsessions per day
    for training in new_list:
        training_day, _, _, calories_burnt = training
        total_calories[training_day] += calories_burnt
        total_workouts += 1

    #This for-loop shows the total calories and total workouts for each day in
    #the dictionary "total_calories" and prints them
    for date, tot_calories in total_calories.items():
        print("On " + str(date) + " you have burnt a total of "
             + str(tot_calories) + " calories in " + str(total_workouts) + " workouts.")

    #Making a new list with only the calories and another list with only the total time in minuts which are found in
    #the list "new_list"
    calories = [training[3] for training in new_list]
    tot_time = [training[2] for training in new_list]

    #Checking if the list "calories" is empty before using statisics
    if len(calories) > EMPTY_LIST:
        avg_calories_burnt = statistics.mean(calories)
        print("The average burnt calories per training is " + str(avg_calories_burnt) + " calories.")
        med_calories = statistics.median(calories)
        print("The median calories burnt per training is " + str(med_calories) + " calories.")
        max_calories = max(calories)
        print("The maximum calories burnt in a training is " + str(max_calories) + " calories.")
        min_calories = min(calories)
        print("The minimum calories burnt in a training is " + str(min_calories) + " calories.")

    #Checking if the list "tot_time" is empty before using statisics
    if len(tot_time) > EMPTY_LIST:
        avg_time = statistics.mean(tot_time)
        print("The average time spent per training is " + str(avg_time) + " minutes.")
        med_time = statistics.median(tot_time)
        print("The median time spent per training is " + str(med_time) + " minutes.")
        max_time = max(tot_time)
        print("The maximum time spent on a training is " + str(max_time) + " minutes.")
        min_time = min(tot_time)
        print("The minimum time spent on a training is " + str(min_time) + " minutes.")

    return

#This if statement checks if the user wants to start a new training session.
#if the answer is yes, then it starts the function and adds it as a tuple into the list of training sessions
#and also invokes the function "check_list" to give a summary when the user exits the function "training"
if training_start == "y":
    training_list.append(training(person_weight))
    check_list(training_list)