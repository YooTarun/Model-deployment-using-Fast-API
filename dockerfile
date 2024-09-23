FROM python:3.9-slim

WORKDIR /model

COPY . /model

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:model", "--host", "0.0.0.0", "--port", "8000"]