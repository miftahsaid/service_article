from sqlalchemy import create_engine,MetaData

user = 'root'
password = '1'
host = '127.0.0.1'
port = 3306
database = 'db_'

engine = create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database
		))
meta = MetaData()
conn = engine.connect()
