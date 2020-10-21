# Testing for file writing
with open('C:/Users/Hubert/Desktop/Python Crash course project/Alien Invasion/HighScore.txt','r') as fh:
    for i in fh:
        y = int(i)

x = 10000

if x > y:
 with open('C:/Users/Hubert/Desktop/Python Crash course project/Alien Invasion/HighScore.txt','w') as fh:
    print(x,file=fh)
    