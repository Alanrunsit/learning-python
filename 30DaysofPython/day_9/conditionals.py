#level 1

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
elif 0 < age < 18:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive")
else:
    print("How is that possible...")

my_age = 16
diff = int(my_age - age)
if diff == 0:
    print("We are the same age!")
elif diff > 0:
    print(f"I am {abs(diff)} years older than you!")
elif diff < 0:
    print(f"You are {abs(diff)} years older than me!")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else: 
    print(f"{a} is equal to {b}")

#level 2
grade = int(input("Enter your grade: "))
if 100 >= grade >= 90:
    print("Grade: A")
elif 90 > grade >= 80:
    print("Grade: B")
elif 80 > grade >= 70:
    print("Grade: C")
elif 70 > grade >=60:
    print("Grade: D")
elif 60 > grade:
    print("Grade: F")

month = str(input("Enter a month:")).capitalize()
seasons = {
    "January" : "Winter",
    "February" : "Winter",
    "March" : "Spring",
    "April" : "Spring",
    "May" : "Spring",
    "June" : "Summer",
    "July" : "Summer",
    "August" : "Summer",
    "September" : "Fall",
    "October": "Fall",
    "November" : "Fall",
    "December" : "Winter"
}
print(f"Month: {month}\nSeason: {seasons.get(month)}")

fruit = str(input("Enter a fruit"))
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print("fruit is already in list!")
else:
    fruits.append(fruit)
    print(fruits)

#level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
     }
 }

if 'skills' in person:
    print(f"Middle skill: {person['skills'][len(person['skills'])//2]}")
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python is one of the skills")
    else:
        print("Python is not one of the skills")
if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("He is a front end developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB', 'Python'}.issubset(set(person['skills'])):
        print("He is a fullstack developer")
    else:
        print("unknown title")
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")