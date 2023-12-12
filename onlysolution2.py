# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

letter = ".. -.-. .- -. - .... .. ... .- .-.. .-.. -.. .- -.--"

def solution(letter): #letter을 매개변수로하는 solution함수 정의
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    #딕셔너리를 이용해서 모스부호를 알파벳으로 매핑한다

    morse_code = letter.split(' ')
    #매개변수를 통해 들어온 letter을 ' '(띄어쓰기)를 기준으로 분리 해서 morse_code에 저장한다

    answer = ''.join(morse[code]for code in morse_code)
    #answer값을 morse_code안에 있는 분리된 letter의 모스부호들을 매핑된 알파벳으로 바꿔주고
    #join을 통해 중간에 공백없이 합쳐준다

    return answer
    #answer값으로 return

# letter = ".. -.-. .- -. - .... .. ... .- .-.. .-.. -.. .- -.--"
# answer = solution(letter)
# print(answer)

#letter을 내가 생각났던 명대사였던 캡틴아메리카 명대사가 나오도록 letter에 저장
#함수를 호출해서 answer값에 저장
#answer값을 출력