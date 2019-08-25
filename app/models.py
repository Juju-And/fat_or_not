from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def calculate_bmi(self):
        return round(self.weight / ((self.height/100) * (self.height/100)), 2)

    def check_bmi(self):
        # < 18, 5 – niedowagę
        # 18, 5–24, 99 – wartość
        # prawidłową
        # ≥ 25, 0 – nadwagę
        bmi = self.calculate_bmi()
        if bmi <= 18.5:
            return bmi, 'Idź coś zjeść'
        elif bmi > 25:
            return bmi, 'Schudnij grubasie'
        else:
            return bmi, 'Waga w normie'

    def __repr__(self):
        return '<User {}>'.format(self.id)
