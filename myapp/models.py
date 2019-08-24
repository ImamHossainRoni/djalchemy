from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from utils.db import Base

class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __int__(self, name):
        self.name = name

    def __repr__(self):
        return u"Language(%s)" % (self.name)