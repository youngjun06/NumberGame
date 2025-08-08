import random
import os
import json
import math
import datetime as dt

if os.path.exists("score.json"):
    try:
        with open("score.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            top_score = data[0]["score"]
            day = data[0]["day"]
            print("게임을 시작합니다.")
            print(f"[{day}] 최고 기록 {top_score}")
    except:
        top_score = 999
        print("게임을 시작합니다.")
        print(f"최고 기록: {top_score}")
else:
    top_score = 999
    print("게임을 시작합니다.")
    print(f"최고 기록: {top_score}")


number = random.randint(1, 100)
try_num = 0
# print("답: ", number)

while True:
    try_num += 1
    print("-"*10)
    print(f"{try_num}번 시도 ", end="")
    answer = int(input(">> "))
    if answer == number:
        print("정답입니다.")
        break
    else:
        if answer > number:
            print("DOWN")
        else:
            print("UP")
        if try_num >= 5:
            hit = math.sqrt(number)
            print("힌트: ", hit)
print(f"정답: {number}, 시도 횟수: {try_num}")
print("-"*10)

if try_num <= top_score:
    print("최고 기록입니다!")
    data = [{"day": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "score": try_num}]
    with open("score.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
