class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
n = int(input())
head = node(n)
# print(head.data)
# print(node)

def add(val): #값 링크드리스트에 노드를 더하는 함수
    new = node(val)
    if head.next is None:
        head.next = new
        print("잘되는 중")
        print("길이: ",length())
    # elif type(head.next) is not None:
    #     p = int(input("몇번째?: "))
    #     if p >= length() or p < 1:
    #         print("err")
    #     else :
    #         for i in range(p-1):
    #             loc = loc.next
    #         loc.next(val)
    else:
        print("길이: ",length())
        p = int(input("몇번째?: "))
        if p > length() or p < 1:
            print("err")
            return
        
        loc = head
        for i in range(p-1):
            loc = loc.next
        new.next = loc.next
        loc.next = new
        
def length():
    k = head
    l = 0
    while k is not None:
        l += 1
        k = k.next
    return l
        
        
def delete(): #링크드리스트에서 노드를 삭제하는 기능을 구현하는 함수
    #구현 방안: 실제 구동 방식은 삭제를 하는 방식이 아닌 1->2->3으로 연결 되어 있다고 했을 때 1을 3에 연결하면서 2에 대한 존재를 지우는 것
    print("길이: " ,length())
    p = int(input("몇번째 노드 삭제?: "))
    if p > length() or p < 1:
        print("err")

    elif p == 1:
        global head
        head = head.next
        return
    
    loc = head
    
    for i in range(p-2): #p-1은 삭제 대상 노드 -2하면 삭제 대상 노드 바로 앞 노드
        loc = loc.next
        
    loc.next = loc.next.next
        
add(2)
add(3)
add(4)
delete()
loc = head

while loc is not None:
    print(loc.data)
    loc = loc.next