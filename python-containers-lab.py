students = ["zaheed", "prabh", "madiha", "matt", "alex"]
print(students)

foods = ('apples', 'tuna sandwich', 'mac & cheese', 'fried chicken', 'peanut butter', 'pho', 'green curry')
for food in foods:
    print(f"{food} is a good food.")
    print( foods[2:] )

home_town = {
    "city": "dark side of the moon",
    "state" : "space",
    "population": 200000
}
print(f"I was born in {home_town['city']}, {home_town['state']}, population of {home_town['population']}")
for key, val in home_town.items()  :
    print(key, val)

cohort = {students[i]: foods[i] for i in range(len(students))}
print(cohort)

students_awesome = []
for student in students:
    students_awesome.append(student + " are cultural mavens")
print(students_awesome) 




