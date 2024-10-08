import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

print("=" * 80)
print(f"BASE_DIR={BASE_DIR}")
print(f"SQLALCHEMY_DATABASE_URI={SQLALCHEMY_DATABASE_URI}")
print(f"TEMPLATE_FOLDER={TEMPLATE_FOLDER}")
print(f"STATIC_FOLDER={STATIC_FOLDER}")
print("=" * 80)
