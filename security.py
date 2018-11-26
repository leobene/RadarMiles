from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
	"""
	Function that gets called when user calls the /auth endpoint with
	their username and password.
	:param username: username in string format.
	:param password: un-encrypted password in string format.
	:return: A UserModel object if authentication was sucessful, None otherwise.
	"""
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	"""
	Function that gets called when user has already authenticded, and Flask-JWT
	verified their autorization header is correct.
	:param username: username in string format.
	:return: A UserModel object.
	"""
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)