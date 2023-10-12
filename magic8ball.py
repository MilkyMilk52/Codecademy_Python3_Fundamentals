name = input("what is your name? ") #Leave blank if you don't want to put your name
question = input("What is your question? ")
answer = ""

import random

random_number = random.randint(1,9)
print(random_number)

if random_number == 1:
  answer = "Yes - Definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error, seems like you asked too hard of a question! (Number value outside of range - Buggy bois)"

if len(question) == 0:
  question = "Error - Missing question!"
  answer = "Please provide a question!"
else:
  question = question

if len(name) == 0:
  print("Question:", question)
else:
  print(name, "asks:", question)

print("Magic 8-Ball's answer:", answer)