from __future__ import print_function

# sorting


list1 = [6, 4, -5, 3.5]
list1.sort()
print(list1)
list2 = ['ha', 'hi', 'B', '7']
list2.sort()
print(list2)

list1 = [chr(177), 'cat', 'car', 'Dog', 'dog', '8-ball', '5', chr(162)]
list1.sort()
print(list1)

monarchs = [('George', 5), ('Elizabeth', 2), ('George', 6), ('Elizabeth', 1)]
monarchs.sort()
print(monarchs)


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(n=1):
    while (True):
        if isprime(n): yield n
        n += 1


for n in primes():
    if n > 100: break
    print(n)


class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while (True):
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end=' \n')


class AnimalActions:
    def quack(self): return self.strings["quack"]

    def feathers(self): return self.strings["feathers"]

    def bark(self): return self.strings["bark"]

    def fur(self): return self.strings["fur"]


class Duck(AnimalActions):
    strings = dict(
        quack="Quaaaaack",
        feathers="This duck has gray and white feathers",
        bark="The duck cannot bark",
        fur="The duck has no fur"
    )


class Person(AnimalActions):
    strings = dict(
        quack="The person imitates a duck",
        feathers="The person takes a feather from the ground and shows it",
        bark="The person says Woof",
        fur="The person puts on a fur coat"
    )


class Dog(AnimalActions):
    strings = dict(
        quack="The dog cannot quack",
        feathers="The dog has no feathers",
        bark="Arf",
        fur="The dog has white fur with black spots"
    )


def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())


def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest: ")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("- In the doghouse: ")
    for o in (donald, john, fido):
        in_the_doghouse(o)


if __name__ == "__main__": main()\
 \

# exception
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except:
    print('something bad happened')
print('after badness')

# FICA Tax
# Calculate for a single employee and obtain earnings

str1 = "Enter total earnings for this year prior to the current pay period: "
ytdEarnings = eval(input(str1))  # ytd earnings
curEarnings = eval(input("Enter earnings for the current pay period: "))
totalEarnings = ytdEarnings + curEarnings
# Calculate SS tax
socialSecurityBenTax = 0
if totalEarnings <= 117000:
    socialSecurityBenTax = 0.062 * curEarnings
elif ytdEarnings < 117000:
    socialSecurityBenTax = 0.062 * (117000 - ytdEarnings)
# Calculate and display teh FICA tax
medicareTax = 0.0145 * curEarnings
if ytdEarnings >= 200000:
    medicareTax += 0.009 * curEarnings
elif totalEarnings > 200000:
    medicareTax += 0.009 * (totalEarnings - 200000)
ficaTax = socialSecurityBenTax + medicareTax
print("FICA tax for the current pay period: ${0:0,.2f}".format(ficaTax))

""" controller model of previous program
# -- VIEW --


class AnimalActions:
    def quack(self): return self._doAction["quack"]

    def feathers(self): return self._doAction["feathers"]

    def bark(self): return self._doAction["bark"]

    def fur(self): return self._doAction["fur"]

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return "The {} has no {}".format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()

# -- MODEL --


class Duck(AnimalActions):
    strings = dict(
        quack="Quaaaaack",
        feathers="This duck has gray and white feathers"
    )


class Person(AnimalActions):
    strings = dict(
        quack="The person imitates a duck",
        feathers="The person takes a feather from the ground and shows it",
        bark="The person says Woof",
        fur="The person puts on a fur coat"
    )


class Dog(AnimalActions):
    strings = dict(
        bark="Arf",
        fur="The dog has white fur with black spots"
    )


# -- CONTROLLER --


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest: ")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("- In the doghouse: ")
    for o in (donald, john, fido):
        in_the_doghouse(o)


if __name__ == "__main__": main()"""

# Student Grade calculator

def main():
    listOfStudents = obtainListOfStudents()
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter a students name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter students grade on final exam: "))
        category = input("Enter category (LG or PF): ")
        if category.upper() == "LG":
            st = LGstudent(name, midterm, final)
        else:
            st = PFstudent(name, midterm, final)
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tGRADE")
    listOfStudents.sort(key=lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)

class LGstudent:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final

    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name

    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()

class PFstudent(LGstudent):

    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average > 60:
            return "Pass"
        else:
            return "Fail"

main()

