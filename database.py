"""
Document stuff
"""
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from sqlalchemy.ext.declarative import declarative_base


# TODO: Connections string
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine("mysql://scott:tiger@localhost/test",
                       pool_recycle=3600,
                       isolation_level="READ UNCOMMITTED")
Base = declarative_base()

Table('Category', metadata,
      Column('data', String(32)),
      mysql_engine='InnoDB',
      mysql_charset='utf8',
      mysql_key_block_size="1024"
     )
class Category(Base):
    """

    """
    __tablename__ = 'Category'
    category_id = Column(Integer(), primary_key=True)
    category = Column(VARCHAR(15))

# TODO: Create classes
class Notification(Base):
    """

    """
    __tablename__ = 'Notification'
    Column('notification_id', SMALLINT, primary_key=True),
    category = Column(VARCHAR(25))
    incident_number = Column(VARCHAR(15))
    customer_impact = Column(VARCHAR(50))
    content = Column(TEXT())
    affected_carriers = Column(VARCHAR(50))
    start_date = Column(DATETIME())
    end_date = Column(DATETIME())
    expected_end_date = Column(DATETIME())
    ForeignKeyConstraint(['category'], ['Category.category_id']),
    autoload=True)


class NotificationStats(Base):

    __tablename__ = 'NotificationStats'
    notification_stat_id = Column(Integer, primary_key=True)
    notification_category = Column(VARCHAR())
    avg_notification_lag = Column(Integer())
    min_notification_lag = Column(Integer())
    max_notification_lag = Column(Integer())
    avg_duration = Column(Integer())
