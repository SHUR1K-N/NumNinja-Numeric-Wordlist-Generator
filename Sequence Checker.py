import re

try:
    while(True):
        drag = input("Drag and drop .txt file here: ")
        output = re.findall(".+\\\\(.+.txt)", drag)

        with open(str(output[0]), "r") as file:
            numList = list(map(int, file.read().strip().split()))
            prevNumber = numList[0]
            for number in numList[1:]:
                if (number == (prevNumber + 1)):
                    prevNumber = number
                    continuous = "PASSED!"
                else:
                    continuous = "FAILED!"
                    break
        print(f"Continuity check for \"{output[0]}\": {continuous}\n")
except:
    # print(e)
    print("\nPress Enter to exit...")
    input()
