from sqlalchemy import create_engine
from sqlalchemy.orm import mapped_column, sessionmaker, DeclarativeBase, Mapped

from laika.config import settings

engine = create_engine(settings.db_url)

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class HackerspaceConfig(Base):
    __tablename__ = "hackerspace_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(unique=True)
    value: Mapped[str]
