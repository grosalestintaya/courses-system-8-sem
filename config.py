#zfrom dotenv import load_dotenv
#import os

#load_dotenv()

#user = os.environ["MYSQL_USER"]
#password = os.environ["MYSQL_PASSbbWORD"]
#host = os.environ["MYSQL_HOST"]
#database = os.environ["MYSQL_DATABASE"]
DATABASE_CONNECTION_URI = f'mysql+pymysql://root:@localhost/dbexamen'

#DATABASE_CONNECTION_URI = f'mysql+pymysql://admin:76668813g@examencloud.cbu56rel5olk.us-east-1.rds.amazonaws.com/dbexamen'
print(DATABASE_CONNECTION_URI)
# DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}/{database}'
# print(DATABASE_CONNECTION_URI)

