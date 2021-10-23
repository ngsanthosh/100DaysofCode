# Implement two stacks in a single array
# The core idea is as follows, we maintain the first stack from front side... and we maintain the second stack
# from the back side of the array...The main things are how we maintain the boundary cases!! if top1==top2-1 then 
# no more elements can be added in stack 1 similarly in stack 2 top2 == top1+1 is the condition 



class TwoStacks :
	def __init__(self, n) :
		self.arr = [-1 for _ in range(n)]
		self.top1 = -1
		self.top2 = n
		self.n = n
	def isFull(self) :
		if self.top2-self.top1 == 1 :
			return True
		else :
			return False
	def isEmpty(self, sno) :
		if sno == 1 :
			if self.top1 == -1 :
				return True
			else :
				return False
		if sno == 2 :
			if self.top2 == self.n :
				return True
			else :
				return False
	def push(self, sno, x) :
		if not self.isFull() :
			if sno == 1 :
				self.top1+=1
				self.arr[self.top1] = x
				return
			if sno == 2 :
				self.top2-=1
				self.arr[self.top2] = x
				return
		else :
			print("Stack is full")
			return
	def peek(self, sno) :
		if sno == 1 :
			if not self.isEmpty(1) :
				return self.arr[self.top1-1]
		if sno == 2 :
			if not self.isEmpty(2) :
				return self.arr[self.top2-1]
	def pop(self, sno) :
		if sno == 1 :
			if not self.isEmpty(1) :
				top = self.arr[self.top1]
				self.arr[self.top1] = -1
				self.top1-=1
				return top
		if sno == 2 :
			if not self.isEmpty(2) :
				top = self.arr[self.top2]
				self.arr[self.top2] = -1
				self.top2+=1
				return top
	def PrintStack(self) :
		print(self.arr)

s = TwoStacks(10)
