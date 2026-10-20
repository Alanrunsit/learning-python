lst = []

lst = [1, 2, 3, 4, 5]

print(len(lst))

print(lst[0],lst[len(lst)//2],lst[-1])

mixed_data_types = ["Alan", 16, 5.10, "single", "wut"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

it_companies[0] = "Meta"
print(it_companies)

it_companies.append("SpaceX")
it_companies.insert(len(it_companies)//2, "Tesla")
it_companies[0] = it_companies[0].upper()
print(", ".join(it_companies))
print("Tesla" in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[len(it_companies)//2])

it_companies.pop(0)
it_companies.pop(len(it_companies)//2)
it_companies.pop(-1)
it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack[full_stack.index("Redux")+1 : full_stack.index("Redux")+1] = ["Python", "SQL"] 
print(full_stack)

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
if len(ages) % 2 == 0:
    median_age = (ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2
else:
    median_age = ages[len(ages)//2]

average_age = sum(ages)/len(ages)
print("Range= ", max_age - min_age)
print(abs(min_age-average_age) == abs(max_age-average_age))

import sys
sys.path.append("/day_5")
from countries import countries

if len(countries) % 2 == 0:
    middle_countries = countries[len(countries)//2 - 1:len(countries)//2 + 1]
else:
    middle_countries = countries[len(countries)//2]

if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]

mini_countries = ["China", "Russia", "USA", "Finland", "Sweden"]
china, russia, usa, *scandic = mini_countries
