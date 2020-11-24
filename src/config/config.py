import os

DB_HOST=os.environ.get('DB_HOST','127.0.0.1')
DB_NAME=os.environ.get('DB_NAME','ginger_db')
DB_USER=os.environ.get('DB_USER','root')
DB_PASSWORD=os.environ.get('DB_PASSWORD','')

SECRET_KEY=os.environ.get('SECRET_KEY','jwkbrQoHZLky6hWv0UeEugArZZn$dccmymmBb$vl3yE0tYincM6hyKgwW4zY59v')
DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)