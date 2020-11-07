import multiprocessing
import time; import os
from tqdm import tqdm
from termcolor import colored
import colorama

colorama.init()

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
BANNER2 = colored('''             ----------------------------------------------''', 'blue')
BANNER3 = colored('''             || NumNinja: The Number Dictionary Generator ||''', 'red')
BANNER4 = colored('''             ----------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


########## Method Elements ###########

def zeros1(numList, chunkOne, Output, digitStr):
    try:
        with open(Output, 'a') as file:
            for number in numList[0:chunkOne]:
                file.write((digitStr + "\n") % number)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


def zeros2(numList, chunkOne, chunkTwo, Output, digitStr):
    try:
        with open(Output, 'a') as file:
            for number in numList[chunkOne:chunkTwo]:
                file.write((digitStr + "\n") % number)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


def zeros3(numList, chunkTwo, chunkThree, Output, digitStr):
    try:
        with open(Output, 'a') as file:
            for number in numList[chunkTwo:chunkThree]:
                file.write((digitStr + "\n") % number)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


def zeros4(numList, chunkThree, Output, digitStr):
    try:
        with open(Output, 'a') as file:
            for number in numList[chunkThree:]:
                file.write((digitStr + "\n") % number)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (correctInput is False):
        try:
            minunit = int(input("\nEnter the minimum value (Default = zero): ") or 0)
            maxunit = int(input("Enter the maximum value: "))

            if maxunit > minunit:
                Output = str(input("Enter output folder (Default = working folder):") or "./")
                Output += "/"

                print("\nMethods:-")
                print("1. Leading Zeros\n2. Staightforward (currently under construction)")
                method = int(input("\nSelect method number: ") or 1)
                print("")
                if (method == 1):
                    digits = int(input("Enter the number of digits: "))
                    digitStr = (f"%0{digits}d")
                    print("\nShow progress?")
                    print("1. Yes (slower)\n2. No (faster)")
                    progressPrompt = int(input("\nSelect option number (Default = No): ") or 2)

                    genunit = maxunit - minunit

                    numList = []
                    for i in range(minunit, maxunit + 1):
                        numList.append(i)
                    length = len(numList)

                    chunkOne = length // 4
                    chunkTwo = chunkOne * 2
                    chunkThree = chunkOne * 3

                    Output += ((digitStr) % minunit) + " to " + ((digitStr) % maxunit) + ".txt"

                    print(f"\nNumber of lines that will be generated: {genunit}")

                    print("\nWorking...", end='')

                    process1 = multiprocessing.Process(target=zeros1, args=[numList, chunkOne, Output, digitStr])
                    process2 = multiprocessing.Process(target=zeros2, args=[numList, chunkOne, chunkTwo, Output, digitStr])
                    process3 = multiprocessing.Process(target=zeros3, args=[numList, chunkTwo, chunkThree, Output, digitStr])
                    process4 = multiprocessing.Process(target=zeros4, args=[numList, chunkThree, Output, digitStr])

                    start = time.time()

                    processPool = [process1, process2, process3, process4]

                    for process in processPool:
                        process.start()

                    for process in processPool:
                        process.join()

                    completionTime = time.time() - start
                    rate = genunit // completionTime

                    print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} lines/sec)")
                    print("Press Enter to exit.")
                    input()

                    break

            elif (minunit == maxunit):
                print("\nThe minimum value cannot be equal to the maximum value. Please try again.\n")

            elif (minunit > maxunit):
                print("\nThe minimum value cannot be greater than the maximum value. Please try again.\n")
        except ZeroDivisionError:
            print("\n\nThe task completed successfully in zero seconds.")
            print("Press Enter to exit.")
            input()
            break
        except KeyboardInterrupt:
            print("\nCTRL ^C\n\nThrew a wrench in the works.")
            print("Press Enter to exit.")
            input()
            os._exit()
        except:
            print("\nOne of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers. Please try again.\n")
            continue
