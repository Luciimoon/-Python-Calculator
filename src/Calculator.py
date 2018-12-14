
Running = True

def simplify(num, msg):
    del msg[0:3]
    msg.insert(0, str(num))


def calculate(msg):
    msg = [x for x in msg if x != ' ']
    while (len(msg) > 1):

        if(msg[0].isdigit() and msg[1].isdigit()):
            msg[:2] = [''.join(msg[:2])]
        if(len(msg) > 3):
            if(msg[2].isdigit() and msg[3].isdigit()):
                msg[2:4] = [''.join(msg[2:4])]

        if ('+' in msg[:2]):
            cal = float(msg[0]) + float(msg[2])
            simplify(cal, msg)
        elif ('-' in msg[:2]):
            cal = float(msg[0]) - float(msg[2])
            simplify(cal, msg)
        elif ('*' in msg[:2]):
            cal = float(msg[0]) * float(msg[2])
            simplify(cal, msg)
        elif ('/' in msg[:2]):
            cal = float(msg[0]) / float(msg[2])
            simplify(cal, msg)
        elif ('**' in msg[:3] or '^' in msg[:2]):
            cal = float(msg[0]) ** float(msg[2])
            simplify(cal, msg)
        elif ('//' in msg[:3]):
            cal = float(msg[0]) // float(msg[2])
            simplify(cal, msg)
        elif ('%' in msg[:2]):
            cal = float(msg[0]) % float(msg[2])
            simplify(cal, msg)
        else:
            cal = 'error'
    print(cal)

while (Running):
    x = list(input('equation?'))
    calculate(x)

    GoAgain = input("\ndo you want to go again?").lower()
    if (GoAgain == "yes" or GoAgain == "y"):
        Running = True
    elif (GoAgain == "no" or GoAgain == "n"):
        Running = False
    else:
        print('error, please try again')