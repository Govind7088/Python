'''
name="Govind"
print(name[:5])
print(name[0:])
c=name[-4:-1]
print(c)
d=name[0::2]
print(d)

'''

# String Function

'''

story="once upon a time there was live a boy in a village. He lived in Mayur vihar phase 1"
print(len(story))
print(story.endswith("jhdasg"))
print(story.endswith("phase 1"))
print(story.count("O"))
print(story.count("i"))
print(story.capitalize())
print(story.upper())
print(story.lower())
print(story.find("vihar"))
print(story.replace("boy", "Govind"))

'''

# Escape sequence character.

'''
story="I am Govind Maurya. \n He is \\ good \t boy."
print(story)

'''

# write a program to print good after noon with name.
 
'''
name=input("Enter Your Name : ")
print("Good After Noon, "+ name)

'''
# Write a program to fill in letter template with your name and date.


letter='''Dear, <|NAME|>
You are selected!, And your welcome in our company and come in our company and visit our company
Date : <|DATE|>
'''
name=input("Enter Your Name : ")
date=input("Enter Date : ")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)



