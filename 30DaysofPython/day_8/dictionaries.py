dog = {}
dog["name"]="unicorn"
dog["color"]="white"
dog["breed"]="corgi"
dog["age"]=4
student = {
    "first_name" : "Alan",
    "last_name" : "Lei",
    "gender" : "Male",
    "age" : 16,
    "martial_status" : "independent",
    "skills" : ["Programming","Viola","Connectivity","Leadership"],
    "country" : "USA",
    "city" : "EB",
    "address" : "slow down",
}
print(len(student))
print("skills: ",student.get("skills"))
student["skills"].append("Vibecoding")

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
del student["address"]
del dog
