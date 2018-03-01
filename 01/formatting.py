# STRING FORMATTING

age = 22
like = "taylor swift".title()
name = "Amy"

print "My age is {} and I like {}".format(age, like)
print "My age is 22 and I like Taylor Swift"


print "My age is {1} and I like {0}".format(age, like)
print "My age is Taylor Swift and I like 22"

print "My name is {}, my age is {} and I like {}".format(name, age, like)
# # What would we expect?

# print "testing"
# print "xxx {name}, xxx{age}, xxx{like}".format(name=name, age=age, like=like)



