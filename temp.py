from BlueSmoke import db
from BlueSmoke.models import Semesters

att = Semesters(sem='Fall 2017')
db.session.add(att)
db.session.commit()
