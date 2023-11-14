import random
def main():
    Number = random.randint(1,100)
    while True :
        userguess = int(input("ป้อนตัวเลข: "))
        if userguess == Number:
         print("ยินดีด้วยคุณทายถูก")
         break
        elif userguess > Number :
         print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        else :
         print("คุณทายผิดตัวเลขที่ป่อนน้อยเกินไป")
