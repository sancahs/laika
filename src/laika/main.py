from fastapi import FastAPI

from laika.services import CloseHackerspace, GetHackerspaceOpenStatus, OpenHackerspace

app = FastAPI()


@app.get("/status")
def status():
    return {"api_status": True, "db_status": False}


@app.get("/status/space-api")
def status_space_api():
    return {
        "api_compatibility": ["15"],
        "space": "Sanca Hackerspace",
        "logo": "https://hackerspace.sanca.log.br/assets/img/logo-sanca-hackerspace.png",
        "url": "https://hackerspace.sanca.log.br",
        "location": {
            "address": "R. Dona Ana Prado, 18 - Vila Prado, São Carlos - SP, 13574-031",
            "lat": -22.022418551785602,
            "lon": -47.89997796075527,
            "country_code": "BR",
            "timezone": "America/Sao_Paulo",
            "hint": "A entrada fica em outra rua. É o portão laranja em frente a loja de água 'IBIRÁGUA'",
        },
        "state": {
            "open": False,
            "lastchange": 1776828925.712378,
        },
        "contact": {
            "telegram": "@sanca_hs"
        },
        "issue_report_channels": ["telegram"],
        "projects": ["https://github.com/sancahs"],
    }


@app.post("/v1/hackerspace/open")
def open_hackerspace():
    status = OpenHackerspace().open()
    return {"is_open": True, "status": status}


@app.post("/v1/hackerspace/close")
def close_hackerspace():
    status = CloseHackerspace().close()
    return {"is_open": False, "status": status}


@app.get("/v1/hackerspace/is-open")
def get_hackerspace_open_status():
    return GetHackerspaceOpenStatus().get()
