# abs() : returns the absolute value of the given numbers

integer = -20
print('Absolute value of -20 is:', abs(integer))

# abs(num)




# getattr() : returns the value of the named attirbute of an object

class Person:
	age = 31
	name = "Tim"

# getattr(object, name[, default])
# or, equivalently:  object.name

person = Person()
print('The age is', getattr(person, "age"))
print('The age is', person.age)

print('The sex is:', getattr(person, 'sex', 'Male')) # providing a default value 'Male'

