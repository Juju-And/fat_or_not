from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def calculate_bmi(self):
        return self.weight / self.height * self.height

    def check_bmi(self):
        # < 18, 5 – niedowagę
        # 18, 5–24, 99 – wartość
        # prawidłową
        # ≥ 25, 0 – nadwagę
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "underweight"
        elif bmi > 25:
            return "overweight"
        else:
            return "ok"

    def __repr__(self):
        return '<User {}>'.format(self.id)
