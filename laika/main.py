from fastapi import FastAPI

app = FastAPI()


@app.get("/status/space-api")
def status_space_api():
    return {
        "space": "Sanca Hackerspace",
        "api_compatibility": ["15"],
        "logo": "",
        "url": "https://hackerspace.sanca.log.br",
        "location": {
            "address": "",
            "lat": "",
            "lon": "",
        },
        "state": {
            "open": False,
        },
        "contact": {
            "telegram": "@sanca_hs"
        },
        "issue_report_channels": ["telegram"],
        "projects": ["https://github.com/sancahs"],
    }
