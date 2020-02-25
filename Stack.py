class Stack:
	stack=[]
	max_size=-1
	def __init__(self,size=-1):
		self.max_size=size
	def push(self,item):
		if self.max_size==-1:
			self.stack.append(item)
		elif len(self.stack)<self.max_size:
			self.stack.append(item)
		else:
			print('Stack is full')
			raise RuntimeError
	def pop(self):
		if len(self.stack)>0:
			t=self.stack[-1]
			self.stack.pop()
			return t
		else:
			print('Stack is empty')
			raise IndexError

	def top(self):
		if len(self.stack)>0:
			return self.stack[-1]
		else:
			print('Stack is already empty')
			raise IndexError


S=Stack()
n=1
while n!=0:
	print('0:Exit\n1-Push\n2-Pop\n3:Peek\n')
	n=int(input('Enter the operation to perform :'))
	if n==0:
		exit
	elif n==1:
		p=int(input('Enter the element to push on the stack'))
		S.push(p)
	elif n==2:
		print('The element removed from the stack :',S.pop())
	elif n==3:
		print('The element at top of the stack: ',S.top())

		
