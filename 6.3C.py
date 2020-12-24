import socket
import sys
import os

cl = socket.socket()
host = '192.168.0.101'
port = 8888

try:
	cl.connect((host,port))
	print('Successfull Connect')
except socket.error as e:
	print (str(e))

while True:
	print('Welcome to the calculator')
	print('1-Log expression')
	print('2-Square root')
	print('3-Exponential expression')
	print('0-exit')

	ans = input('Enter your choice:')
	cl.send(ans.encode())
	os.system('clear')
	if ans == '1':
		#log
		print('Log fucntion')
		num=input('Enter number:')
		b = input('Enter base:')
		cl.send(num.encode())
		cl.send(b.encode())
		total=cl.recv(1024)

		print('Answer :'+ str(total.decode('utf-8')))
	elif ans == '2':
		# root
		cod = True
		while cod:
			print('Square root function')
			num =input('Enter number:')
			if int(num)> -1:
				cod = False
				cl.send(num.encode())
				total=cl.recv(1024)
			else:
				print('Enter positive number')

		print('Answer :'+ str(total.decode('utf-8')))

	elif ans == '3':
		#exponen
		print('Exponential funciton')
		num=input('Enter number:')
		cl.send(num.encode())
		total=cl.recv(1024)
		print('Answer :'+ str(total.decode('utf-8')))

	elif ans == '0':
		#eixt

		cl.close()
		sys.exit()
	else:
		print('Invalid input')
