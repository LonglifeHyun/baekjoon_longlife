def main():
    word = input()
    word = word.upper()
    alpha = {}
    for i in range(ord('A'),ord('Z')+1):
        alpha[chr(i)] = 0

    for c in word:
        alpha[c] += 1

    answer = '.'
    max_cnt = 0
    for key, value in alpha.items():
        if max_cnt < value:
            max_cnt = value
            answer = key
        elif max_cnt == value:
            answer = '?'
    print(answer)

if __name__ == '__main__':
    main()

"""
1. 
[0]자리의 문자 개수 카운트 한 뒤, 해당 문자를 문자열에서 제거.
문자열 len이 0이 될 때까지 반복. 
그러면서 max 값 찾기.
같다면 중복_태그 = true 해서 일단 보류. 
더 큰 max 찾으면 갱신과 동시에 중복_태그 = false.
마지막에 태그가 false이면 해당 문자 출력. 
태그 true면 ? 출력.

2.
a~z 사이즈 만큼 리스트 생성. 
모든 알파벳에 대해서 카운트 후 리스트에 값 저장. 
리스트 선형으로 돌면서 max 값 찾기.
같다면 중복_태그 = true 해서 일단 보류. 
더 큰 max 찾으면 갱신과 동시에 중복_태그 = false.
마지막에 태그가 false이면 int(a) + 해당 index 출력. 
태그 true면 ? 출력.

3. 
[알파벳, 개수]를 가지는 리스트 생성. -> 파이썬의 경우 dictionary
모든 알파벳에 대해 하든, 문자열에 존재하는 알파벳에만 하든 값 저장 후, 
개수 중심으로 내림차순 정렬. 
개수가 [0]!=[1] 이라면 해당 문자 출력. 
만일 같다면, ? 출력.
"""