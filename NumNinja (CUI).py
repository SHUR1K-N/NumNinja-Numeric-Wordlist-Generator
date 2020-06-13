import time; import os
from colorama import init
from termcolor import colored
from tqdm import tqdm

loopFlag = False; digitStr = 0; digits = 0; num = 0; nextLine = "\n"

init()

print(colored('''
                     ███▄    █  █    ██  ███▄ ▄███▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                    ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                       ░   ░ ░  ░░░ ░ ░ ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                             ░    ░            ░            ░  ░           ░  ░   ░        ░  ░''', 'blue'))
print(colored('''                                    NumNinja: The Number Dictionary Generator''', 'red'))
print(colored('''                                   -------------------------------------------''', 'blue'))


########## Method Elements ###########

def zeros(num):
    if (YN in ('y', 'YES', 'Y', 'Yes', 'yes', '1')):
        print()
        for i in tqdm(range(num, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write((digitStr + "\n") % num)
            num += 1
    elif (YN in ('n', 'NO', 'N', 'No', 'no', '0')):
        while (num <= maxunit):
            file.write((digitStr + "\n") % num)
            num += 1
    return num


def straight(num):
    if (YN in ('y', 'YES', 'Y', 'Yes', 'yes', '1')):
        print()
        for i in tqdm(range(num, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write("%d\n" % num)
            num += 1
    elif (YN in ('n', 'NO', 'N', 'No', 'no', '0')):
        while (num <= maxunit):
            file.write("%d\n" % num)
            num += 1
    return num


############### Main ###############

while (loopFlag is False):
    try:
        minunit = int(input("\nEnter the minimum value (Default = zero): ") or '0')
        maxunit = int(input("Enter the maximum value: "))

        if maxunit > minunit:
            Output = str(input("Enter output folder (Default = working folder):") or "./")
            Output += "/"

            print("\nSelect method:-")
            method = int(input("1. Leading Zeros 2. Staightforward: "))
            print("")
            if (method == 1):
                digits = int(input("Enter the number of digits: "))
                digitStr = ("%0")
                digitStr += ("%d" % digits)
                digitStr += ("d")
                YN = str(input("Show progress? (slower): ") or "no")

                num = minunit
                genunit = maxunit - minunit

                Output += ((digitStr) % num) + " to " + ((digitStr) % maxunit) + ".txt"

                print("\nNumber of lines that will be generated: %d" % genunit)

                with open(Output, '+w') as file:
                    start = time.time()
                    zeros(num)
                    completionTime = time.time() - start
                print("\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, genunit // completionTime))
                print("Press any key to exit.")
                input()

                loopFlag = True

                os._exit()

            elif (method == 2):
                YN = str(input("Show progress? (slower): ") or "no")
                if maxunit > minunit:

                    num = minunit
                    genunit = maxunit - minunit

                    Output += "%d to %d.txt" % (num, maxunit)

                    print("\nNumber of lines that will be generated: %d" % genunit)

                    with open(Output, '+w') as file:
                        start = time.time()
                        straight(num)
                        completionTime = time.time() - start
                    print("\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, genunit // completionTime))
                    print("Press any key to exit.")
                    input()

                    loopFlag = True

                    os._exit()

        elif (minunit == maxunit):
            print("\nThe minimum value cannot be equal to the maximum value.")

        elif (minunit > maxunit):
            print("\nThe minimum value cannot be greater than the maximum value.")
    except:
        print(e)
        print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.")
