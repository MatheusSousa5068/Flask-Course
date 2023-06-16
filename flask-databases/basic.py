from models import db, Pet, Owner, Toy

rufus = Pet('Rufus')
fido = Pet('Fido')

db.session.add_all([rufus, fido])
db.session.commit()

print(Pet.query.all())


rufus = Pet.query.filter_by(name='Rufus').first()
jose = Owner('Jose', rufus.id)
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

rufus = Pet.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()



