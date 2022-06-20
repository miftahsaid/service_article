from sqlalchemy import create_engine,MetaData

user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'article'

engine = create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database
		))
meta = MetaData()
conn = engine.connect()
