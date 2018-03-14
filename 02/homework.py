# http://blamcast.net/python/
# exercise 12 - 35

# EX 12

# name = raw_input("Name? ")
# age = raw_input("Age? ")
# weight = raw_input("Weight? ")
# height = raw_input("Height? ")

# print "So you're name is {}, you're {} years old {} heavy and {} tall".format(name, age, weight, height)

# EX 13

# from sys import argv

# script, first, second, third = argv

# print "this script is called:", script
# print "your first variable is:", first
# print "your second variable is:", second
# print "your third variable is:", third

# EX 14

# from sys import argv

# script, user_name = argv

# prompt = '> '

# print "Hi {}, I'm the {} script.".format(user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me {}?".format(user_name)
# likes = raw_input(prompt)

# print "Where do you live {}?".format(user_name)
# lives = raw_input(prompt)

# print "What kind of computer do you have? {}".format(user_name)
# computer = raw_input(prompt)

# print """

# Alright, so you said {} about liking me.
# You live in {}.
# You have a {} computer.
# Nice
# """.format(likes, lives, computer)

# EX 15

# from sys import argv

# script, filename = argv

# txt = open(filename)

# print "Here's your file {}".format(filename)
# print txt.read()

# print "I'll also ask you to type it again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# EX 16

# from sys import argv

# script, filename = argv

# print "We're going to erase {}".format(filename)
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."

# raw_input("?")

# print "Opening the file..."
# target = open(filename, "w")

# print "Truncating the file. Goodbye!"
# target.truncate()

# print "Now I'm going to ask you for three lines."

# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")

# print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print "And finally, we close it."
# target.close()

# EX 17

# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from {} to {}".format(from_file, to_file)

# input = open(from_file)
# indata = input.read()

# print "The input file is {} bytes long".format(len(indata))

# print "Does the output file exist? {}".format(exists(to_file))
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# output = open(to_file, 'w')
# output.write(indata)

# print "All done."

# output.close()
# input.close()

# EX 18

def print_two(arg1, arg2):
  print "arg1: {}, arg2: {}".format(arg1, arg2)

def print_one(arg1):
  print "arg1 {}".format(arg1)

def print_none():
  print "no args for me"

print_two('a', 'b')
print_one('c')
print_none()

# EX 19

# EX 20

# EX 21

# EX 22

# EX 23

# EX 24



