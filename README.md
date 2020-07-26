# NumNinja: The Number Dictionary Generator

A super fast number dictionary generator (700,000+ lines per second) I created from scratch, that takes the following as input:

- A custom range of integers to generate within
- Method (either Leading Zeros or Straightforward)
- Output location for the generated .txt file

...and then generates a text document with all the integers in ascending order either by the Leading Zeros method (constant length of digits from start to end) or the Straightforward method (varying digit length); ideal to aid dictionary attacks performed upon a number-based pin system, or with a possibility of the password being regular/contact numbers. This project was created in Python and has both versions — graphical UI and console UI.

**Dependencies you may have to "pip install" before being able to run the Python file(s):**

**tqdm** (for GUI progress bars)

**tkinter** (for GUI elements)

**colorama** (for colors)

**termcolor** (for colors)

My website: http://bit.do/SHUR1KN