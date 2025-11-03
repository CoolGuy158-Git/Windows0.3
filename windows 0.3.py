import time
import random
import os
import secrets
ram_usage = False
print(r" /$$      /$$ /$$                 /$$                                  ")
print(r"| $$  /$ | $$|__/                | $$                                  ")
print(r"| $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$  /$$  /$$  /$$  /$$$$$$$")
print(r"| $$/$$ $$ $$| $$| $$__  $$ /$$__  $$ /$$__  $$| $$ | $$ | $$ /$$_____/")
print(r"| $$$$_  $$$$| $$| $$  \\ $$| $$  | $$| $$  \\ $$| $$ | $$ | $$|  $$$$$$ ")
print(r"| $$$/ \\  $$$| $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$ \\____  $$")
print(r"| $$/   \\  $$| $$| $$  | $$|  $$$$$$$|  $$$$$$/|  $$$$$/$$$$/ /$$$$$$$/")
print(r"|__/     \\__/|__/|__/  |__/ \\_______/ \\______/  \\_____/\___/ |_______/ ")
print(r"                                                                       ")
print(r"                                                                       ")
print(r"                                                                       ")
print(r"  /$$$$$$        /$$$$$$                                                 ")
print(r" /$$$_  $$      /$$__  $$                                                ")
print(r"| $$$$\\ $$     |__/  \\ $$                                                ")
print(r"| $$ $$ $$        /$$$$$/                                                ")
print(r"| $$\\ $$$$       |___  $$                                                ")
print(r"| $$ \\ $$$      /$$  \\ $$                                                ")
print(r"|  $$$$$$/ /$$\ |  $$$$$$/                                                ")
print(r" \\______/ |__/  \\______/                                                 ")


print(" ")

print("Please type boot to give User Confirmation")

user_confirmation = input(">>> ").strip().lower()

if user_confirmation in ["boot"]:
    print("PC is booting...")
    time.sleep(3)

    print("run on Ram or Storage? y for storage, n for Ram")

    user_preference = input(">>> ").strip().lower()

    if user_preference in ["y"]:
        print("Booting in storage...")
        time.sleep(2)
        print("Welcome to windows 0.3 test edition, no GUI yet type Help to get a list of commands")
    elif user_preference in ["n"]:
        ram_usage = True
        print("Booting in Ram...")
        time.sleep(2)
        print("running in Ram, RAM USAGE WILL INCREASE BY 100%")
    else:
        print("NOTHING SELECTED, PC going to sleep")
        exit()

else:
    print("ERROR_User_Confirmation.exe = False, PC going to sleep")
    exit()

