'''  Understanding Lamda functions   '''

''' And creating an EXPENSE TRACKER '''

# Python Lambda Functions are anonymous functions means that the function is without a name.

# As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

'''
    SYNTAX :
        result_variable_name = lambda arguments:expression 

'''


# This function can have any number of arguments but only one expression, which is evaluated and returned.

# One is free to use lambda functions wherever function objects are required.

# This code defines a lambda function named upper that takes a string as its argument and converts it to uppercase using the upper() method. It then applies this lambda function to the string ‘GeeksforGeeks’ and prints the result

# str1 = 'GeeksforGeeks'

# upper = lambda string: string.upper()
# print(upper(str1))


'''Step 1'''

# In this project, you're going to build a simple, yet functional expense tracker in Python.

# Start by defining a function named add_expense that takes three parameters: expenses, amount and category. Use the pass keyword to fill the function body

def add_expense(expenses,amount,category):
    pass


'''# Step 2'''

# A list in Python is a built-in data type that allows you to store many items in a single data structure. In Python, you create a list by putting items inside square brackets ([]), with each item separated from the following one by a comma.

# Example Code
# numbers = [1, 2, 3, 4]
# Use a pair of square brackets to create an empty list named expenses. You will use it to store each of your expenses.

expenses=[]


'''Step 3'''

# The expenses parameter of your add_expense function will be a list of expenses. You want to be able to add items at the end of your list. For that you'll use the .append() list method:

# Example Code
# my_list = [2, 4, 7]
# my_list.append(3)
# In the example above, after appending 3, my_list would be [2, 4, 7, 3].

# Replace pass with a call to the .append() method on the expenses list. Don't pass any arguments to .append() for now.

def add_expense(expenses, amount, category):
    expenses.append()
    
    
'''Step 4'''

# A dictionary is another built-in data type in Python. A dictionary is a collection of data in the form of key-value pairs. Dictionaries are defined with curly braces ({}) and they contain key-value pairs separated by commas. Each key is followed by a colon (:) and the value:

# Example Code
# {'amount': 50.0, 'category': 'Food'}
# In the example above, 'amount' and 'category' are keys, and 50.0 and 'Food' are their corresponding values.

# Create a dictionary with a key 'amount' and value of the amount parameter and pass your new dictionary to the .append() call.

def add_expense(expenses, amount, category):
    expenses.append({'amount':amount})
    
    
'''Step 5'''
# Add another key-value pair to the dictionary you are appending to the expense list. Use the string 'category' as the key, and the category parameter as the value.
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount,'category':category})


'''
Step 6'''
# Next, define a function named print_expenses that takes one parameter expenses. This function will later be used to display each expense in your list.

# Fill the body of your new function with a pass statement.
def print_expenses(expenses):
    pass

'''Step 7'''
# Inside the print_expenses function, create a for loop that iterates over each item in the expenses list. Use expense as the loop variable and move pass inside the loop body.

def print_expenses(expenses):
    for expense in expenses:
        pass
    
    
    '''Step 8'''
# Next, you are going to display the details for each expense.

# Inside the for loop, replace pass with a print() call and pass it the following f-string: f'Amount: {expense}, Category: {expense}'


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')
        
'''   Step 9 '''
  #In Python, an important thing to know is that the same type of quote used to define a string cannot be used inside it. For example, the string 'I'm a string!' is not valid. To use the single quote inside that string you should either:

# Escape the quote by prepending a backlash to it: 'I\'m a string!'
# Or use double quotes to define the string: "I'm a string!" (preferred).
# You can access values in a dictionary through its keys. You need to use bracket notation and include the key between the square brackets:

# Example Code
# my_dict = {'amount': 50.0, 'category': 'Food'}
# my_dict['amount'] # 50.0
# You are currently interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
        
        
'''# Step 10'''

# You will need a function to calculate the total amount of expenses.

# Define a function named total_expenses that takes one parameter expenses. Fill the function body with a pass statement for now.

def total_expenses(expenses):
    pass


