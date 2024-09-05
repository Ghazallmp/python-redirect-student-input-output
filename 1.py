import sys
fin=open("input.txt","rt")
sys.stdin=fin
fout=open("output.txt","wt")
sys.stdout=fout
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