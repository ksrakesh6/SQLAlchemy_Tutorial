"""Classical Mapping Example """

import sqlalchemy as db
from sqlalchemy import (
                        Table,
                        MetaData,
                        Column,
                        Integer,
                        String,
                        DateTime,
                        Sequence)
from sqlalchemy.orm import mapper

# Postgress Engine  Initiation
#    dialect://user@hostname:port/database

engine_pg = db.create_engine(r'postgresql://aadhi@localhost:3967/dvdrental')
metadata = MetaData()

# Table Definition of Actor in Postgres database

Actor = Table(
         'actor',
         metadata,
         Column('actor_id', Integer,
                Sequence('actor_actor_id_seq'),
                primary_key=True),
         Column('first_name', String(45)),
         Column('last_name', String(45)),
         Column('last_update', DateTime))

# Class for Table Actor each objects are each row in database


class actor(object):
    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update


# Map Database Actor table to class Actor
actor_mapper = mapper(actor, Actor)

# Select Actor with id  is 1
First_Actor = Actor.select(actor.actor_id == 1)
print(engine_pg.execute(First_Actor).fetchall())
