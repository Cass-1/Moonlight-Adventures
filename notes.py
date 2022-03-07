#Roslyn Sue Djang
#Isaac Dahle
#Python Notes for us :))

# dictionary =  A changeable, unordered collectoin of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly




decisions = {'choiceA' : "You wake up", 'choiceB': "You go back to sleep"}

decisions.update({'Choice': "Hey you!"})    # One way to change dict
decisions.pop('choiceA')    #removes this key:value pair
decisions.clear()   #will clear the dict

#safe way to print key:values using the get method. If there is no key, the program will print "None"
print(decisions.get('choiceC'))


#not as safe as the get method. Could probably validate inputs when asking for user-prompts? (and could use this)
#print(decisions['choiceC'])

# methods:  .keys() --> prints the keys;  .values() --> prints the values;   .items() --> prints the dict.


#can use a for loop to print items in a dict
for key, value in decisions.items():
    print(key, value)



#   *args =  parametger that will pack all arguments into a tuple
#*           useful so that a function can accept a varying amount of arguments.

def add(*args):     #*  the name args doesn't matter, could be stuff; what's important is the aestrick(*).
    sum = 0
    args = list(args)   #*  a tuple cannot be changed so we cast it as a list.
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))



#   **kwargs =  parameter that will pacl all arguments into a dictionary
#*              useful so that a function can accept a varying amount of keyword arguments
#*              (similar to *args)

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Ms.", first="Roslyn", middle="Grace", last="Djang")