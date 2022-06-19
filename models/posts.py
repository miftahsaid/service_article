from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,VARCHAR,TIMESTAMP,Text
from config.db import meta


post_ = Table(
    'posts',meta,
    Column('id',Integer, primary_key=True),
    Column('Title',VARCHAR(200)),
    Column('Content',Text),
    Column('Category',VARCHAR(100)),
    Column('Created_date',TIMESTAMP),
    Column('Updated_date',TIMESTAMP),
    Column('Status',VARCHAR(100))
)
