
import sqlalchemy.orm
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings


Base = declarative_base()
DB_ENGINE = settings.DATABASES['default']['ENGINE'].rpartition('.')[-1]


if DB_ENGINE == 'postgresql_psycopg2':
    connection_string = ('postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}').format(**settings.DATABASES['default'])
else:
    connection_string = ('{0}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}').format(DB_ENGINE, **settings.DATABASES['default'])

if DB_ENGINE == 'mysql':
    connection_string += '?charset=utf8'


metaData = sa.MetaData()
# engine = sa.create_engine('mysql://root:test@localhost/djalchemy', echo=True)
engine = sa.create_engine(connection_string, pool_recycle=1800, pool_size=200, max_overflow=-1)
Session = sa.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)