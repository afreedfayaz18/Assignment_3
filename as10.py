import time
def timedecor(func):
	def inner_dec(*x):
		start=time.time()
		func(*x)
		end=time.time()
		print("time taken:",str((end-start)*1000),"milliseconds")
	return inner_dec

@timedecor
def cal_square(*numbers):
	sqre_list=[]
	for i in numbers:
		sqre_list.append(i*i)
	print(sqre_list)

@timedecor
def cal_cube(*numbers):
	cube_list=[]
	for i in numbers:
		cube_list.append(i*i*i)
	print(cube_list)

cal_square(1,2,3)
cal_cube(3,4,5,6)
