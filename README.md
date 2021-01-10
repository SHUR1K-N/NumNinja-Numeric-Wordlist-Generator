# NumNinja: Number Dictionary Generator

## Description & Usage
A super-high speed numeric dictionary generator (up to 2M+ lines per second), that generates a file with all the integers within a user-specified range, either by the Leading Zeros method or Straightforward method; ideal for aiding dictionary attacks performed against a number-based pin system, or if the candidates to be tried are within, say, a specific range of contact or ID numbers.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator/master/Images/CUI%20Example.png" >
<p>Example Execution</p>
</div>

### Example
If a specific network vendor's SIM numbers begin with either the digit `7` or `8`, a dictionary consisting of all integers `70000000 – 89999999` would be both more efficient in terms of space and time for finding the correct candidate, than trying a significantly larger dictionary that consists of all integers `00000000 – 99999999`.

## Generation Methods
### Leading Zeros
Generates integers within the user-defined constraints, **at a *constant* length (also user-defined)**, for example:

```
00000
00001
00002
...
00068
00069
...
00999
01000
...
09998
09999
10000
```

### Straightforward
Generates integers within the user-defined constraints, **at *incremental* lengths**, for example:

```
0
1
2
...
68
69
...
999
1000
...
9998
9999
10000
```

This project was created in Python, and comes with a graphical UI version as well.

## Optimization
The extremely high integer generation speed is owed to the implementation of multiprocessing in this program (the regular version of the program is completely functional, but the much faster multiprocessing version is still an active work in progress).

## Dependencies to PIP-Install
- **tqdm** (for progress bars)
- **tkinter** (for GUI elements)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
