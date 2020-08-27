import time
import multiprocessing
import threading
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

def zeros1(numList, chunkOne, Output, digitStr):
    with open(Output, 'a') as file:
        for number in numList[0:chunkOne]:
            file.write((digitStr + "\n") % number)
    return


def zeros2(numList, chunkOne, chunkTwo, Output, digitStr):
    with open(Output, 'a') as file:
        for number in numList[chunkOne:chunkTwo]:
            file.write((digitStr + "\n") % number)
    return


def zeros3(numList, chunkTwo, chunkThree, Output, digitStr):
    with open(Output, 'a') as file:
        for number in numList[chunkTwo:chunkThree]:
            file.write((digitStr + "\n") % number)
    return


def zeros4(numList, chunkThree, Output, digitStr):
    with open(Output, 'a') as file:
        for number in numList[chunkThree:]:
            file.write((digitStr + "\n") % number)
    return


############### Main ###############

if __name__ == "__main__":

    printBanner()

    while (correctInput is False):
        try:
            minunit = int(input("\nEnter the minimum value (Default = zero): ") or '0')
            maxunit = int(input("Enter the maximum value: "))

            if maxunit > minunit:
                Output = str(input("Enter output folder (Default = working folder):") or "./")
                Output += "/"

                print("\nMethods:-")
                print("1. Leading Zeros\n2. Staightforward (currently under construction")
                method = int(input("\nSelect method number (Default = Straightforward): ") or "2")
                print("")
                if (method == 1):
                    digits = int(input("Enter the number of digits: "))
                    digitStr = (f"%0{digits}d")
                    print("\nShow progress?")
                    print("1. Yes (slower)\n2. No (faster)")
                    progressPrompt = input("\nSelect option number (Default = No): ") or "2"

                    genunit = maxunit - minunit

                    numList = []
                    for i in range(minunit, maxunit + 1):
                        numList.append(i)
                    length = len(numList)

                    chunkOne = length // 4
                    chunkTwo = chunkOne * 2
                    chunkThree = chunkOne * 3

                    Output += ((digitStr) % minunit) + " to " + ((digitStr) % maxunit) + ".txt"

                    print("\nNumber of lines that will be generated: %d" % genunit)

                    print("\nWorking...", end='')

                    process1 = multiprocessing.Process(target=zeros1, args=[numList, chunkOne, Output, digitStr])
                    process2 = multiprocessing.Process(target=zeros2, args=[numList, chunkOne, chunkTwo, Output, digitStr])
                    process3 = multiprocessing.Process(target=zeros3, args=[numList, chunkTwo, chunkThree, Output, digitStr])
                    process4 = multiprocessing.Process(target=zeros4, args=[numList, chunkThree, Output, digitStr])

                    start = time.time()

                    process1.start()
                    process2.start()
                    process3.start()
                    process4.start()
                    process1.join()
                    process2.join()
                    process3.join()
                    process4.join()

                    completionTime = time.time() - start

                    print("\n\nThe task completed successfully in %f seconds. (at ~%d lines/sec)" % (completionTime, genunit // completionTime))
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
