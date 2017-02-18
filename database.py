"""
Document stuff
"""
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://app:password@localhost:8889/EmailParser",
                       isolation_level="READ COMMITTED",
                       pool_recycle=8889,
                       # echo=True,
                       # convert_unicode=bool,
                       # pool_recycle=int,
                       # encoding=str,
                       # pool_size=int,
                       # poolclass=type,
                       # connect_args=dict,
                       # max_overflow=int,
                       # module=Tix.NoneType / new.module,
                       # strategy=str
                       )

engine.execute("CREATE DATABASE IF NOT EXIST test")
engine.execute("USE test")

metadata = MetaData()
Base = declarative_base()


class Category(Base):
    """

    """
    __table_name__ = 'Category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    category_id = Column(Integer(), primary_key=True)
    category_name = Column(String(15))


# TODO: Create classes
class Notification(Base):
    """

    """
    __table_name__ = 'Notification'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    Column('notification_id', Integer(), primary_key=True),
    category = Column(String(25))
    incident_number = Column(String(15))
    customer_impact = Column(String(50))
    content = Column(String(255))
    affected_carriers = Column(String(50))
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    expected_end_date = Column(DateTime())


class AffectedCarrier(Base):
    __table_name__ = 'Affected_Carrier'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    affected_carrier_id = Column(Integer, primary_key=True)
    notification_id = Column(Integer, ForeignKey="Notification.notification_id")
    carrier_id = Column(Integer, ForeignKey="Carrier.carrier_id")

    # user = relationship("User", back_populates="addresses")


class CarrierStats(Base):
    __table_name__ = 'Carrier_Stats'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    carrier_stat_id = Column(Integer, primary_key=True)
    carrier_name = Column(String())
    avg_notification_lag = Column(Integer())
    min_notification_lag = Column(Integer())
    max_notification_lag = Column(Integer())
    avg_expected_end_date_accuracy = Column(Integer())
    min_expected_end_date_accuracy = Column(Integer())
    max_expected_end_date_accuracy = Column(Integer())
    avg_planned_maintenance_duration = Column(Integer())
    min_planned_maintenance_duration = Column(Integer())
    max_planned_maintenance_duration = Column(Integer())
    avg_unplanned_maintenance_duration = Column(Integer())
    min_unplanned_maintenance_duration = Column(Integer())
    max_unplanned_maintenance_duration = Column(Integer())
    avg_service_degradation_duration = Column(Integer())
    min_service_degradation_duration = Column(Integer())
    max_service_degradation_duration = Column(Integer())


class NotificationStats(Base):
    __table_name__ = 'Notification_Stats'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    notification_stat_id = Column(Integer, primary_key=True)
    notification_category = Column(String())
    avg_notification_lag = Column(Integer())
    min_notification_lag = Column(Integer())
    max_notification_lag = Column(Integer())
    avg_expected_end_date_accuracy = Column(Integer())
    min_expected_end_date_accuracy = Column(Integer())
    max_expected_end_date_accuracy = Column(Integer())
    avg_planned_maintenance_duration = Column(Integer())
    min_planned_maintenance_duration = Column(Integer())
    max_planned_maintenance_duration = Column(Integer())
    avg_unplanned_maintenance_duration = Column(Integer())
    min_unplanned_maintenance_duration = Column(Integer())
    max_unplanned_maintenance_duration = Column(Integer())
    avg_service_degradation_duration = Column(Integer())
    min_service_degradation_duration = Column(Integer())
    max_service_degradation_duration = Column(Integer())


metadata.create_all(engine)
