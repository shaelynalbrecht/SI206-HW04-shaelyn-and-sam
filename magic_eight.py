response = raw_input("What is your question? ")
if response[-1] is not "?":
    print("I'm sorry, I can only answer questions.")

while response != "quit":
    response = raw_input("Ask another question: ")

import random

answers_list = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
"As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
"Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
"My sources say no", "Outlook not so good", "Very doubtful"]

answers_list[random.randrange(0,19)]
