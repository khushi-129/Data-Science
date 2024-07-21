#chat application
'''Data Collection:
-Sources
Internet-> open source website/scraping/API calls
API Calls- Weather, '''

chat=True
while chat:
    message=input("Enter your message :")
    #print("Welcome :",message)
    message=message.lower()
    if message=="hi" or message=="hello" or message=="hey":
        print("Hello User")
    
    elif message=="bye":
        print("Bye User...")
        break
    else:
        print("I dont understand")
