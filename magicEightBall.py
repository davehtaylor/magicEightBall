# Magic Eight Ball
# 
# This is a Magic Eight Ball program, written in Python. A user is given a prompt to ask a question of the Magic Eight Ball, 
# and then to press a key to shake the ball and receive an answer. Just as with its real-life counterpart, there are 20 possible 
# answers, some negative, some positive, some neutral. This program will choose one of the answers from the list at random and 
# return that answer to the user. 

import random                                   # Import random so we can randomly choose a response from the responses[] list.
import time                                     # Import time so we can use the sleep() function to add a dramatic pause to the response.

responses = ["It is certain",                   # List of the responses presented to the user. 
             "It is decidedly so",
             "Without a doubt",
             "Yes definitely",
             "You may rely on it",
             "As I see it, yes",
             "Most likely",
             "Outlook good",
             "Yes",
             "Signs point to yes",
             "Reply hazy try again",
             "Ask again later",
             "Better not tell you now",
             "Cannot predict now",
             "Concentrate and ask again",
             "Don't count on it",
             "My reply is no",
             "My sources say no",
             "Outlook not so good",
             "Very doubtful"]

print "\n"
print "**************************************"          # Pretty banner when the program runs
print "*          Magic Eight Ball          *"
print "**************************************"

print "\n"

print "Ask a question of the Magic Eight Ball"
print "then hit the 'Enter' key to shake the"
print "ball and receive your answer.\n"

selection = raw_input()                         # Wait for the user to hit "Enter" before presenting the answer. 

print "Contemplating "                          # Give some pause to appear to be thinking about the answer. 
time.sleep(0.5)                                 # Wait half a second between printing each of the periods
print "." 
time.sleep(0.5)
print "." 
time.sleep(0.5)
print ".\n"

print "*** " + (random.choice(responses)) + " ***"                # Choose a random response from the responses[] list and print it out.
print "\n"
