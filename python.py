from datetime import datetime

now = datetime.now()
print now

# a = raw_input("You shall pass,but give me your name! ") 
# print "This is a wonder, my name is also %s" % (a)

# def clinic():
#     print "You've just entered the clinic!"
#     print "Do you take the door on the left or the right?"
#     answer = raw_input("Type left or right and hit 'Enter'.").lower()
#     if answer == "left" or answer == "l":
#         print "This is the Verbal Abuse Room, you heap of parrot droppings!"
#     elif answer == "right" or answer == "r":
#         print "Of course this is the Argument Room, I've told you that already!"
#     else:
#         print "You didn't pick left or right! Try again."
#         clinic()

# clinic()

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "r")

# for item in my_list:
#     f.write(str(item) + "\n")

print f.read()
print f.readline()
print f.readline()
print f.readline()
f.close()

