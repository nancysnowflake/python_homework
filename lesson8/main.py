from Functions import *
from Constants import *


while True:
	print(HELLO_TEXT)
	print(CREATE_USER_TEXT)
	print(FIND_USER_INDEX_TEXT)
	print(FIND_USER_NAME_TEXT)
	print(DELETE_USER_INDEX_TEXT)
	print(EXIT_TEXT)

	n = int(input())
	if n == 1:
		name = input(INPUT_USER_NAME_TEXT)
		age = int(input(INPUT_USER_AGE_TEXT))
		sex = input(INPUT_USER_SEX_TEXT)
		if name == '':
			print(BAD_NAME_TEXT)
		elif age < 0:
			print(BAD_AGE_TEXT)
		elif sex != 'М' and sex != 'Ж':
			print(BAD_SEX_TEXT)
		else:
			index = add_user(name, age, sex)
			print(CREATED_USER_INDEX_TEXT, index)
	elif n == 2:
		index = int(input(FIND_INDEX_INPUT_TEXT))
		name, age, sex = find_user_index(index)
		if name == False:
			print(NOT_FOUND_USER_TEXT)
		else:
			print(name, age, sex)
	elif n == 3:
		name = input(FIND_NAME_INPUT_TEXT)
		name, age, sex = find_user_name(name)
		if name == False:
			print(NOT_FOUND_USER_TEXT)
		else:
			print(name, age, sex)
	elif n == 4:
		index = int(input(FIND_INDEX_INPUT_TEXT))
		deleted = delete_user(index)
		if deleted == False:
			print(NOT_FOUND_USER_TEXT)
		else:
			print(DELETED_TEXT)
	elif n == 5:
		break
	else:
			print(BAD_COMMAND_TEXT)




