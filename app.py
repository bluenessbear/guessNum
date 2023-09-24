# 猜數字
import random

answerNum = random.randint(1, 50)
for i in range(1, 5):
    guess = input("1~50 請在4次內猜出數字：")
    if guess == "" or not guess.isdigit():
        break
    elif int(guess) == answerNum:
        print(i)
        print("第" + str(i) + "次 讚！答對了^_^ ")
        quit()
    elif int(guess) > answerNum:
        print("> 第" + str(i) + "次 猜低些試試")
    elif int(guess) < answerNum:
        print("> 第" + str(i) + "次 猜高些試試")
print("\n正確答案是：" + str(answerNum))
input()
