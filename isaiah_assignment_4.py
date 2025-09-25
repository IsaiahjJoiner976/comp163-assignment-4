student_name = "Isaiah"
current_gpa = 3.95
study_hours = int(23)
social_points = int(60)
stress_level = int(50)

print(f"Welcome {student_name}!")
print(f"Starting Stats → GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

print("Choose course load:")
print("1. Low Volume (12 credits)")
print("2. Standard (15 credits)")
print("3. High Volume (18 credits)")

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
