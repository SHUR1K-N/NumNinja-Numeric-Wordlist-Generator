import time; import os
from colorama import init
from termcolor import colored
from tqdm import tqdm

correctInput = False; digitStr = 0; digits = 0; num = 0

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
    if (YN == "1"):
        print()
        for i in tqdm(range(num, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write((digitStr + "\n") % num)
            num += 1
    elif (YN == "2"):
        while (num <= maxunit):
            file.write((digitStr + "\n") % num)
            num += 1
    return(num)


def straight(num):
    if (YN == "1"):
        print()
        for i in tqdm(range(num, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write("%d\n" % num)
            num += 1
    elif (YN == "2"):
        while (num <= maxunit):
            file.write("%d\n" % num)
            num += 1
    return(num)


############### Main ###############

while (correctInput is False):
    try:
        minunit = int(input("\nEnter the minimum value (Default = zero): ") or '0')
        maxunit = int(input("Enter the maximum value: "))

        if maxunit > minunit:
            Output = str(input("Enter output folder (Default = working folder):") or "./")
            Output += "/"

            print("\nMethods:-")
            print("1. Leading Zeros\n2. Staightforward")
            method = int(input("\nSelect method number (Default = Straightforward): ") or "2")
            print("")
            if (method == 1):
                digits = int(input("Enter the number of digits: "))
                digitStr = ("%0")
                digitStr += ("%d" % digits)
                digitStr += ("d")
                print("\nShow progress?")
                print("1. Yes (slower)\n2. No (faster)")
                YN = input("\nSelect option number (Default = No): ") or "2"

                num = minunit
                genunit = maxunit - minunit

                Output += ((digitStr) % num) + " to " + ((digitStr) % maxunit) + ".txt"

                print("\nNumber of lines that will be generated: %d" % genunit)

                print("\nWorking...", end='')

                with open(Output, '+w') as file:
                    start = time.time()
                    zeros(num)
                    completionTime = time.time() - start
                file.close()
                print("\n\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, genunit // completionTime))
                print("Press any key to exit.")
                input()

                os._exit()
                break

            elif (method == 2):
                print("\nShow progress?")
                print("1. Yes (slower)\n2. No (faster)")
                YN = input("\nSelect option number (Default = No): ") or "2"
                if maxunit > minunit:

                    num = minunit
                    genunit = maxunit - minunit

                    Output += "%d to %d.txt" % (num, maxunit)

                    print("\nNumber of lines that will be generated: %d" % genunit)

                    print("\nWorking...", end='')

                    with open(Output, '+w') as file:
                        start = time.time()
                        straight(num)
                        completionTime = time.time() - start
                    file.close()
                    print("\n\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, genunit // completionTime))
                    print("Press any key to exit.")
                    input()

                    os._exit()
                    break

        elif (minunit == maxunit):
            print("\nThe minimum value cannot be equal to the maximum value.")

        elif (minunit > maxunit):
            print("\nThe minimum value cannot be greater than the maximum value.")
    except:
        print(e)
        print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.")
        continue
