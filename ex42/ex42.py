##  Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a object of type Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a self.name attribute (set to name)
		self.name = name

## Cat is-a object of type Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a self.name attribute (set to name)
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a self.name attribute (set to name)
		self-name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a object of type person
class Employee(Person):

	def __init__(self, name, salary):
		## 
		super(Employee, self).__init__(name)
		## Employee has-a self.salary attribute (set to salary)
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a object of type Fish
class Salmon(Fish):
	pass

## Halibut is-a object of type Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## kirby is-a Cat
kirby = Cat("Kirby")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet attribute (set to kirby)
mary.pet = kirby

## frank is an Employee
frank = Employee("Frank", 120000)

## frank has-a pet attribute (set to rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()