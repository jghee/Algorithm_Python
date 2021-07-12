def solution(nums):
    answer = 0
    result = 0
    tmp = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                for c in range(1, result + 1):
                    if result % c == 0:
                        tmp += 1
                if tmp < 3:
                    answer += 1
                tmp = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)

    return answer
