import pytest

from laika.db import HackerspaceConfig, Session


@pytest.fixture
def db_session():
    with Session.begin() as session:
        yield session


@pytest.fixture
def hs_is_open(db_session):
    try:
        return db_session.query(HackerspaceConfig).filter(HackerspaceConfig.key == "is_open").one()
    except Exception:
        setting = HackerspaceConfig(key="is_open", value="")
        db_session.add(setting)
        db_session.commit()
