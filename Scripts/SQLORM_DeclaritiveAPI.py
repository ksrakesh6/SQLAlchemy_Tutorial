"""
Declaritive Way of connecting to Postgresql using SQLAlchemy ORM
"""
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To Spin up a session "
session = sessionmaker()
engine_pg = db.create_engine(r'postgresql://aadhi@localhost:3967/dvdrental')
session.configure(bind=engine_pg)
pg_session = session()
base = declarative_base()


class actor(base):
    " Class Model for the table Actor"
    __tablename__ = 'actor'
    actor_id = db.Column(db.Integer,
                         primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    last_update = db.Column(db.DateTime)

    def __repr__(self):
        "String Representation"
        return ("Actor_id : {0} Name : {1} Updated on : {2}".format(
                self.actor_id,
                ' '.join([self.first_name, self.last_name]),
                self.last_update))


# To fetch the 1st row of data
print(pg_session.query(actor).first())
