"""from flask_bcrypt import Bcrypt

password = 'secret'

bcrypt = Bcrypt()
hashed_password = bcrypt.generate_password_hash(password)

print(bcrypt.check_password_hash(hashed_password, 'wrong'))"""

from werkzeug.security import generate_password_hash, check_password_hash
password = 'secret'
hashed_pass = generate_password_hash(password)

print(hashed_pass)
print(check_password_hash(hashed_pass, 'wrong'))