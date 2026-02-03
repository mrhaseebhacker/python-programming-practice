def happy_birthday(name,age):

    print(f"Happy Birthday to : {name}")
    print(f"You are : {age} years old") 

happy_birthday("Haseeb", 20)
happy_birthday("Ahmad",19)
def display_invoice(username, amount, due_date):

    print(f"Your name is : {username}")
    print(f"Your amount is : {amount}")
    print(f"Due date is : {due_date}")

display_invoice("Haseeb", 4000, 25)

def create_name(first_name, last_name):

    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("haseeb", "tariq")
print(full_name)
print((lambda x,y: x+y)(1,2))



def calc_sum(a,b):
    sum = a+b
    print(sum)
calc_sum(12,13)

calc_sum(30,33)

calc_sum(40,30)

def ave(a,b):
    ave = (a+b)/2
    print(ave)

ave(20,30)

nums = [1,2,3,4,4]

def print_len(nums):
    print(len(nums))

print_len(nums) 

heroes = ["ironman", "batman", "superman"]

def print_list(list):
    for item in list:
        print(item , end=" ")
print_list(heroes) 
print()       
    
    

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(fact)
calc_fact(6)


def converter(USD):
    PKR = USD * 275
    print(USD ,"USD" " = ", PKR, "PKR")
converter(100)   


def even_odd():
    num = int(input("Enter a number:"))
    if num% 2 ==0:
        print("Even")
    else:
        print("Odd")

even_odd()
even_odd()
