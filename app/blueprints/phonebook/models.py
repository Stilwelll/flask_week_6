from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Item | {self.itemname}>"

    def __str__(self):
        return f"{self.itemname}"

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in {'itemname'}:
                setattr(self, key, value)
            db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #def upload_to_cloudinary(self, file_to_upload):