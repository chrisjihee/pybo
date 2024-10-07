import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# print(f"BASE_DIR={BASE_DIR}")
# print(f"SQLALCHEMY_DATABASE_URI={SQLALCHEMY_DATABASE_URI}")
