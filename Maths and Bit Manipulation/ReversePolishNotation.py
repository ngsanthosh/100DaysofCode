class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-":
                b=stack.pop()
                a=stack.pop()
                # print("a-b",a-b)
                stack.append(a-b)
            elif i=="*":
                # print(stack.pop())
                # print(stack.pop())
                stack.append(stack.pop()*stack.pop())
            elif i=="/":
                b=stack.pop()
                a=stack.pop()
                
                stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[0]
        