dict = {
        "name" : "haseeb",
        "age" : 20,
        "city" : "lahore",
}
print(dict.keys())
print(dict.values())

print(dict["name"])
print(dict["age"])
print(dict["city"])
dict ["age"] = 19
print(dict["age"])
         

student = {
        "name" : "haseeb",
        "subjects" : {
                "phy" : 90,
                "chem" : 95,
                "math" : 94
        }

}
new_dict = {"city" : "lahore"}
print(student.update(new_dict))
print(list(student.keys()))
print(list(student["subjects"]))
new_dict = {"city" : "lahore"}
student.update(new_dict)
print(student)
