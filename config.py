import os

db_host = os.environ.get("DB_HOST", default="192.168.150.136")
db_name = os.environ.get("DB_NAME", default="sample")
db_user = os.environ.get("DB_USERNAME", default="mohannad")
db_password = os.environ.get("DB_PASSWORD", default="")
db_port = os.environ.get("DB_PORT", default="5432")

SQLALCKEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"