# Step 11
# Lambda functions are brief, anonymous functions in Python, ideal for simple, one-time tasks. They are defined by the lambda keyword, and they use the following syntax:

# Example Code
# lambda x: expr
# In the example above, x represents a parameter to be used in the expression expr, and it acts just like any parameter in a traditional function. expr is the expression that gets evaluated and returned when the lambda function is called.

# Create a variable named test and assign it a lambda function that takes an x parameter and returns x * 2.


test = lambda x:x*2

'''
# Step 12'''
# To call a lambda function you can use the usual function syntax with a pair of parentheses after the variable name.

# Call your test lambda function and pass 3 as the argument. Then, print the result.

print(test(3))
'''
Step 13'''
# Lambda functions can be valuably combined with the map() function, which executes a specified function for each element in a collection of objects, such as a list:

# Example Code
# map(lambda x: x * 2, [1, 2, 3])
# The function to execute is passed as the first argument, and the iterable is passed as the second argument.

# The result of the example above would be [2, 4, 6], where each item in the list passed to map() has been doubled by the action of the lambda function.

# Modify your print() call to print the result of calling map() with test as the first argument, and [2, 3, 5, 8] as the second argument. You won't be able to see a readable output yet.

test =lambda x: x * 2
print(map(test,[2,3,5,8]))

# Step 14
# You should see something like <map object at 0xd273a8> printed on the console, which is the string representation of the map object returned by map().

# To obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the list() function.

print(list(map(test, [2, 3, 5, 8])))

# Step 15
# The sum() function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.

# For now, make a little test and modify your current print() call replacing the list() call with a call to the sum() function passing it the current map() call as the argument.
test = lambda x: x * 2
print(sum(map(test, [2,3,5,8])))

# Step 16
# Next, you are going to implement the same logic within the total_expenses function.

# For now, delete both the test function and the print() call.

'''Step 17'''
# In the total_expenses function, you'll now integrate a lambda function. Replace pass with a lambda function that has expense as its parameter.

# expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.
def total_expenses(expenses):
    lambda expense: expense['amount']

'''Step 18'''
# Now, call map() passing your lambda function as the first argument and the expenses list as the second argument.


def total_expenses(expenses):
    map(lambda expense: expense['amount'],expenses)
    
    
'''Step 19'''
# Finally, pass your map() call to the sum() function to obtain the total expenses and return the result

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Step 20
# Next, define a function named filter_expenses_by_category that takes two parameters: expenses and category. Use pass to fill the function body.

    
def filter_expenses_by_category(expenses,category):
    pass

expenses = []

'''Step 21'''
# Within the filter_expenses_by_category function, replace pass with a lambda function. Use expense as the parameter and evaluate the comparison between the value of the 'category' key of the expense dictionary and category using the equality operator.

def filter_expenses_by_category(expenses, category):
    lambda expense : expense['category'] == category
    
''' Step 22'''
# The filter() function allows you to select items from an iterable, such as a list, based on the output of a function:

# Example Code
# filter(my_function, my_list)
# filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.

# The result of the example above is an iterator containing the elements of my_list for which my_function returns True.

# Within the filter_expenses_by_category function, call filter() passing the lambda function you wrote in the previous step as the first argument and the expenses list as the second argument.

def filter_expenses_by_category(expenses, category):
    filter(lambda expense: expense['category'] == category,expenses)
    
''' Step 23 '''
# Finally, return the result of the filter() call.
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

'''# Step 24'''
# The next step is to define the main function, which will be the entry point of the interactive expense tracker program.

# Define a function named main without parameters. Fill the function body with the expenses list you created at the beginning of this project. You will use this list to store the expense records.

def main():
    expenses = []
    
'''Step 25'''  
# A while loop is another kind of loop that runs a portion of code as long as a specified condition is True. The loop terminates when the condition becomes False:

# Example Code
# while condition:
#     <code>
# Below the expenses list, create a while loop. Use True for the condition, and print the string '\nExpense Tracker' inside the loop body to show the title of the program.