repetitions = 0
for _ in range(100):
    Command = input("$ ").strip().lower()
    if ram_usage == False:
        repetitions += 1
    elif ram_usage == True:
        repetitions += 2
    BSOD = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if random.randint(1, 1000) == 1:  # 1 in 1000 chance
        print("WINDOWS 0.3 has encountered a critical error")
        print("RESTART THE SYSTEM")
        break
    else:

        if repetitions == 100:
            print("WARNING!!! You used up all your RAM, shutting off the PC...")
            break
        if repetitions == 90:
            print("WARNING!!! YOU USED UP 90% OF YOUR RAM, please refresh the PC, or else it will automatically shut off")

        if Command in ["help"]:
            print("run- Runs floppy")
            print("msinfo32- Shows hardware info")
            print("winver- Shows Software Info")
            print("flip a coin- Flips A Coin")
            print("shut off- Shuts off PC")
            print("save- Saves this session on the HDD")
            print("lan- connects to a LAN network")
            print("clock.exe- Shows Time")
            print("refresh- Clears The Screen")
            print("print- The computer repeats what you say")
            print("calculatora.exe- Allows you to add")
            print("calculators.exe- Allows you to subtract")
            print("calculatorm.exe- Allows you to multiply")
            print("calculatord.exe- Allows you to divide")
            print("updates- Checks for updates")
            print("game.exe- Allows you to play a number game")
            print("age calculator.exe- Calculates your age")
            print("product name generator.exe- Makes a product name")
            print("winfetch- msinfo32 but downloaded from a third party site on your pc named https://www.winfetch.com using a usb stick because your pc cant open https")
            print("ekdmp- runs an early keyword detection model priority AI, MAY TAKE UP LOTS OF RAM!")
            print("ram usage- shows RAM usage")
        elif Command in ["run"]:
            print("ERROR! no floppy disk found, please insert a floppy disk")
        elif Command in ["ram usage"]:
            print("ram usage: ", repetitions)
        elif Command in ["msinfo32"]:
            print("1.5 mb of HDD, 0.1 b of RAM, Manchester Baby ")
        elif Command in ["winver"]:
            print("Windows 0.3 no GUI edition 2h2t update 0.0.0 Storage taken up- 1.3mb of storage All rights reserved Microsoft Corporation 1967")
        elif Command in ["flip a coin"]:
            print("flipping coin...")
            time.sleep(1)
            print(random.choice(['heads', 'tails']))
        elif Command in ["lan"]:
            print("Welcome to the internet, unfortunately only 3 url's are available...")
            print("type exit to exit")
            print("WARNING! url's are case sensitive")
            print("available url's are www.how-to-drink-water.com, www.windows-0.3, www.this-is-a-http-url.com")
            while True:
                url = input("www. ")
                print("www.",url, ".com")
                if url == "how-to-drink-water":
                    print("|-----------|")
                    print("| Step 1    |")
                    print("|Drink water|")
                    print("|THE END!   |")
                    print("|-----------|")
                elif url == "windows-0.3":
                    print("|--------------|")
                    print("| 0.3 help     |")
                    print("|in a modern pc|")
                    print("|go to         |")
                    print("www.windows.com|")
                    print("|--------------|")
                elif url == "this-is-a-http-url":
                    print("|--------|")
                    print("|this url|")
                    print("|can be o|")
                    print("|pened by|")
                    print("|a potato|")
                    print("|--------|")
                elif url == "exit":
                    print("exiting...")
                    break
                else:
                    print("|---------|")
                    print("|error 404|")
                    print("|---------|")
        elif Command in ["save"]:
            print("ERROR! You have no HDD space")
        elif Command in ["clock.exe"]:
                    current_time = time.ctime()
                    print("|--------------------------|")
                    print("| Clock.exeV2.0            |")
                    print(f"| {current_time} |")
                    print("|                          |")
                    print(r"|Enter {exit} to exit.    |")
                    print("|--------------------------|")
        elif Command in ["refresh"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            repetitions = 0
            print("Welcome back To Windows 0.3! Type Help For A List Of Commands")
        elif Command in ["print"]:
            Repeat = input("<")
            if len(Repeat) > 50:
                print("length too long RAM is being overused, please reduce the text")
            else:
                print("=" + Repeat)
        elif Command in ["calculatora.exe"]:
            First_Digit = float(input("x: "))
            Second_Digit = float(input("y: "))
            print("answer =", First_Digit + Second_Digit)
        elif Command in ["calculators.exe"]:
            First_Digit = float(input("x: "))
            Second_Digit = float(input("y: "))
            print("answer =", First_Digit - Second_Digit)
        elif Command in ["calculatorm.exe"]:
            First_Digit = float(input("x: "))
            Second_Digit = float(input("y: "))
            print("answer =", First_Digit * Second_Digit)
        elif Command in ["calculatord.exe"]:
            First_Digit = float(input("x: "))
            Second_Digit = float(input("y: "))
            if Second_Digit == 0:
                print("ERROR, Could not calculate")
            else:
                print("answer =", First_Digit / Second_Digit)
        elif Command in ["updates"]:
            print("No new updates found, update 1.2.2")
        elif Command in ["game.exe"]:
            print("Write a num from 1-5 write esc/exit to exit")
            while True:
                repetitions += 1
                num = random.randint(1, 5)
                guess = input(">>> ")
                if guess.lower() in ["esc", "exit"]:
                    print("Going back to windows 0.3...")
                    break
                elif guess.isdigit():
                    if int(guess) == num:
                        print("Correct!")
                    else:
                        print("Incorrect! Correct number was", num)
                else:
                    print("Please enter a number between 1 and 5")
        elif Command in ["age calculator.exe"]:
            print("Forgot your age? Type your name and birth year to find out! WARNING, it might have a less or more than 1 year error so WATCH OUT!!!")
            name = input("Name> ")
            birth = input("Birth> ")
            birth_num = int(birth)
            age = time.localtime().tm_year - birth_num
            age_num = int(age)
            if name.isdigit():
                print("invalid name, SYNTAX ERROR")
            elif age_num > 120:
                print("invalid age, SYNTAX ERROR")
            elif age_num < 1:
                print("invalid age, SYNTAX ERROR")
            else:
                print(name, " you are ", age_num)
        elif Command in ["product name generator.exe"]:
            print("GOT A COOL A PRODUCT IDEA BUT NO NAME??? JUST: ")
            brand = input("brand name> ")
            product = input("product type> ")
            product_name = f"{brand} {product}".title()
            print(product_name)
        elif Command in ["shut off"]:
            print("It is now safe to unplug the PC")
            break
        elif Command in ["del_sys32"]:
            print("WARNING! this command was not shown in Help because of how destructive it is")
            conf = input("ARE YOU SURE YOU WANT TO RUN THIS COMMAND? Y or n >>> ").lower().strip()
            if conf == "y":
                print("deleting OS")
                print("sys32 deletion #-----------")
                time.sleep(0.5)
                print("sys32 deletion ##----------")
                time.sleep(0.5)
                print("sys32 deletion ###---------")
                time.sleep(0.5)
                print("sys32 deletion ####--------")
                time.sleep(0.5)
                print("sys32 deletion #####-------")
                time.sleep(0.5)
                print("sys32 deletion ######------")
                time.sleep(0.5)
                print("sys32 deletion #######-----")
                time.sleep(0.5)
                print("sys32 deletion ########-----")
                time.sleep(0.5)
                print("sys32 deletion #########---")
                time.sleep(0.5)
                print("sys32 deletion ##########--")
                time.sleep(0.5)
                print("sys32 deletion ###########-")
                time.sleep(0.5)
                print("sys32 deletion ############")
                reinstall = secrets.token_hex(10)
                print("Contact Microsoft and give them this code so you can reinstall your copy of Windows 0.3")
                print(reinstall)
                break
            if conf == "n":
                print("exiting")
        elif Command in ["winfetch"]:
            print("llllll llllll    0.1 mb of memo")
            time.sleep(0.1)
            print("llllll llllll    1.5 mb of hdd")
            print("llllll llllll    processor: manchester baby")
            time.sleep(0.2)
            print("llllll llllll    graphics:  NONE")
        elif Command.lower() == "ekdmp":
            think_time = random.randint(0, 3)

            print("EKDMP type exit to exit")
            print("WARNING, AI MAY TAKE UP A LOT OF RAM")

            keywords_negative = ["bad", "depressed", "sad", "hurts", "hurt", "unhappy" ]
            keywords_positive = ["happy", "amazing", "good", "jolly", ]
            keywords_neutral = ["meh", "ok", "yes"]
            keywords_greetings = ["hello", "hey", "hi", ]
            keywords_aggressive = ["hate", "sybau", "stfu", "shut", "stupid", "idiot", "bad", "fat",
                                   "stupid", "unworthy", "clueless"]
            keywords_goodbye = ["goodbye", "bye"]
            keywords_serious = ["suicide"]
            keywords_unusual = ["unusual", "alien", "ufo", "weird"]
            keywords_celebration = ["yay!", "yippee", "birthday", "wedding", "lottery"]
            keywords_special = ["windows0.3", "help"]
            keywords_unknown = []

            categories = {
                "aggressive": keywords_aggressive,
                "negative": keywords_negative,
                "positive": keywords_positive,
                "neutral": keywords_neutral,
                "greetings": keywords_greetings,
                "goodbye": keywords_goodbye,
                "serious": keywords_serious,
                "unusual": keywords_unusual,
                "celebration": keywords_celebration,
                "special": keywords_special,
                "unknown": keywords_unknown,
            }

            priority_order = ["serious", "aggressive", "negative", "positive", "celebration", "neutral", "greetings",
                              "goodbye", "unusual", "special"]

            responses = {
                "negative": ["Tell me more, I would love to help",
                             "Would you like to tell me more about why you're feeling like that?",
                             "It's fine, I'm here for you, tell me more",],
                "positive": ["WOW! What happened?", "Tell me more, I'm excited to know why you are so happy!",
                             "Really?? Why?"],
                "neutral": ["Tell me more...", "Ok", "How are you doing?", "I would like to know more!"],
                "aggressive": ["No need to be angry, tell me why you're feeling like that", "Ok, chill", "I'm sorry"],
                "greetings": ["hello", "hey", "hi"],
                "goodbye": ["bye", "goodbye"],
                "serious": [
                    "Im so sorry you're feeling like that, help is available, please contact your nearest therapist YOU ARE NOT ALONE!"],
                "unusual": ["That's so weird...", "I don't understand...", "How weird is that?"],
                "celebration": ["Yay! im so happy for you!", "Lets go!", "That is so cool!"],
                "special": ["Its a pretty nice OS right?", "If you would like to know more on command shell write winver!"],
                "unknown": ["you please clarify?", "I dont understand...",
                            "unfortunately I cannot understand what you're saying would you please clarify?",
                            "Please clarify", "Can you say that again but differently?", "what?", "WHAT?", "wat"]
            }

            while True:
                repetitions += 5
                if repetitions >= 60:
                    print("WARNING, 60% RAM USED, AI TURNING OFF")
                    break

                user_input = input("You: ").lower()
                if user_input == "exit":
                    break

                words = user_input.split()
                detected_category = "unknown"

                for category in priority_order:
                    if any(word in categories[category] for word in words):
                        detected_category = category
                        break
                time.sleep(think_time)

                print(">>>", random.choice(responses[detected_category]))

        else:
            print("The command '",Command,"' is not recognized, please check spelling error A230kvyfhg")

