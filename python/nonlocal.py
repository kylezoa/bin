x=10

def func_core():
	x = 2
	
	print ("x is", x)
	
	def func_inner():
		nonlocal x
		x=3
		
	func_inner()
	print('changed local x to',x)
	
func_core()
	
	