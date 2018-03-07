def hello_world():
  print "My name is Amy"
  print 2 * 2

hello_world()

print range(10)
# 0 to 9 in an array

print range(1, 10)
# 1 to 9 in an array

print range(1, 10, 2)
# 1 to 9 in an array, skipping every  val

def add_two_numbers():
    n1 = 2
    n2 = 3
    answer = n1 + n2
    print "{} plus {} is {}".format(n1, n2, answer)

add_two_numbers()

def add_two_numbers_2(n1, n2):
  print "{} plus {} is {}".format(n1, n2, n1 + n2)

add_two_numbers_2(1,7)

def add_two_numbers_and_return(n1, n2):
  return n1 + n2

res = add_two_numbers_and_return(22,2)

print res
