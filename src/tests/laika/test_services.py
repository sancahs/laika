import pytest

from laika.db import HackerspaceConfig, Session
from laika.services import CloseHackerspace, OpenHackerspace


@pytest.fixture
def db_session():
    with Session.begin() as session:
        yield session


@pytest.fixture
def hs_config(db_session):
    try:
        return db_session.query(HackerspaceConfig).filter(HackerspaceConfig.key == "is_open").one()
    except Exception:
        setting = HackerspaceConfig(key="is_open", status="")
        db_session.add(setting)
        db_session.commit()


def test_open_hackerspace():
    assert OpenHackerspace().open() == "open"


def test_close_hackerspace():
    assert CloseHackerspace().close() == "closed"
