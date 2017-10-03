#!/usr/bin/python

import math
import random
import subprocess

#### Variables ####

practice_number = 'a'
p_num_isnan = True
keep_going = False
ascii_art_fil = ''
right = 0
lines = 0

#### Functions ####

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def get_input(message, num):
  res = raw_input("{0}\n>".format(message))

  if(num and is_number(res)):
    return int(res)
  else:
    print "Step 4"
    return res

def math_question(b, c):
  num1 = random.randint(0, b)
  if(c == False):
    num2 = random.randint(0, b)
  else:
    num2 = practice_number
  ans = num1 + num2
  return {'num1': num1, 'num2': num2, 'ans': ans}

def get_ascii_art_file():
  return open('./pics/pic1.txt')

#### Run Code ####

while(p_num_isnan):
  practice_number = get_input("Is there a number you want to practice?\nEnter a number or all for all numbers.", True)
  if(is_number(practice_number)):
    p_num_isnan = False
  elif(practice_number == 'all'):
    p_num_isnan = False

print "Thanks. You will practice {practice_number}.".format(**locals())

# gets the file, saves are array of lines, and gets answer
ascii_art_file = get_ascii_art_file()
file_arr = ascii_art_file.read().split('\n')
ans = file_arr.pop(0)

while(True):
  rezzie = math_question(10, True)
  # Enter clear screen here
  input_ans = get_input("{rezzie[num1]} + {rezzie[num2]} = x".format(**locals()), True)
  if(input_ans == rezzie['ans']):
    print "You got it right! Good work!"
    right += 1
    # Enter clear screen here
    subprocess.call(['clear'])
    print '\n'.join(file_arr[0:right])
  else:
    print "Ummmm... keep trying :)"


print "you are done"

# Next grab a text file of ascii art
# Then find out how many lines there are
# For every question asked correctly, one more line gets deplayed
# # something like: clear -> display art -> ask new question
# some features:
# # get out of the rest of the questions by guessing the picture
# # adding, subtracting, multiplying, dividing
# # range of numbers (1-5, 7-9 etc)
