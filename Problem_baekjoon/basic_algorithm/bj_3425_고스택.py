'''
고창영은 스택을 조금 변형해서 고스택을 만들었다.

고스택은 숫자만을 저장할 수 있고, 다음과 같은 10가지 연산을 수행할 수 있다.

편의상 스택의 가장 위에 저장된 수를 첫 번째 수라고 하고, 그 다음은 차례대로 두 번째 수, 세 번째 수라고 한다.

NUM X: X를 스택의 가장 위에 저장한다. (0 ≤ X ≤ 109)
POP: 스택 가장 위의 숫자를 제거한다.
INV: 첫 번째 수의 부호를 바꾼다. (42 -> -42)
DUP: 첫 번째 숫자를 하나 더 스택의 가장 위에 저장한다.
SWP: 첫 번째 숫자와 두 번째 숫자의 위치를 서로 바꾼다.
ADD: 첫 번째 숫자와 두 번째 숫자를 더한다.
SUB: 첫 번째 숫자와 두 번째 숫자를 뺀다. (두 번째 - 첫 번째)
MUL: 첫 번째 숫자와 두 번째 숫자를 곱한다.
DIV: 첫 번째 숫자로 두 번째 숫자를 나눈 몫을 저장한다. 두 번째 숫자가 피제수, 첫 번째 숫자가 제수이다.
MOD: 첫 번째 숫자로 두 번째 숫자를 나눈 나머지를 저장한다. 두 번째 숫자가 피제수, 첫 번째 숫자가 제수이다.

'''

class go_stack:
    def __init__(self):
        self.go_stack = []
        
    def POP(self):
        self.go_stack.pop()
        
    def NUM(self,X):
        self.go_stack.append(X)
        
    def INV(self):
        change = self.go_stack.pop()
        self.go_stack.append(-change)
    
    def DUP(self):
        add_comp = self.go_stack.pop()
        self.go_stack.append(add_comp)
        self.go_stack.append(add_comp)
        
    def SWP(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
        
        self.go_stack.append(com_2)
        self.go_stack.append(com_1)
        
    def ADD(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
       
        self.go_stack.append(com_2+com_1)
        

    def SUB(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
       
        self.go_stack.append(com_2-com_1)
        
    def MUL(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
       
        self.go_stack.append(com_2*com_1)
    
    def DIV(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
       
        self.go_stack.append(com_2//com_1)
    
    def MOD(self):
        com_1 = self.go_stack.pop()
        com_2 = self.go_stack.pop()
       
        self.go_stack.append(com_2%com_1)
    
go_stack_1 = go_stack()
go_stack_1.NUM(4)
go_stack_1.NUM(5)
go_stack_1.POP()

print(go_stack_1.go_stack)

        
        
    