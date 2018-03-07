number = raw_input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer

if number > 10:
  print "Too high!"
elif number <= 0:
  print "Too low!"
else:
  print "Perfect!"