from basic import db, User

# Create
matheus = User('Matheus', 18)
pablo = User('Pablo', 80)
marcela = User('Marcela', 20)
db.session.add_all([matheus, pablo, marcela])

db.session.commit()


# Read All
all_users = User.query.all()
print(all_users)

# Read by ID
user_one = User.query.get(1)
print(user_one.name)

# Read with filters
user_matheus = User.query.filter_by(name="Matheus")
print(user_matheus.all())



# Update
first_user = User.query.get(3)
first_user.age = 22
db.session.add(first_user)
db.session.commit()

# Delete
first_user = User.query.get(1)
db.session.delete(first_user)
db.session.commit()

print(User.query.all())