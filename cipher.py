# DO NOT TRY RUNNING ENTIRE FILE AS IT CONTAINS SNIPPETS OF EACH EXERCISE.

'''Step 50 '''
# In Python, the scope of a variable determines where that variable can be accessed:

# Variables defined outside a function have a global scope and they can be accessed from any part of your code.

# Variables defined inside a function are local to that function and cannot be accessed outside of it.

# To see this in action, try to print the alphabet variable at the end of your code. This will raise a NameError exception.

# You should see an error message indicating that alphabet is not defined. This is because alphabet is defined inside the caesar function and is not accessible outside of it.

text = 'Hello Zaira'
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)
    
''' Step 52 '''
# To execute, a function needs to be called (or invoked) by appending a pair of parentheses after its name, like this:

# Example Code
# function_name()
# At the end of your code, call your caesar function. Pay attention to the indentation.

caesar()

'''Step 53'''

# Now you should see the output again. Although this approach works, it doesn't significantly enhance the code's reusability. Repeatedly calling your function will result in the same outcome. However, functions can be declared with parameters to introduce versatility and customization:

# Example Code
# def function_name(param_1, param_2):
#     <code>
# Parameters are variables that you can use inside your function. A function can be declared with different number of parameters. In the example above, param_1 and param_2 are parameters.

# Modify your function declaration so that it takes two parameters called message and offset.

# After that, you'll see an error appear in the terminal. You'll see how to solve it in the next steps.


def caesar(message,offset):
    pass

''' Step 54 '''
# Inside your function body, rename the text and shift variables to message and offset, respectively.


def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar()

''' Step  '''
# Currently, your code raises a TypeError, because the caesar function is defined with two parameters (message and offset), therefore it expects to be called with two arguments.

# Calling caesar() without the required arguments stops the execution of the code.

# Give message and offset values, by passing text and shift as arguments to the caesar function call.

caesar(text,shift)

''' Step 56 '''
# At the bottom of your code, after your existing caesar(text, shift) call, call your function again.

# This time, pass the text variable and the integer 13 as arguments.

text = 'Hello Zaira'
shift = 13

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 13)

''' Step 57'''
# Currently, every single letter is always encrypted with the same letter, depending on the specified offset. What if the offset were different for each letter? That would be much more difficult to decrypt. This algorithm is referred to as the Vigenère cipher, where the offset for each letter is determined by another text, called the key.

# Start transforming your Caesar cipher into a Vigenère cipher by removing the two function calls.

#Vigenère cipher, where the offset for each letter is determined by another text, called the key.

text = 'Hello Zaira'
shift = 13

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    
'''  Step 58 '''
# Now modify your function declaration: change the function name into vigenere and the second parameter into key.  
 
text = 'Hello Zaira'
shift = 3

def vigenere(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
    
    
''' Step 59 '''
# Delete your shift variable. Then, declare a new variable called custom_key and assign the value of the string 'python' to this variable.

custom_key = 'python'

''' Step 60 '''
# Since your key is shorter than the text that you will have to encrypt, you will need to repeat it to generate the whole encrypted text. At the beginning of your function body, declare a key_index variable and set it to zero.

def vigenere(message, key):
    key_index = 0

''' Step 61 '''

# When coding, readability is key. Comments serve as effective notes, explaining the logic behind your code. They prove valuable when returning to a project after some time and also aid your colleagues in understanding the code.

# In Python, you can write a comment using a #. Anything that comes after the # won't be executed.

# Before your if statement, add a comment saying Append space to the message.    
    
#Append space to the message.


   # Append space to the message


''' Step 62 ''' 

# Next, inside the else block, declare a variable called key_char and assign it the value of key at the index key_index mod(%) the length of key.



key_char = key[key_index%len(key)]
  


''' Step 63'''
# You will need to increase the key_index count for the next iteration. To do this, after the line you just added and in the same code block, use the addition assignment operator to increment key_index by one


key_index += 1
    
    
    
'''Step 64'''
# Inside the else clause, write a comment saying Find the right key character to encode.

            #Find the right key character to encode.
         

   
'''Step 65'''
# The .index() method is identical to the .find() method but it throws a ValueError exception if it is unable to find the substring.

# A ValueError is a built-in exception that is raised when an argument with the right type but inappropriate value is passed to a function.

# After incrementing key_index, declare a variable named offset. Find the index that key_char has in alphabet and assign it to offset. Use the .index() to find the index.
offset = alphabet.index(key_char)


'''Step 66'''
# Above the offset variable, create another comment saying Define the offset and the encrypted letter.
#Define the offset and the encrypted letter.


'''Step 67'''
# At the moment, your function prints some strings, but these values cannot be used by other parts of code to perform any actions.

# For that purpose, you need to use a return statement:

# Example Code
# def foo():
#     return 'spam'
# You need to write return followed by a space and the value that the function should return. Once the return statement is found, that value is returned and the execution of the function stops, proceeding to the next line of code after the function call. In the example above, the foo function returns the string 'spam'.

# Remove the two print() calls from your function and return encrypted_text.
def vigenere():
    # i skipped the code
   return encrypted_text

''' Step 68'''
# Call your function passing text and custom_key as the arguments. Store the return value of the function call in a variable called encryption.

encryption = vigenere(text,custom_key)
print(encryption)

''' Step 69 '''
# And now, try to print encryption to see the actual output on the terminal.

'''Step 70'''
# Encryption and decryption are opposite processes and your function can do both with a couple of tweaks.

# Add a third parameter called direction to your function definition. Also, comment out the last two lines of code to avoid errors in the console.

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key ,direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text
    
# encryption = vigenere(text, custom_key)
# print(encryption)

'''Step 71'''
# All you need to do is multiply the offset by the direction in the new_index assignment. The multiplication operator in Python is *.
new_index = (index + offset * direction) % len(alphabet)

'''Step 72'''
# Now you can uncomment the last two lines and modify your function call passing 1 as the third argument.
encryption = vigenere(text, custom_key,1)

'''Step 74'''
# Now print your decryption variable.
decryption = vigenere(encryption, custom_key, -1)
print(decryption)


'''step 75'''
# Now, your function can be used both to encrypt and decrypt a message. Clean up your code with better variable names.

# Change each occurrence of encrypted_text into final_message.

text = 'Hello Zaira'
custom_key = 'python'
def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
    
        # Append space to the message
        if char == ' ':
            final_message += char
        else:        
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)


