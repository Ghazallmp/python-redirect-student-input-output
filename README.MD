# How to redirect standard input outpt

to import from input use sys:
```python 
import sys
```
this is how to read from input named:"input.txt":
```python 
fin=open("input.txt","rt")
sys.stdin=fin
```
this is how to write output and name it to"output.txt"
```python 
fout=open("output.txt","wt")
sys.stdout=fout
```
this is how to calculate two numbers from input:
```python
while True:
    parts=input().strip().split()
    if parts[0]=="add":
        print(int(parts[1])+int(parts[2]))
    elif parts[0]=="sub":
        print(int(parts[1])-int(parts[2]))
    elif parts[0]=="mul":
        print(int(parts[1])*int(parts[2]))
    elif parts[0]=="truediv":
        print(int(parts[1])/int(parts[2]))
    elif parts[0]=="floordiv":
        print(int(parts[1])%int(parts[2]))
    elif parts[0]=="pow":
        print(int(parts[1])**int(parts[2]))
    else:
        break
```