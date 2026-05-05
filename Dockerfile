FROM python:3.10-slim as base

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.10-slim

WORKDIR /app

COPY --from=base /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "App.py"]