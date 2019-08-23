from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def calculate_bmi(self):
        return self.weight / ((self.height/100) * (self.height/100))

    def check_bmi(self):
        # < 18, 5 – niedowagę
        # 18, 5–24, 99 – wartość
        # prawidłową
        # ≥ 25, 0 – nadwagę
        bmi = self.calculate_bmi()
        if bmi <= 18.5:
            return bmi, "underweight"
        elif 18.6 <= bmi <= 25:
            return bmi, "overweight"
        else:
            return bmi, "ok"

    def __repr__(self):
        return '<User {}>'.format(self.id)
