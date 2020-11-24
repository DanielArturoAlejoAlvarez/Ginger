import os

DB_USER=os.environ.get('DB_USER','root')
DB_PASSWORD=os.environ.get('DB_PASSWORD','Br1tney$2=')
DB_HOST=os.environ.get('DB_HOST','127.0.0.1')
DB_NAME=os.environ.get('DB_NAME','ginger_db')
SECRET_KEY=os.environ.get('SECRET_KEY','RXuwGX6syfZoZ4gi$y8fbkEtDgknmsAcpUyVQRmo')

DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
