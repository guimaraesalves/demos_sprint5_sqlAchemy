from app.configs.database import db
from sqlalchemy import Column, Integer, String, Date, DateTime

class CallRecord(db.Model):

    # forçar o nome da tabela
    __tablename__ = 'call_records'

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(Date)
    end_time = Column(Date)