N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)


"""
import sys

def solution(data):
    '''
        Notes:
            1. n까지의 수를 스택에 push
            2. 마지막 값을 pop한 뒤 max에 저장
            3. 다음 수가 작을 경우 해당값까지 pop
            4. 다음 수가 클 경우 max부터 push
            5. 마지막 값을 pop한 뒤 max에 저장
    '''

    answer=[]
    stack=[]
    max = 0
    for d in data:
        if stack and stack[-1]>d:
            print("NO")
            return 0
        elif max < d:
            for i in range(max+1, d+1):
                stack.append(i)
                answer.append('+')
            max = stack.pop()
            answer.append('-')
        else:
            while stack and stack[-1] >= d:
                stack.pop()
                answer.append('-')
    for a in answer:
        print(a)

n = int(input())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
solution(data)

"""