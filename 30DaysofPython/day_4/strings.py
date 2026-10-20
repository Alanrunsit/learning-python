from operator import index

from pandas import cut


a, b, c ,d = "Thirty", "Days", "Of", "Python"
python = a + " " + b + " " + c + " " + d

x, y, z = "Coding", "For", "All"
coding_for_all = x + " " + y + " " + z
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.index("Coding"))
print(company.replace("Coding", "Python"))
print("Python for Everyone".replace("Everyone", "All"))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
print("Coding for All"[0])
print("Coding for All"[-1])
print("Coding for All"[10])
acronym = "Python For Everyone"
print(acronym[0] + acronym[7] + acronym[11])
acronym = "Coding For All"
print(acronym[0] + acronym[7] + acronym[11])
print(acronym.index("C"))
print(acronym.index("F"))
print(acronym.rfind("l"))
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.rindex("because"))
print(sentence.replace("because because because", ""))
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print("   Coding For All      ".strip())
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
list=["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" ".join(list))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
print(f("8 + 6 = {8 + 6}"))
print(f("8 - 6 = {8 - 6}"))
print(f("8 * 6 = {8 * 6}"))
print(f("8 / 6 = {8 / 6}"))
print(f("8 % 6 = {8 % 6}"))
print(f("8 // 6 = {8 // 6}"))
print(f("8 ** 6 = {8 ** 6}"))