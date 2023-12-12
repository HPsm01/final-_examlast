def solution(age): #age를 매개변수를 하는 solution 함수 정의
    trans_age = { #trans_age라는 숫자를 알파벳으로 바꾸는 딕셔너리로 매핑
        '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
        '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
    }

    if 0 < age <= 1000: #제한사항
        str_age = str(age) #age를  str로 문자열로 바꿔 str_age에 저장

        answer = ''.join(trans_age[alphabet] for alphabet in str_age)
       #answer값을 str_age 모스부호들을 매핑된 알파벳으로 바꿔주고 join을 통해 모든 값들을 공백없이 합쳐서 저장

        return answer
        #answer값으로 return

#age값을 input으로 입력받고 나중에 있을 제한 사항의 비교 때문에 int로 바꿔주었다
#solution 함수를 호출해서 answer에 저장하고 print를 통해 출력한다.

# age = input("행성의 나이를 입력하시오: ")
# age = int(age)
# answer = solution(age)
# print(answer)
