'''Refer the video below to know more about the Bisection Method '''
# https://youtu.be/dJqmPJeWIQg

'''#Step 1'''
# In this project, you will find the approximate square root of a given number using the bisection method.

# The bisection method is a technique for finding the roots of a real-valued function. It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

# Begin by creating a function named square_root_bisection. Leave the parameters empty for now.

def square_root_bisection():
    pass

    
'''#     Step 2'''
# Give the square_root_bisection function the following parameters:

# square_target: The number for which you want to find the square root.
# tolerance (optional): The acceptable difference between the square of the approximate root value and the actual target value (default is 1e-7). The tolerance 1e-7 implies that the solution will be accurate to within 0.0000001 of the true value and is a good default choice that balances accuracy and performance.
# max_iterations (optional): The maximum number of iterations to perform (default is 100). If the method doesn't converge within this limit, you'll assume the solution is not found.


def square_root_bisection(square_target,tolerance=1e-7,max_iterations=100):
    pass


'''Step 3'''

# If the number for which you want to find the square root is negative, the code should raise an error as the square root of a negative number is not defined in real numbers.

# Remove the pass statement and create an if statement to check if square_target is less than 0.

def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
    if square_target<0:
        pass
    
'''    Step 4'''
# The raise statement allows you to force a specific exception to occur. It consists of the raise keyword followed by the exception type, and enables you to provide a custom error message:

# Example Code
# raise ValueError("Invalid value")
# When the code above runs, a ValueError is raised and the message "Invalid value" is shown to the user.

# If the square_target is less than 0, no real-valued square root can be computed. Therefore, raise a ValueError with the message 'Square root of negative number is not defined in real numbers'. Don't forget to remove the pass keyword.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
'''Step 5
'''

# You'll create separate cases for when square_target is 0 or 1.

# Begin by creating an if statement to check if square_target is equal to 1.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target==1:
        pass
    
'''Step 6'''
# If the square_target is equal to 1, declare a variable root and assign it the value 1 . Also, print the message 'The square root of {square_target} is 1'. Remember to format the message using an f-string.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root=1
        print(f'The square root of {square_target} is 1')
        
        
        
'''# Step 7'''
# Create an elif statement to check if square_target is equal to 0. If it is, assign the value 0 to the root variable. Also, print the message 'The square root of {square_target} is 0'. Remember to format the message using an f-string.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target==0:
        root=0
        print(f'The square root of {square_target} is 0')
        
        
'''# Step 8'''
# Next, you are going to work on the cases where the square_target is a positive number apart from 1 or 0.

# Create an else clause to handle these cases.
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target==0:
        root=0
        print(f'The square root of {square_target} is 0')
    else:
        pass

# Step 9
# In Python, the max() function returns the largest of the input values.

# Example Code
# max(1, 2, 3) # Output: 3
# The variables low and high will be used to define the initial interval where the square root lies.

# Inside the else clause, initialize the low variable to 0 and the high variable to be the maximum of either 1 or square_target as the square root of a number is always less than or equal to the number itself.
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target==0:
        root=0
        print(f'The square root of {square_target} is 0')
        
    else:
        low=0
        high=max(1,square_target)
        
'''# Step 10'''
# Set the value of root to None as at this point, you don't have an approximate value yet.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target==0:
        root=0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1, square_target)
        
        """ Solution """
        
        root = None

'''Step 11'''
# Now you'll repeatedly narrow down the interval by finding the midpoint of the current interval and comparing the square of the midpoint with the target value.

# For that, inside the else block, create a for loop that runs up to max_iterations times.

# For your loop, use the range function, which generates a sequence of numbers you can iterate over. The syntax is range(start, stop, step), where start is the starting integer (inclusive), stop is the last integer (not inclusive), and step is the difference between a number and the previous one in the sequence.

# Also, use _ as a loop variable. The _ acts as a placeholder and is useful when you need to use a variable but don't actually need its value.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        """ Solution """
        
        for _ in range(max_iterations):
            pass  
        
# Step 12
# Inside the for loop, calculate the midpoint of the interval ranging from low to high. Assign this value to a variable mid.

# Also, calculate the square of the midpoint (mid) and store it in the variable square_mid.


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        for _ in range(max_iterations):
            
            """ Solution """
            mid=(low+high)/2
            square_mid=mid**2
            
            
'''Step 13'''
# The abs() function returns the absolute value of a number, which is always positive, regardless of the number sign. You will use it to check that the estimated square root is close enough to the actual value.

# Now, create an if statement to check if the absolute value of the difference between square_mid and square_target is within the specified tolerance.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2   
             
            """ Solution """
            if abs(square_mid - square_target)<tolerance:
                pass    
            
# Step 14
# If the difference is within the specified tolerance, set the value of root to mid and break out of the loop.


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            """Solution"""

            if abs(square_mid - square_target) < tolerance:
                root=mid
                break

# Step 15
# If the difference is not within the specified tolerance, create an elif statement to check if square_mid is less than square_target.

# Assign the value of mid to low as the square root would now lie between low and mid.

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid<square_target:
                low = mid
                
# '''Step 16'''
# If both the if and elif conditions are not met, the value of mid would be greater than square_target. In this case, create an else clause and assign the value of mid to high.

            else:
                high = mid
                
'''Step 17'''
# In Python, the is keyword checks for object identity. It's used to determine if two variables point to the same object in memory. In contrast to is, the equality operator (==) determines if the values of two objects are the same, regardless of whether they are the same object in memory.

# Outside the for loop, create an if statement to check if root is None. If it is, print the message 'Failed to converge within {max_iterations} iterations.'. Remember to format the message using an f-string.


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid
    #SOLUTION
        if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')
            
# Step 18
# Create an else clause to handle the case where the value of root is not None, indicating that a root has been found. If it is not None, print the message 'The square root of {square_target} is approximately {root}'. Remember to format using an f-string.         
            
        else:
            print(f'The square root of {square_target} is approximately {root}')
            
#'''Step 19'''
# Finally, return the value of root from the square_root_bisection function.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    return root

# Step 20
# Outside the function definiton, create a variable N and assign the value of 16 to it.
N=16


# Step 21
# Call the square_root_bisection function with the N variable as the argument. This will print the result to the console.

# Experiment with larger values.

# With this, you have successfully implemented the bisection method to find the square root of a number.
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
        
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    return root

N = 16
square_root_bisection(N)