def main():
    expenses = []
    while(True):
        print('\nExpense Tracker')
    
'''    
Step 26'''
# The while loop you created in the previous step is an infinite loop that will allow the program to continuously present menu options until the user decides to exit.

# After the print() call, add another print() call to print the string '1. Add an expense'.
def main():
    expenses = []

    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        
        
'''Step 27'''
# Next, add another print() call and pass the string '2. List all expenses'.
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        
# Step 28
# Provide the other menu options by printing the following three strings in your while loop: '3. Show total expenses', '4. Filter expenses by category', and '5. Exit'. Keep adding the print() calls in order.
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
'''Step 29'''
# The input() function takes a user input and it returns the user input in the form of a string.

# Inside your while loop, call the input() function passing the string 'Enter your choice: ' as the argument, and assign the result to a variable named choice.

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input("Enter your choice: ")
        
'''Step 30'''
# You are going to use conditional statements to check the user's choice. If the choice is '1', it means the user wants to add an expense.

# Still in the while loop, under the choice variable, write an if statement to check if choice equals the string '1'. If it's true, it will be the starting point for adding a new expense.

# Inside the if statement body, declare a variable amount and assign it an empty input() call.

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice=='1':
            amount=input()
            
            
            
'''Step 31'''
# Inside the if statement, you should ask the user to enter the amount for the expense and store it in a variable.

# Pass the string 'Enter amount: ' to your empty input() call, so you can store the expense.

#same indent as above replace the amount with this statement
amount = input('Enter amount: ')


# Step 32
# The amount of the expense needs to be converted before performing any calculation. The float() function takes a string or an integer number as argument and returns a floating point number.

# Pass input('Enter amount: ') to the float() function.

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            amount = float(input('Enter amount: '))
            
            
# Step 33
# Inside your if statement, create a variable named category to store the expense category. Assign it a call to input() and use the 'Enter category: ' as the argument.

#same indent as above under amount ...
category = input('Enter category: ')


# Step 34
# Once you have the expense details, you need to call the add_expense function to add the new expense to the expenses list.

# After getting the amount and category using input(), call the add_expense function, passing three arguments: expenses, amount and category.

# expenses is the empty list created in the main function earlier in this project.
# amount is the amount of the expense.
# category is the category of the expense.

#same indent as above under amount and category...
add_expense(expenses,amount,category)

# Step 35
# To list all expenses, you can use an elif clause after an if statement. The elif checks additional conditions and only works following an if statement.

# Create an elif clause to check if the user's choice equals the string '2'. Inside the elif clause, print the string '\nAll Expenses:'.

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice=='2':
            print('\nAll Expenses:')
            
            
#             Step 36
# After the print() call, call the print_expenses function to display all the expenses that have been added so far. Pass the expenses list as the argument.


        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
            
            
# Step 37
# To show the total expenses, create an elif statement that checks if choice == '3'.

# If it's true, it means the user wants to see the total expenses. So call print() and pass the string '\nTotal Expenses: ' as the first argument and total_expenses(expenses) as the second argument.
        elif choice == '3':
            print('\nTotal Expenses: ',total_expenses(expenses))
            
            
# Step 38
# Create another elif clause that checks if choice == '4'. Inside the new elif, create a variable category and assign it input('Enter category to filter: ') to filter the expense category.
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            
# Step 41
# Still within the elif clause, pass the expenses_from_category iterator to a print_expenses call.
            print_expenses(expenses_from_category)
            
            
# Step 42
# To provide a way to exit the program, use another elif clause to check if choice equals the string '5'.

# Inside the new elif clause, print the string 'Exiting the program.' to show that the program is terminating its execution.
        elif choice=='5':
            print('Exiting the program.')
            
# Step 43
# Finally, to stop the execution of the while loop, add the break statement inside your last elif clause.

        elif choice == '5':
            print('Exiting the program.')
            break
        
        
# Step 44
# Finally, call your main() function, and try the expense tracker program in the console.

# With that, the expense tracker project is complete!

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()
