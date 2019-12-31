from app import db
from app.models import Rate

db.create_all()

add_rate_gsm = Rate(type_connect='GSM', price_per_minute=15)
add_rate_cdma = Rate(type_connect='CDMA', price_per_minute=20)
add_rate_lte = Rate(type_connect='LTE', price_per_minute=25)

db.session.add(add_rate_gsm)
db.session.add(add_rate_cdma)
db.session.add(add_rate_lte)
db.session.commit()
