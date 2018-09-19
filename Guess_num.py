import random

answer = random.randint(1,100)

num=int(input("Please input a num:"))

while num != answer:
    if num > answer:
        num=int(input("The num is more,input a num"))
    elif num < answer:
        num=int(input("The num is less,input a num"))
print("You are Win!")