from laika.db import HackerspaceConfig, Session


class ToggleHackerspace:
    def update_is_open(self, session, value):
        session.query(HackerspaceConfig).filter(HackerspaceConfig.key == "is_open").update({"value": value})


class OpenHackerspace(ToggleHackerspace):
    def open(self):
        with Session.begin() as session:
            self.update_is_open(session, "open")
        return "open"


class CloseHackerspace(ToggleHackerspace):
    def close(self):
        with Session.begin() as session:
            self.update_is_open(session, "close")
        return "closed"


class GetHackerspaceOpenStatus():
    def get(self):
        with Session.begin() as session:
            is_open = session.query(HackerspaceConfig).filter(HackerspaceConfig.key == "is_open").one()
            return {"is_open": is_open.value == "open", "status": is_open.value}
