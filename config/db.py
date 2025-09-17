from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:mysql25@localhost:3309/userfastapi")

meta_data = MetaData()