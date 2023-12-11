
FROM python:3.11.7-slim

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml

RUN pip install poetry

RUN poetry install --all-extras --no-dev 

COPY ./src /app/src

VOLUME ./db/db.json /app/src/db/db.json

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000"]