from datetime import datetime as dt

greetIntent=["hi","hello","hey","hii","heya","hi!"]
dateIntent=["date","day","what's the date","what is the date"]
timeIntent=["time","current time","what's the time","what is the time"]



chat=True
while chat:
    message=input("Enter your message :")
    message=message.lower()

    if message in greetIntent:
        print("Hello User!")
    elif message in dateIntent:
        date=dt.now().date()
        cur_date=date.strftime("%A %d %B, %Y")
        print("Today's Date: ", cur_date)
    elif message in timeIntent:
        time=dt.now().time()
        cur_time=time.strftime("%H:%M:%S %p")
        print("Today's Time: ",cur_time)
    elif message=='bye':
        print("Bye !")
        break
    else:
        print("I don't understand!")



