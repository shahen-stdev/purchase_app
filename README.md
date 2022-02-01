## Customer purchase simple app without authentication(was not required). 

## Install Env and Run
```bash
poetry install && \
poetry shell && \
alembic  revision --autogenerate -m"Initial migration" && \
uvicorn api.main:app
```