import time
from colorama import init
from termcolor import colored
from tqdm import tqdm

correctInput = False

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
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)


########## Method Elements ###########

def zeros():
    if (progressPrompt == "1"):
        for number in tqdm(range(minunit, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write((digitStr + "\n") % number)
    elif (progressPrompt == "2"):
        for number in range(minunit, maxunit + 1):
            file.write((digitStr + "\n") % number)
    return


def straight():
    if (progressPrompt == "1"):
        for number in tqdm(range(minunit, maxunit + 1), desc="Progress", unit=" numbers", unit_scale=1):
            file.write(f"{number}\n")
    elif (progressPrompt == "2"):
        for number in range(minunit, maxunit + 1):
            file.write((digitStr + "\n") % number)
    return


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (correctInput is False):
        try:
            minunit = int(input("\nEnter the minimum value (Default = zero): ") or '0')
            maxunit = int(input("Enter the maximum value: "))

            genunit = maxunit - minunit

            if maxunit > minunit:
                Output = str(input("Enter output folder (Default = working folder):") or "./")
                Output += "/"

                print("\nMethods:-")
                print("1. Leading Zeros\n2. Staightforward")
                method = int(input("\nSelect method number (Default = Straightforward): ") or "2")
                print("")

                digits = int(input("Enter the number of digits: "))

                if (method == 1):
                    digitStr = (f"%0{digits}d")
                    Output += ((digitStr) % minunit) + " to " + ((digitStr) % maxunit) + ".txt"

                elif (method == 2):
                    Output += f"{minunit} to {maxunit}.txt"

                print("\nShow progress?")
                print("1. Yes (slower)\n2. No (faster)")

                progressPrompt = input("\nSelect option number (Default = No): ") or "2"

                print(f"\nNumber of lines that will be generated: {genunit}")

                print("\nWorking...", end='')

                if (method == 1):
                    with open(Output, 'w') as file:
                        start = time.time()
                        zeros()
                        completionTime = time.time() - start

                elif (method == 2):
                    with open(Output, 'w') as file:
                            start = time.time()
                            straight()
                            completionTime = time.time() - start

                rate = genunit // completionTime
                print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} lines/sec)")
                print("Press any key to exit.")
                input()

                break

            elif (minunit == maxunit):
                print("\nThe minimum value cannot be equal to the maximum value. Please try again.\n")

            elif (minunit > maxunit):
                print("\nThe minimum value cannot be greater than the maximum value. Please try again.\n")

        except ZeroDivisionError:
            print("\n\nThe task completed successfully in zero seconds.")
            print("Press any key to exit.")
            input()
            break

        except:
            print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.\n")
            continue
