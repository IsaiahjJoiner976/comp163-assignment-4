student_name = "Isaiah"
current_gpa = 3.95
study_hours = int(23)
social_points = int(60)
stress_level = int(50)

print(f"Welcome {student_name}!")
print(f"Starting Stats → GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")
print("")

print("Choose course load:")
print("1. Low Volume (12 credits)")
print("2. Standard (15 credits)")
print("3. High Volume (18 credits)")
print("")

print("--- Course Planning Decision ---")
print("")
choice = input("Your selection: ")

if choice == "1": 
    if current_gpa >= 3.5:
        stress_level -= 10
        study_hours += 6
        social_points += 10
        print("Doing amazing! Keep it up!")
    elif current_gpa >= 3.0:
        stress_level -= 5
        study_hours += 4
        social_points += 30
        print("I'd hope so! Good job!")
    elif current_gpa >= 2.0:
        stress_level += 7
        study_hours += 2
        social_points += 40
        print("Don't start slacking! Keep studying!")
    else:
        stress_level -= 10
        study_hours += 1
        social_points += 60
        print("Stay focused! Try taking more time to study and maybe grab a tutor.")
elif choice == "2":
    if current_gpa >= 3.5:
        stress_level += 10
        study_hours += 7
        social_points -= 40
        print("Doing well! Keep it up!")
    elif current_gpa >= 3.0:
        stress_level += 11
        study_hours += 8
        social_points -= 35
        print("Amazing! Good job!")
    elif current_gpa >= 2.0:
        stress_level += 15
        study_hours += 9
        social_points -= 20
        print("We all start somewhere. Stay focused!")
    else:
        stress_level += 20
        study_hours += 11
        social_points -= 10
        print("There's still time to get your GPA up. Talk to your professor!")
elif choice == "3": 
    if current_gpa >= 3.5:
        stress_level += 28
        study_hours += 15
        social_points -= 35
        print("Amazing! Good job!")
    if current_gpa >= 3.0:
        stress_level += 25
        study_hours += 14
        social_points -= 30
        print("Going strong! Good job!")
    elif current_gpa >= 2.0:
        stress_level += 20
        study_hours += 12
        social_points -= 40
        print("Could be better. Keep studying!")
    else:
        stress_level += 50
        study_hours += 23
        social_points -= 50
        print("Don't give up! Take more time to study and maybe grab a tutor.")
else:
    print("Invalid input")

print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress level: {stress_level}")
print("")

print("--- Study Strategy Decision ---")
print("")
study_options = ["Programming", "Math", "English", "History"]

print("Choose which course to study: ", study_options)
print("")

study_decision = input("Your decision: ")

if study_decision not in study_options:
    print("Invalid course.")
else:
    if (study_decision == "Programming"):
        if (study_decision == "Programming") and current_gpa >= 3.5:
            current_gpa += .2
            social_points -= 3
        elif (study_decision == "Programming") and current_gpa >= 3.0:
            current_gpa += .15
            social_points -= 6
        elif (study_decision == "Programming") and current_gpa < 3.0:
            current_gpa += .1
            social_points -= 12
    elif (study_decision == "Math"):
        if (study_decision == "Math") and current_gpa >= 3.5:
            current_gpa += .15
            social_points -= 2
        elif (study_decision == "Math") and current_gpa >= 3.0:
            current_gpa += .12
            social_points -= 5
        elif (study_decision == "Math") and current_gpa < 3.0:
            current_gpa += .05
            social_points -= 10
    elif (study_decision == "English"):
        if (study_decision == "English") and current_gpa >= 3.5:
            current_gpa += .13
            social_points -= 2
        elif (study_decision == "English") and current_gpa >= 3.0:
            current_gpa += .1
            social_points -= 5
        elif (study_decision == "English") and current_gpa < 3.0:
            current_gpa += .04
            social_points -= 6
    elif (study_decision == "History"):
        if (study_decision == "History") and current_gpa >= 3.5:
            current_gpa += .1
            social_points -= 2
        elif (study_decision == "History") and current_gpa >= 3.0:
            current_gpa += .07
            social_points -= 8
        elif (study_decision == "History") and current_gpa < 3.0:
            current_gpa += .02
            social_points -= 10
    else:
        social_points -= 15
        print("You need to get to work!")
if (study_decision == "Programming" or study_decision == "Math"):
    print(f"Current GPA: {current_gpa} and Social Points: {social_points}")
    print("Technical approach! Boosts GPA but lowers social time.")
elif (study_decision == "English" or study_decision == "History"):
    print(f"Current GPA: {current_gpa} and Social Points: {social_points}")
    print("Liberal arts approach! GPA boost but less social experience.")
print("")

print("--- Final Semester Assessment ---")
print("")

print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress level: {stress_level}")
print("")

excelling_grade = current_gpa >= 3.5 
passing_grade = current_gpa >= 2.0
failing_grade = current_gpa < 2.0
end_options = ["Study", "Work", "Party"] 
if excelling_grade == True:
    print("Mastered your courses!")
    print(end_options)
    end_choice = input("How will you spend your summer: ")
    if end_choice is not end_options[0] or end_options[1]: 
        print("Go crazy! You deserve it!")
    elif end_choice is end_options[0]:
        print("Look at you! Keeping ahead.")
    elif end_choice is end_options[1]:
        print("Working already!? I knew you could do it!")
elif passing_grade == True:
    print("Courses passed!")
    print(end_options)
    end_choice = input("What will you do this summer: ")
    if end_choice is not end_options[0] or end_options[1]: 
        print("Fair. You should enjoy your summer.")
    elif end_choice is end_options[0]:
        print("Responsible. I like it.")
    elif end_choice is end_options[1]:
        print("Money is always good.")
elif failing_grade == True:
    print("Courses...failed.")
    print(end_options)
    end_choice = input("You going to study this summer...? ")
    if end_choice is not end_options[0] or end_options[1]: 
        print("Oh...ok. Sure. It is summer...I guess...")
    elif end_choice is end_options[0]:
        print("That's what I like to hear! Never too late to improve!")
    elif end_choice is end_options[1]:
        print("You...aren't giving up are you? ")
