response = raw_input("What is your question? ")
if response[-1] is not "?":
    print("I'm sorry, I can only answer questions.")

while response != "quit":
    response = raw_input("Ask another question: ")
