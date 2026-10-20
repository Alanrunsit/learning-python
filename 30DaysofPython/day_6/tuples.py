emptytuple = ()
print(emptytuple)

brothers = ("John", "David", "Michael")
sisters = ("Jane", "Emily", "Sarah")
siblings = brothers + sisters

print(len(siblings))

family_members= siblings + ("Mom", "Dad")
print(family_members)
siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "eggs", "meat")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_tp=list(food_stuff_tp)
middle_item = food_stuff_tp[len(food_stuff_tp)//2]
first_items = food_stuff_tp[:3]
last_items = food_stuff_tp[-3:]
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country")
else:
    print("Estonia is not a Nordic country")
if 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country")
else:
    print("Iceland is not a Nordic country")