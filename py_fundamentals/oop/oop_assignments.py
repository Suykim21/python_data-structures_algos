'''

Assignment: Bike
Create a new class called Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?


'''

# OOP Bike

# define the Bike class
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'

    def drive(self):
        print 'Driving'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5

# create instances and run methods
bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()


'''
Assignment: Car
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

A sample output would be like this:

Price: 2000
Speed: 35mph
Fuel: Full
Mileage: 15mpg
Tax: 0.12
Copy
Price: 2000
Speed: 5mph
Fuel: Not Full
Mileage: 105mpg
Tax: 0.12
Copy
Price: 2000
Speed: 15mph
Fuel: Kind of Full
Mileage: 95mpg
Tax: 0.12
Copy
Price: 2000
Speed: 25mph
Fuel: Full
Mileage: 25mpg
Tax: 0.12
Price: 2000
Speed: 45mph
Fuel: Empty
Mileage: 25mpg
Tax: 0.12
Copy
Price: 20000000
Speed: 35mph
Fuel: Empty
Mileage: 15mpg
Tax: 0.15
'''

# OOP Car

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed 
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
           self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)
        
car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)


'''
Assignment: Product
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product Class:
Attributes:

• Price

• Item Name

• Weight

• Brand

• Status: default "for sale"
Methods:

• Sell: changes status to "sold"

• Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

• Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.

• Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
'''


'''
Optional Assignment: Store
Now, let's build a store to contain our products by making a store class and putting our products into an array.

Store class:
Attributes:

• products: an array of products objects

• location: store address

• owner: store owner's name
Methods:

• add_product: add a product to the store's product list

• remove_product: should remove a product according to the product name

• inventory: print relevant information about each product in the store
You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.
'''

'''
Assignment: Animal
Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

Objective
The objective of this assignment is to help you understand inheritance. Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.

Animal Class
Attributes:

• name

• health
Methods:

• walk: decreases health by one

• run: health decreases by five

• display health: print to the terminal the animal's health.
Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

Dog Class
• inherits everything from Animal
Attributes:

• default health of 150
Methods:

• pet: increases health by 5
Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

Dragon Class
• inherits everything from Animal
Attributes:

• default health of 170
Methods:

• fly: decreases health by 10

• display health: prints health by calling the parent method and prints "I am a Dragon"
Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
'''

# Create a class Animal

class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'My name is: ' + self.name
        print 'I have: ' + str(self.health) + ' health'

animal = Animal('Garfield')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self):
        self.health += 5
        return self

dog = Dog('Odie')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

dragon = Dragon('Nightwing')
dragon.fly().displayHealth()

'''
Assignment: MathDojo
HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

PART I
Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

md.add(2).add(2,5).subtract(3,2).result
which should perform 0+2+(2+5)-(3+2) and return 4.

PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

PART III
Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
'''

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self

'''
Assignment: Call Center
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call Class
• Create your call class with an init method. Each instance of Call() should have:
Attributes:

• unique id

• caller name

• caller phone number

• time of call

• reason for call
Methods:

• display: that prints all Call attributes.
CallCenter Class
• Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
Attributes:

• calls: should be a list of call objects

• queue size: should be the length of the call list
Methods:

• add: adds a new call to the end of the call list

• remove: removes the call from the beginning of the list (index 0).

• info: prints the name and phone number for each call in the queue as well as the length of the queue.
You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.

Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
'''

'''
Assignment: Hospital
You're going to build a hospital with patients in it! Create a hospital class.

Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?

Patient:
Attributes:

• Id: an id number

• Name

• Allergies

• Bed number: should be none by default
Hospital
Attributes:

• Patients: an empty array

• Name: hospital name

• Capacity: an integer indicating the maximum number of patients the hospital can hold.
Methods:

• Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

• Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
'''

'''
Optional Assignment: Underscore
Your own custom Python Module!
Did you know that you can actually create your own custom python module similar to the Underscore library in JavaScript? That may be hard to believe, as the things you've learned might seem simple (again, we try to make it look simple... (-: ), but in truth, you know how to create significant Python modules of your own. To create a custom Python module, you will simply add methods to a Python class!

You will create the following methods from the underscore library as methods of the "_" object. Pay attention to what you have to change, in terms of parameters for each method as well as implementation.

class Underscore(object):
    def map(self):
        # your code here
    def reduce(self):
        # your code here
    def find(self):
        # your code here
    def filter(self):
        # your code
    def reject(self):
        # your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
Copy
In the code above, you just created your own custom Python module/library that others can use! How can others use the methods in your library? By calling the properties stored in the class you defined (e.g. _.map(), _. reduce(), _.find(), etc).

Your assignment is to implement the 5 methods above using delegating callbacks. You will have to modify the 5 methods to take in an array and a callback. Use what you learned in the previous chapter about callbacks to complete the assignment.

One important concept that we want you to learn through this assignment is how to pass data to and from callbacks. You pass data to a callback with a parameter and you pass data from the callback back to the parent function with a return. While you are going through this assignment pay close attention to this relationship.

To understand what each method does, please refer to the underscore library. Note that your method does not have to be as robust as underscore's; you just need to get the base functionality working. Therefore for most methods you will only have the list and a lambda as parameters, and for the lambda you will pass in each element and potentially a "memo" also known as a "collector".

Note that some of these functions already exist in Python. We want you to explore how you might implement these yourself. Be aware that these tools exist to help work in a design idiom known as "functional programming". It's not something that we cover here, but is a topic you may want to explore on your own. It is mainly used in data science in recent years.
'''

