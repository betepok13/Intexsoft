from app import db


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_connect = db.Column(db.String(4), nullable=False)
    price_per_minute = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return '<Rate {}>'.format(self.type_connect)


class Call(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_in = db.Column(db.String(13), nullable=False)
    number_target = db.Column(db.String(13), nullable=False)
    timestamp_start_call = db.Column(db.String(30), nullable=False)
    timestamp_end_call = db.Column(db.String(30), nullable=False)
    cost_call = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Call {}>'.format(self.id)
