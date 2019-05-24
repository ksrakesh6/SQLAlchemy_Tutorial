"""
Declaritive Way of connecting to Postgresql using SQLAlchemy ORM
Example to print SQL query along with the Data
"""
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To Spin up a session "
session = sessionmaker()
engine_pg = db.create_engine(r'postgresql://aadhi@localhost:3967/dvdrental',
                             echo=True)
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
        return ("\nActor_id : {0} Name : {1} Updated on : {2}\n".format(
                self.actor_id,
                ' '.join([self.first_name, self.last_name]),
                self.last_update))


# To fetch the 1st row of data - Select single column in SQL
tb_data = pg_session.query(actor)
print(tb_data.first().first_name)

# To Filter Data in the table- where in SQL
print(tb_data.filter(actor.first_name == 'Julia').all())

# To Filter Data by checking contains - Like % in SQL
print(tb_data.filter(actor.first_name.like('%Chr%')).all())
print(tb_data.filter(actor.first_name.contains('Chr')).all())
