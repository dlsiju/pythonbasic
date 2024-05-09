# remove items form dictionary

empl_dict = {
    "name": "Karthik",
    "age": 25,
    "salary": 80000,
    "jobtitle": "Software developer"
}
print('empl_dict=', empl_dict)
print("name=",empl_dict["name"])
print("age=",empl_dict["age"])
print("salary=",empl_dict["salary"])
print("jobtitle=",empl_dict["jobtitle"])
del empl_dict["name"]
print('empl_dict after removing name', empl_dict)
if 'salary' in empl_dict and empl_dict['salary'] == 80000:
    del empl_dict['salary']
print('employee dicitonary after removing salary=', empl_dict)
empl_dict["position"] = empl_dict.pop("jobtitle")
print('empl_dict after updating jobtitle=', empl_dict)
