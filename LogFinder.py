import math

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

start = 1000
end = 9999
step = 1
print(bold+red+"Note :\n1. Enterd number should Without decimal and without space")

while(True):
    n=float(input(cyan+bold+"\nEnter the Number To Find Log :"))
    for number in range(start, end + 1, step):
        logarithm = math.log10(number)
        log=(f"{logarithm:.4f}")
        lv = log[2:]
        if number==n:
           print(yellow+"\nLog value of ",number,"  =>  ",lgreen+lv)
           
       