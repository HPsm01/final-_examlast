# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000
import math #표준라이브러리 모듈 중에 math 모듈을 가져옴

def solution(r1, r2): #r1,r2를 매개변수를 하는 solution함수 정의
    if  (1 <= r1 < r2 <= 1000000): #제한사항


      answer = 0 #answer를 0으로 초기화

    for x in range(-r2, r2 + 1): #x의 범위를 -r2부터 r2+1까지 for문으로 반복
        for y in range(-r2, r2 + 1):#y의 범위를 -r2부터 r2+1까지 for문으로 반복

            distance = math.sqrt(x**2 + y**2)
             #distance를 원들의 중심은 원점이니
             # 원점부터 점의 거리가 작은원의 반지름보다 크고 큰원 반지름보다 작은 점이 만약 있따면 answer에 1씩 더해준다
            if r1 <= distance <= r2:
                answer += 1

    return answer
    #answer값으로 return

# r1 = input("r1을 입력하시오: ")
# r1 = (int)(r1)
# r2 = input("r2을 입력하시오: ")
# r2 = (int)(r2)
# answer = solution(r1, r2)
# print(answer)

#r1의 값이랑 r2의 값을 input으로 받아주고 둘을 int형식으로 바꿔준다
#solution함수를 호출해서 answer값에 저장 하고 print로 answer값을 출력해준다.