import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter8=chr(random.randint(165,290)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter7=chr(random.randint(165,290)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter8 + uppercaseLetter8 # + ....
password = shuffle(password)

#Ouput
print(password)