#Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update('Nvidia','Nebius', 'Meta')
it_companies.pop()
"""
remove-->If item isn't in group, will raise a KeyError
discard-->Regardless, will remove 
"""

#Level 2
A.update(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isidsjoint(B))
A.union(B)
B.union(A)
print(A.symmetric_difference(B))

del A, B, it_companies

#Level 3
setage = set(age)

"""""
string--> immutable text
list--> Mutable and ordered
tuple--> immutable and ordered
set--> mutable and unordered
"""
teach = "I am a teacher and I love to inspire and teach people"
print("Unique Words", len(set(teach.split())))