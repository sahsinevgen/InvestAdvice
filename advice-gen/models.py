import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = db.create_engine('sqlite:///../django-api/mysite/db.sqlite3')
connection = engine.connect()
Base = declarative_base()
meta = Base.metadata
Session = sessionmaker(bind=engine)
session = Session()

class Advices(Base):
    __table__ = db.Table("advice", meta, autoload_with=engine)

    @staticmethod
    def save_new(currency, operation_type, entry,
                stop_losses, take_profits, datetime, source):

        advice = Advices(currency=currency,\
                        operation_type=operation_type,\
                        entry=str(entry),\
                        datetime=datetime,\
                        source=source)

        session.add(advice)
        session.commit()
        session.refresh(advice)

        SLs = [StopLoss(entry=str(sl), advice_id=advice.id) for sl in stop_losses]
        TPs = [TakeProfit(entry=str(tp), advice_id=advice.id) for tp in take_profits]

        all_data = []
        all_data += SLs
        all_data += TPs

        session.add_all(all_data)
        session.commit()

class StopLoss(Base):
    __table__ = db.Table("stopLoss", meta, autoload_with=engine)

    # advice_id = db.Column("advice_id", db.ForeignKey('advice.id'))

class TakeProfit(Base):
    __table__ = db.Table("takeProfit", meta, autoload_with=engine)

    # advice_id = db.Column("advice_id", db.ForeignKey('advice.id'))
    # advice = db.orm.relationship("Advices", foreign_keys=[advice_id])

print(session.query(Advices).get(1))