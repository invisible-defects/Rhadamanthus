from sqlalchemy import Table, Column, Integer, String, MetaData
import sqlalchemy as sa

class Citizen(object):
    def __init__(self, name, carma):
        self.name = name
        self.carma = carma

    def __repr__(self):
        return "<User('%s','%s')>" % (self.name, self.carma)

engine = sa.create_engine('sqlite:///radamant_action.db')

metadata = MetaData()

deads_table = Table('Dead_citizens', metadata,
    Column('name', String, primary_key=True),
    Column('carma', Integer)
)

