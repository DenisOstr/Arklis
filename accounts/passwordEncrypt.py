from werkzeug.security import generate_password_hash, check_password_hash

def checker(hash, pasw):
	c = 0

	for x in str(hash[c]['password']):
		if check_password_hash(x, pasw):
			break
			return True
		else:
			return False
		c += 1


def hasher(pasw):
	hashp = generate_password_hash(pasw)

	if hashp is not None:
		return hashp
	else:
		return 'unable to hash'