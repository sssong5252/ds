a = int(input())
stack = [None] * a

def push(n): #푸시 함수 0번 인덱스 입력 오류 해결 필요
    if stack[a-1] is None:
        stack[a-1] = n

    else:
        for i in range(a-2, -1, -1):
            if stack[i] is None:
                stack[i] = n
                return

            else:
                print("err: full stack", stack[n])
            
    def pop():
        for i in stack:
            if i is not None:
                i = None
                break
        
        
    # pop 함수: pop 입력 시 스택의 마지막 값 확인 후 제거. 마지막 값 None 으로 바꾸기
    
 

push(5)
push(4)
push(3)
push(2)
push(1)
print(stack)