import random

print("=== 猜数字游戏 ===")
print("我想了一个1到100之间的数")

secret = random.randint(1, 100)
chances = 10
guessed = False

for attempt in range(1, chances + 1):
    print(f"\n第{attempt}次机会 / 共{chances}次")
    
    try:
        guess = int(input("猜一个数: "))
    except:
        print("要输入数字啊大哥")
        continue
    
    if guess < 1 or guess > 100:
        print("在1到100之间 看清楚")
        continue
    
    if guess < secret:
        print("太小了 往大猜")
    elif guess > secret:
        print("太大了 往小猜")
    else:
        print(f"对了！就是{secret}")
        print(f"你用了{attempt}次")
        guessed = True
        break

if not guessed:
    print(f"\n机会用完了。数字是{secret}。下次加油。")
