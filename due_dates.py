import os
import sys
import time
import re

def add(filename):
	os.system('clear')
	c = ''

	sys.stdout.write("(b) Go back to menu\n")
	sys.stdout.write("(q) Quit\n")

	content = ""
	with open(filename, "r") as f:
		content = f.read()

	sys.stdout.write("\nName of Task: ")
	c = input()
	if c == 'b' or c == 'B': return
	elif c == 'q' or c == 'Q': sys.exit(0)
	content = content + '_'.join(c.split()) + ' '

	sys.stdout.write("\nDue Date (MM/DD/YYYY HH:mm): ")
	c = input()
	if c == 'b' or c == 'B': return
	elif c == 'q' or c == 'Q': sys.exit(0)
	t = str(time.mktime(time.strptime(c, "%m/%d/%Y %H:%M")))
	content = content + t + '\n'

	with open(filename, "w") as f:
		f.write(content)	


def task_time(task):
	d = time.localtime(task[0])
	t = time.localtime()
	inc = False

	# minutes remaining
	mins = d[4] - t[4]
	if mins < 0:
		mins += 60
		inc = True

	# hours remaining
	hrs = d[3] - t[3]
	if inc:
		hrs -= 1
		inc = False
	if hrs < 0:
		hrs += 24
		inc = True

	# days remaining
	dys = d[7] - t[7]
	if inc: dys -= 1

	r = ""
	if dys < 0: r = "OVERDUE!!!\n"
	else: r = '| ' + str(dys) + " Days " + str(hrs) + " Hours " + str(mins) + " Minutes\n"

	sys.stdout.write(str(task[1]))
	pad = 36 - len(str(task[1]))
	while pad >= 0:
		sys.stdout.write(' ')
		pad -= 1
	sys.stdout.write(r)


def list(filename):
	os.system('clear')
	c = ''

	while(True):
		with open(filename, "r") as f:
			tasks = []

			for line in f:
				task = line.split()
				tasks.append((float(task[1]), task[0]))

			tasks.sort()
			if len(tasks) <= 3:
				sys.stdout.write("Top:\n")
				for task in tasks[:]:
					task_time(task)

			else:
				sys.stdout.write("Top:\n")
				for task in tasks[:3]:
					task_time(task)

				sys.stdout.write("_________________________\n")
				for task in tasks[3:]:
					task_time(task)

		sys.stdout.write("\n(b) Go back to menu\n")
		sys.stdout.write("(q) Quit\n")

		c = input()
		if c == 'b' or c == 'B': break
		elif c == 'q' or c == 'Q': sys.exit(0)
		
		os.system('clear')


def rmv(filename, flag):
	os.system('clear')
	content = ""
	
	if flag == '1' or flag == '3':
		c = ''
		e = False

		if flag == '1': sys.stdout.write("Name of Task (No Spaces): ")
		else: sys.stdout.write("Are you sure you want to remove all tasks (press y to continue)")

		c = input()
		if flag == '3' and c != 'y' and c != 'Y':
			return "Operation Cancelled."
	
	if flag == '1' or flag == '2':
		with open(filename, "r") as f:
			for line in f:
				task = line.split()
				if flag == '1' and task[0] == c: e = True
				elif flag == '2' and float(task[1]) < time.mktime(time.localtime()): pass
				else: content = content + ' '.join(task) + '\n'

	with open(filename, "w") as f:
		f.write(content)

	if flag == '1' and e: return c + " was removed."
	elif flag == '1' and not e: return "Task does not exist."
	elif flag == '2': return "Past due tasks removed."
	return "All tasks removed."


def remove(filename):
	os.system('clear')
	c = ''

	while(True):
		sys.stdout.write("What would you like to do?\n")
		sys.stdout.write("(1) Remove One Task\n")
		sys.stdout.write("(2) Remove Past Due Tasks\n")
		sys.stdout.write("(3) Remove All Tasks\n")
		sys.stdout.write("(b) Go back to menu\n")
		sys.stdout.write("(q) Quit\n")
		if c == 'strawberry yogurt': sys.stdout.write("\nInvalid Input\n")
		else: sys.stdout.write('\n' + c + '\n')

		c = input()
		if c == '1' or c == '2' or c == '3': c = rmv(filename, c)
		elif c =='b' or c == 'B': break
		elif c == 'q' or c == 'Q': sys.exit(0)
		else: c = 'strawberry yogurt'

		os.system('clear')


if __name__ == '__main__':
	os.system('clear')
	filename = "tasks.txt"
	c = ''

	while(True):
		sys.stdout.write("Menu:\n\n")
		sys.stdout.write("(a) Add\n")
		sys.stdout.write("(l) List\n")
		sys.stdout.write("(r) Remove\n")
		sys.stdout.write("(q) Quit\n")
		if c == 'strawberry yogurt': sys.stdout.write("\nInvalid Input\n")
		else: sys.stdout.write("\n\n")

		c = input()
		if c == 'a' or c == 'A': add(filename)
		elif c == 'l' or c == 'L': list(filename)
		elif c == 'r' or c == 'R': remove(filename)
		elif c =='q' or c == 'Q': sys.exit(0)
		else: c = 'strawberry yogurt'
		
		os.system('clear')
