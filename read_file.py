#!/usr/bin/python

class ReadFile:
  def __init__(self, file_name):
    self.file_name = file_name
    self.file = open(file_name)
    self.file_lines = self.file.read().split('\n')
    self.keep_reading = True
    self.ans = self.file_lines.pop(0)
    self.rl = 0
  def playFile(practice_number, ask, add_line, no_line):
    while(self.keep_reading):
      reply = ask()
      
      if(reply == self.ans):
        print "You guessed it!"
      

# f = open('/home/mwarner/Documents/sandbox/mathascii/pics/pic1.txt')

# r = f.read()

# lines = r.split('\n')

# keep_reading = True

# ans = lines.pop(0)

# rl = 0

# while(keep_reading):
#   ade = raw_input("1 mean add a line 0 means don't\n>")
#   if(ade == '1'):
#     rl += 1
#     for i in range(0, rl):
#       print lines[i]
#   if(rl >= len(lines)):
#     print "end the loop"
#     keep_reading = False 
#   if(ade == 'x'):
#     print "exit this biz"
#     keep_reading = False
# 
# print "You did it! Fini!"