'''
Optional Assignment: Modular Store
You'll be breaking your store and product classes from your previous assignment in two separate modules. First, let's look more closely at how modules work using some examples.

Create two documents. Call one parent and one child. Don't worry about child for a moment. We'll work with parent first. Open parent.py and insert the following:

local_val = "magical unicorns"
def square(x):
    return x * x
class User(object):
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
Copy
Now we have a document with a local variable, a function and a Class. If we run this document from the command line we will see no results. We haven't asked to print anything, nor have we called our function or class method. As we know, without print statements it's difficult to know what our code did when it ran. Let's look at our code by running our functions and printing the result.

# add below the user class
print square(5)
user = User("Anna")
print user.name
print user.say_hello()
Copy
Now, we can see in our terminal window whether our code runs as expected. Now let's see what happens when we import parent into child. In child.py:

import parent
Copy
Before writing anything else, run child.py. Check what's in your directory. What changed? When you imported parent, your Python interpreter compiled your code in parent.py into bytecode. This only occurs when a file is not being executed directly from the command line. This is why you may not have seen .pyc files before now. Once a .pyc file is generated, as long as we don't change that file, Python will not have to re-compile your code to bytecode, which may save processing time when working with large code bases.

You probably also noticed that all of your code from parent.py executed on the import statement. This means that every print statement and variable instantiation is still happening. That's fine, but let's use a concept called namespace and a built-in variable called __name__ to clean up our code.

Namespace:
Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. Namespace is important because we have to know what variables we have access to. To see what variables are available in any given place, add the line: print locals() and see what variables are in your current namespace. The object that prints will be a dictionary where the variable names are keys and the objects they reference are the values. Understanding namespace will help you understand the next portion, where we will use namespace to control the functionality that is imported with our document.

Importing modules and namespace:
Whenever we create a new file and execute it, the Python interpreter automatically creates several variables. We’ll look closer at one of them: the variable __name__. To learn how to use this variable in your own code, follow the steps below:

1. __name__ is not only automatically created, but is also assigned a value. In your document parent.py add this line:

  print __name__
  Copy
2. execute parent.py from the command line

3. You should see __main__ printed to the console

4. In child.py you should already have imported parent, if not, add that line now

5. Execute child.py from the command line

6. You should see parent printed to the console.

7. In parent.py add the following:

  if __name__ == "__main__":
    print "the file is being executed directly"
  else:
    print "The file is being executed because it is imported by another file. The file is called: ", __name__
  Copy
8. Now try running the file directly. You should see the file is being executed directly printed in the console.

9. Execute child.py You should see The file is being executed because it is imported by another file. The file is called: parent

10. How is this useful? We can use this conditional to prevent blocks of code from executing unless the file is being run directly. Why would we want to do this? Consider a situation where one class depends on another, as in the store and products assignments. In our product document we might create a lot of test code to make sure we can create new products and execute methods. When we import products to the store file as a module, we don’t want to see all of those tests run every time we execute the store file, so inside of our product document, we might have something like below:

  if __name__ == "__main__":
    product = Product([args])
    print product
    print product.add_tax(0.18)
  Copy
11. The idea here is that we now have the power to control what is visible to the importing document. Follow the steps below to organize your code using namespace.
Rebuild your store:
• Use your code from the previous optional assignment, Store, to start things off. You should have a single document called store.py

• Create two new documents called product.py and manage.py.

• Divide your code. All of the code for your Product class should be moved to the document product.py. Your product and store documents should contain only the code for their respective classes. Create a few instances of product and store in those documents, but wrap them in your conditional check for __name__ == "__main__".

• Import both classes into manage.py. Now you can create objects of both type and those objects can interact in a third environment, or namespace.
'''

'''
Optional Assignment: representing objects
Try printing an object. You'll see something like this: <__main__.User object at 0x1058f5990>. It might be frustrating how little information you'll see. Python has a built-in magic method __repr__ we can invoke for each class. Let's add a __repr__ method to our User class.

# instantiate class User
class User(object):
  # this method to run every time a new object is instantiated
  def __init__(self, name, email):
    # instance attributes from
    self.name = name
    self.email = email
    self.logged = True
  def __repr__(self):
    return "<User object {}, email {}>".format(self.name,self.email)

if __name__ == "__main__":
  user = User("Anna", "anna@anna.com")
  print user
Copy
Hacker Level OOP:
• Change all of your previous OOP assignments so that only the classes are available if the module is imported. Refer back to the optional modular store assignment if you need a refresher.

• Add a __repr__ method to each class. Format your string however you wish.

• Create a new document called manage.py and import all the previous OOP assignments.

• Create new instances of each of the imported classes. Print each instance.
'''
