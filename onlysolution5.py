# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

numbers = [8, 30, 17, 2, 23]
def solution(numbers): #numbers를 매개변수로 하는 solution함수 정의
    numbers = list(map(str, numbers))

    def compare(x, y): #x와 y를 매개변수로 하는 compare함수 정의
        if 0 > int(x + y) - int(y + x): #먄악 x와 y의 순서를 다르게해서 뺐을 때 음수면 1 양수면 0을 출력한다.
          return 1
        elif  0 < int(x + y) - int(y + x) :
          return 0

    for i in range(len(numbers) - 1): #i를 numbers-1의 길이만큼 반복
        for j in range(i + 1, len(numbers)):#범위가 i+1부터 numbers까지만큼 반복

            if compare(numbers[i], numbers[j]) == 1: #만약 numbers[i],numbers[j]를  compare했을때 결과가 1이면
                numbers[i], numbers[j] = numbers[j], numbers[i]  #numbers[j]와 number[i]의 순서를 바꿔서 저장

            # elif compare(numbers[i], numbers[j]) == 0:
            #     numbers[i], numbers[j] = numbers[i], numbers[j]
            # 0이면 바꿀필요가 없으니 생략

    answer = ''.join(numbers) #join으로 공백없이 numbers를 합쳐서 answer에 저장
    return str(answer) #제한사항 문자열로 바꾸기 위해 str을 사용해서 answer값 return

# numbers = [8, 30, 17, 2, 23]
# answer =solution(numbers)
# print(answer)
# #numbers 배열 선언하고
# #answer에 solution함수를 변수를 numbers로 하여 호출하고 print로 출력
