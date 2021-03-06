from sqlalchemy import create_engine
engine = create_engine('postgresql://steve:s@localhost:5432/test')

# # pyodbc
# engine = create_engine('mssql+pyodbc://scott:tiger@mydsn')

# # pymssql
# engine = create_engine('mssql+pymssql://scott:tiger@hostname:port/dbname')

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
    )

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
    )

ins = users.insert().values(name='jack', fullname='Jack Jones')
print(str(ins), ins.compile().params )

conn = engine.connect()
print(conn)

