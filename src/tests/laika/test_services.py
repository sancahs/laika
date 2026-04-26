import pytest

from laika.services import CloseHackerspace, GetHackerspaceOpenStatus, OpenHackerspace


@pytest.mark.usefixtures("hs_is_open")
def test_open_hackerspace():
    assert OpenHackerspace().open() == "open"


@pytest.mark.usefixtures("hs_is_open")
def test_close_hackerspace():
    assert CloseHackerspace().close() == "closed"


def test_get_hackerspace_open_status_open(db_session, hs_is_open):
    hs_is_open.value = "open"
    db_session.commit()

    assert GetHackerspaceOpenStatus().get() == {"is_open": True, "status": "open"}


def test_get_hackerspace_open_status_closed(db_session, hs_is_open):
    hs_is_open.value = "closed"
    db_session.commit()

    assert GetHackerspaceOpenStatus().get() == {"is_open": False, "status": "closed"}
