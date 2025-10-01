# FILE NAME - coin_toss.py
# NAME: Nicholas Sheppard
# DATE: 09/30/2025
# BRIEF DESCRIPTION:  A program that uses a random number from 1-100 to determine if
# coin flip is Heads or Tails.

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########

import random

def main():
    coin_toss()

def coin_toss():
    number = random.randint(1, 100)
    print("===== Coin Flipper =====")
    #print(number)
    if number >= 51:
        print("Tails")
    else:
        print("Heads")

main()

########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

The lab itself was fairly easy. The hard part was that I did't know what the random number is. To test the code
I printed the variable to verify that the results were what I expected.

'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[x] I'm solid. Totally got it.
'''
