# Q.1 10점
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

#함수정의
def solution(my_string, target):
    # my_string과 target을 매개변수로 하는 함수 solution 정의

    if 1 <= len(my_string) <= 100 and 1 <= len(target) <= 100:
    #제한사항을 if문으로 만들어
    #my_string과 target의 길이가 1보다 크거나 같고 100보다 작거나 같게 만들어줌

        if target in my_string:
        # 만약 target이 my_string 안에 포함되어 있다면 anser을 1로 초기화
            answer = 1

            return answer
            #answer값으로 return
        else: #그렇지않으면 answer을 0으로 초기화
            answer = 0

            return answer
            #answer값으로 return

# my_string=input("my_string값을 입력해주세요: ")
# target=input("target값을 입력해주세요: ")
# answer = solution(my_string,target)
# print(answer)


#my_string값과 target값을 input으로 사용자로부터 값을 받아 초기화
#solution 함수를 호출해서 answer를 선언하고 초기화 해준다
#answer값을 출력