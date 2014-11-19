# Magic Eight Ball
#
# This is a Magic Eight Ball program, written in Python and licensed
# under the GPLv3. See LICENSE.txt for more information.
#
# A user is given a prompt to ask a question of the Magic Eight Ball,
# and then to press a key to shake the ball and receive an answer.
# Just as with its real-life counterpart, there are 20 possible
# answers, some negative, some positive, some neutral. This program
# will choose one of the answers from the list at random and
# return that answer to the user.


# Import random so we can use the random.choice() function to choose
# a response from the responses[] list.
#
# Import time so we can use the time.sleep() function to add a dramatic
# pause to the response.

import random
import time


def thinking():
    """Give some pause to appear to be thinking about the answer."""

    print "\nContemplating "
    for iteration in xrange(3):
        time.sleep(1)
        print "."

responses = ["It is certain",
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
print "**************************************"
print "*          Magic Eight Ball          *"
print "**************************************"
print "\n"

print "Ask a question of the Magic Eight Ball"
print "then hit the 'Enter' key to shake the"
print "ball and receive your answer.\n"

raw_input("Type your question then hit enter:\n\n")

thinking()

print "\n*** " + (random.choice(responses)) + " ***\n"
