import time; import os
import colorama
from termcolor import colored
from tqdm import tqdm

colorama.init()

BANNER1 = colored('''
                     ███▄    █  █    ██  ███▄ ▄███▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                    ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                       ░   ░ ░  ░░░ ░ ░ ░      ░      ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                             ░    ░            ░            ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                                    NumNinja: The Number Dictionary Generator''', 'red')
BANNER3 = colored('''                                   -------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


########## Method Elements ###########

def zeros():
    if (progressBar == "1"):
        for number in tqdm(range(minunit, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write((digitStr + "\n") % number)
    elif (progressBar == "2"):
        for number in range(minunit, maxunit + 1):
            file.write((digitStr + "\n") % number)


def straight():
    if (progressBar == "1"):
        for number in tqdm(range(minunit, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write(f"{number}\n")
    elif (progressBar == "2"):
        for number in range(minunit, maxunit + 1):
            file.write(f"{number}\n")


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()
    try:

        while (True):
            try:
                minunit = int(input("\nEnter the minimum value (Default = zero): ") or 0)
                maxunit = int(input("Enter the maximum value: "))

                if maxunit > minunit:
                    break

                elif (minunit == maxunit):
                    clrscr()
                    print("\nThe minimum value cannot be equal to the maximum value. Please try again.\n")
                    continue

                elif (minunit > maxunit):
                    clrscr()
                    print("\nThe minimum value cannot be greater than the maximum value. Please try again.\n")
                    continue
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                clrscr()
                print("\nInvalid entry (not an integer). Please try again.\n")
                continue

        while (True):
            print("\n\nMethods:-")
            print("1. Leading Zeros\n2. Staightforward")
            method = input("\nSelect method number (Default = Straightforward): ") or "2"
            print("")

            if (method == "1"):
                digits = int(input("Enter the number of digits: "))
                digitStr = (f"%0{digits}d")
                break
            elif (method == "2"):
                break
            else:
                clrscr()
                print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
                continue

        while (True):
            print("\nShow progress?")
            print("1. Yes (slower)\n2. No (faster)")
            progressBar = input("\nSelect option number (Default = No): ") or "2"

            if (progressBar == "1" or progressBar == "2"):
                break
            else:
                clrscr()
                print("\nInvalid entry. Choose either option 1 or 2. Try again.\n")
                continue

        while (True):
            output = input("\nEnter output folder (Default = working folder):") or "./"
            output += "/"

            if (os.path.exists(output) is True):
                break
            else:
                clrscr()
                print("\nEither path does not exist or invalid path entered. Try again.\n")
                continue

        clrscr()
        genunit = maxunit - minunit
        print(f"\nNumber of lines that will be generated: {genunit}")

        print("\nWorking...", end='')

        if (method == "1"):
            output += ((digitStr) % minunit) + " to " + ((digitStr) % maxunit) + ".txt"
            with open(output, 'w') as file:
                start = time.time()
                zeros()
                completionTime = time.time() - start

        elif (method == "2"):
            output += f"{minunit} to {maxunit}.txt"
            with open(output, 'w') as file:
                start = time.time()
                straight()
                completionTime = time.time() - start

        try:
            rate = genunit // completionTime
            clrscr()
            print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} lines/sec)")
            print("Press Enter to exit.")
            input()

        except ZeroDivisionError:
            clrscr()
            print("\n\nThe task completed successfully in zero seconds.")
            print("Press Enter to exit.")
            input()
    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
