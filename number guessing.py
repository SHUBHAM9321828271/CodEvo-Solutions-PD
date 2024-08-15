import random
x = int(input("STARTING RANGE = "))
y = int(input("ENDING RANGE = "))
z = random.randint(x,y)
#g = int(input("GUESS : "))
count = 0
end = 20
while count < 20:
    count += 1
    g = int(input("GUESS : "))
    if (z > g):
        print("YOU HAVE GUESSED IT TOO LOW!!")
        print("chances remaining = %d"%(end-count))
    elif(g > z):
        print("YOU HAVE GUESSED IT TOO HIGH!!")
        print("chances remaining = %d"%(end-count))
    elif(g > 100):
        print("GUESS BTWEEN 0 TO 100")
        print("chances remaining = %d"%(end-count))
    elif(z==g):
        print("win")

    
