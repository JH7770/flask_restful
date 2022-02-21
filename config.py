import os
db_info = {
    'user': 'root',
    'password': 'ansdjdhkd1',
    # 'host': os.environ.get('DB_HOST'),
    'host': "127.0.0.1",
    'port': 3306,
    'database': 'memo'
}
# DB URL
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db_info['user']}:{db_info['password']}@{db_info['host']}:{db_info['port']}/{db_info['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True

# JWT KEY
JWT_SECRET_KEY = "aaaaaaaaaaaaaaaaaaa"