'''Step 77'''
# Functions can be called with default arguments. A default argument indicates the value that the function should take if the argument is not passed. For example, the function below accepts three arguments but you can call it passing two arguments. The third one will assume the specified value by default:

# Example Code
# def foo(a, b, c=value):
#     <code>
# Modify the vigenere function so that its direction parameter has a default value of 1.

def vigenere(message, key, direction=1):
    pass


'''Step 78'''
#Now you can remove the third argument from your first function call.

encryption = vigenere(text, custom_key)


'''Step 79'''
# Right now, punctuation, special characters or digits are not encoded/decoded correctly.

# Check this by adding an exclamation mark at the end of the text string.

text = 'Hello Zaira!'

'''Step 80'''
# The .isalpha() method returns True if all of the characters of the string on which it is called are letters. For example, the code below returns True:

# Example Code
# 'freeCodeCamp'.isalpha()
# # True
# Delete the condition char == ' ' and replace it by calling the .isalpha() method on char.
if char.isalpha():
    final_message += char
            
            
'''  Step 81'''
# The not operator is used to negate an expression. When placed before a truthy value — a value that evaluates to True — it returns False and vice versa.

# Add the not operator at the beginning of the if condition to check if the character is not alphabetic.
 # Append space to the message
if not char.isalpha():
    final_message += char
    
'''step 83'''   
# Calling vigenere with 1 to encrypt and -1 to decrypt is fine but it might be a little bit cryptic. Create a new function called encrypt that takes message and key parameters, and use pass to fill the function body.
    
def encrypt(message,key):
    pass
    
'''Step 84'''
# Delete the pass keyword, and return vigenere(message, key) from your new function   
def encrypt(message, key):
    return vigenere(message, key)
'''Step 86'''
# Next, modify your encryption and decryption variables by calling encrypt and decrypt, respectively, in place of vigenere.
def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)
    
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)

'''Step 87'''
# It works! Now, you are going to start with an encrypted message to be decrypted.

# Change the value of text to the string 'mrttaqrhknsw ih puggrur'.

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

#Step 88
# Since this time you are starting from an encrypted string to decrypt, you won't need the encryption variable anymore.

# Delete encryption and the print(encryption) call. Also, comment out the last two lines of your code.


'''Step 89'''
# Two or more strings can be concatenated by using the + operator. For example: 'Hello' + ' there!' results in 'Hello there!'.

# Call the print() function and use the + operator to concatenate the text variable to the string 'Encrypted text: '. Pay attention to the spacing.
print('Encrypted text: '+text)


'''Step 90'''
# Below the print() call you just added, add another print() call to print Key: python by concatenating the string 'Key: ' and the value of the custom_key variable.
print('Key: '+custom_key)

'''Step 91'''
# In Python, there's a way to easily format strings. f-strings enable you to interpolate values in your strings.

# Interpolation means writing placeholders that will be replaced by the specified values when the program runs. For example, you can get the same result of 'Encrypted text: ' + text with f'Encrypted text: {text}'. You need to put an f before the quotes to create the f-string and write the variables or expressions you want to interpolate between curly braces.

# Modify the first print() call to use an f-string.

print(f'Encrypted text: {text}')


'''Step 92'''
# Next, modify print('Key: ' + custom_key) to use an f-string.
print(f'Key: {custom_key}')

'''
Step 93'''
# The newline character \n is a special sequence used to represent a new line. You can write a backslash \ followed by an n as a normal sequence of characters in a string and it will be replaced by a new line in the output when the program runs.

# Put a newline character at the beginning of your first print call and see the output.
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')


'''Step 94'''
# Uncomment the decryption variable and change its value by passing text as the first argument to decrypt.
decryption = decrypt(text, custom_key)

'''
Step 95'''
# Uncomment your last print() call and change it to use the f-string f'\nDecrypted text: {decryption}\n' as the argument.
print(f'\nDecrypted text: {decryption}\n')

# Step 96
# Wait a minute! You cannot decrypt anything with the wrong key. Try with 'happycoding'.



text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# With that, your cipher project is complete.




text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
