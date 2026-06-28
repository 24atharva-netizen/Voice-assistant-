import pyttsx3
import datetime

engine = pyttsx3.init()

while True:
    command = input("Enter command: ").lower()

    if command == "hello":
        print("Hello Atharva")
        engine.say("Hello Atharva")
        engine.runAndWait()

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%H:%M")
        print("Current Time:", current_time)
        engine.say("Current Time is")
        engine.say(current_time)
        engine.runAndWait()

    elif command == "exit":
        print("Goodbye")
        engine.say("Goodbye")
        engine.runAndWait()
        break

    else:
        print("Command not found")
        engine.say("Command not found")
        engine.runAndWait()