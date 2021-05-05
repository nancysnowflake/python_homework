from Constants import *

def add_user(name, age, sex):
	USER_DICT['name'].append(name)
	USER_DICT['age'].append(age)
	USER_DICT['sex'].append(sex)
	return len(USER_DICT['name']) - 1

def delete_user(index):
	if index < 0 or index >= len(USER_DICT['name']):
		return False
	del USER_DICT['name'][index]
	del USER_DICT['age'][index]
	del USER_DICT['sex'][index]
	return True

def find_user_index(index):
	if index < 0 or index >= len(USER_DICT['name']):
		return False, False, False
	return USER_DICT['name'][index], USER_DICT['age'][index], USER_DICT['sex'][index]

def find_user_name(name):
	i = 0
	while i < len(USER_DICT['name']):
		if USER_DICT['name'][i] == name:
			return USER_DICT['name'][i], USER_DICT['age'][i], USER_DICT['sex'][i]
		i += 1
	return False, False, False