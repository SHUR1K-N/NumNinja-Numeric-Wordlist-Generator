import time; import os
from tkinter import *
from tkinter import filedialog, messagebox
from tqdm import tqdm, tqdm_gui


########## Method Elements ###########

def zeros(num):
    if (progressBar == 1):
        print()
        for i in tqdm_gui(range(num, maxunit + 1), desc="Progress: ", unit=" numbers", unit_scale=1):
            file.write((digitStr + "\n") % num)
            num += 1
    elif (progressBar == 0):
        while (num <= maxunit):
            file.write((digitStr + "\n") % num)
            num += 1


def straight(num):
    if (progressBar == 1):
        print()
        for i in tqdm_gui(range(num, maxunit + 1), desc="Progress: ", unit=" numbers", unit_scale=1):
            file.write(f"{num}\n")
            num += 1
    elif (progressBar == 0):
        while (num <= maxunit):
            file.write(f"{num}\n")
            num += 1


############## GUI Elements ##############

def browse_button():
    global output
    filename = filedialog.askdirectory()
    output.set(filename)


def checkDigits():
    if (method.get() == 1):
        dig.configure(state="normal")
        dig.update()
    elif(method.get() == 2):
        dig.configure(state="disabled")
        dig.update()


def errorGreater():
    error = Tk()
    error.iconbitmap("shur1ken.ico")
    error.withdraw()
    messagebox.showerror("Error", "The minimum value cannot be greater than the maximum value.")
    error.destroy()


def errorEqual():
    error = Tk()
    error.iconbitmap("shur1ken.ico")
    error.withdraw()
    messagebox.showerror("Error", "The minimum value cannot be equal to the maximum value.")
    error.destroy()


def errorInvalid():
    error = Tk()
    error.iconbitmap("shur1ken.ico")
    error.withdraw()
    messagebox.showerror("Error", "One of more of the inputs are invalid. This can happen when any spaces or other characters have been entered instead of numbers, or the specified file path is invalid. Please try again.")
    error.destroy()


def doneBox():
    done = Tk()
    done.iconbitmap("shur1ken.ico")
    done.withdraw()
    messagebox.showinfo("Done!", f"The task completed successfully in {completionTime} seconds.")
    done.destroy()


def exitMeta():
    os._exit(0)


############### Main ###############

if __name__ == "__main__":

    while (True):

        root = Tk()

        minunit = IntVar()
        maxunit = IntVar()
        method = IntVar()
        progressBar = IntVar()
        output = StringVar()
        digits = IntVar()

        method.set(1)

        root.resizable(0, 0)
        root.geometry("441x260+800+400")
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)
        root.iconbitmap("shur1ken.ico")
        root.title("NumNinja: The Number Dictionary Generator")
        root.protocol('WM_DELETE_WINDOW', exitMeta)

        Label(root, text="Minimum value: ").place(x=43, y=12)
        Entry(root, justify=CENTER, width=25, textvariable=minunit).place(x=12, y=35, height=25)

        Label(root, text="Maximum value: ").place(x=307, y=12)
        Entry(root, justify=CENTER, width=25, textvariable=maxunit).place(x=275, y=35, height=25)

        Leading = Radiobutton(root, text="Leading Zeros Method", value=1, variable=method, command=checkDigits).place(x=12, y=80)
        Straightforward = Radiobutton(root, text="Straightforward Method", value=2, variable=method, command=checkDigits).place(x=12, y=110)

        Label(root, text="digits").place(x=232, y=83)
        dig = Entry(root, justify=CENTER, width=4, textvariable=digits)
        dig.place(x=200, y=81, height=25, width=30)

        Checkbutton(root, text="Show progress (slower)", variable=progressBar).place(x=12, y=190)

        Entry(root, justify=CENTER, width=55, textvariable=output).place(x=12, y=150, height=25)
        Button(text="Browse", width=10, command=browse_button).place(x=353, y=150, height=25)

        Button(root, text="Start", width=10, command=root.destroy).place(x=175, y=230, height=25)

        root.mainloop()

        try:
            minunit = minunit.get()
            maxunit = maxunit.get()
            method = method.get()
            digits = digits.get()
            progressBar = progressBar.get()
            output = output.get()

            output += "./"

            if (maxunit > minunit):
                if (method == 1):
                    digitStr = (f"%0{digits}d")

                    num = minunit
                    output += ((digitStr) % num) + " to " + ((digitStr) % maxunit) + ".txt"

                    with open(output, '+w') as file:
                        start = time.time()
                        zeros(num)
                        completionTime = time.time() - start
                    file.close()

                    doneBox()

                    correctInput = True

                    os._exit(0)

                elif (method == 2):
                    num = minunit
                    output += f"{num} to {maxunit}.txt"

                    with open(output, '+w') as file:
                        start = time.time()
                        straight(num)
                        completionTime = time.time() - start
                    file.close()

                    doneBox()

                    break

                    os._exit(0)

            elif (maxunit < minunit):
                errorGreater()
            elif (maxunit == minunit):
                errorEqual()
        except:
            #print(e)
            errorInvalid()
