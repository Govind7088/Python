# _a = 10
# print(_a)

name = "Govind Maurya"
roll = 219067
course = "BCA"
a = f"This is {name}."
b = "This is {}.".format(name)
c = "This is {} and his course {}.".format(name, roll)
d = "This is {1} and his course {0} and his roll {2}.".format(name, roll, course)
e = "This is {0} and his course {2} and his roll {1}.".format(name, roll, course)

print(a)
print(b)
print(c)
print(d)
print(e)