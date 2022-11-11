from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    def __init__(self,title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Book.query.all()

    def __repr__(self) -> str:
        return f"Title: {self.title}"