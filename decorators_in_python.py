user = {
	'name' : 'asish',
	'access_level' : 'admin'
}


def user_has_permission(func):
	def inside_func():
		'''
		Hola
		'''
		if user.get('access_level') == 'admin':
			return func()
	return inside_func


@user_has_permission
def my_func():
	return "Password of admin is 1234"
	'''
	Hye
	'''

#my_secure_func = user_has_permission(my_func())


print(my_func())
print(my_func.__name__)
print(my_func.__doc__)