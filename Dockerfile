FROM python:3.7.9-slim AS tmp-build-env
COPY requirements.txt .
RUN pip3 install  --no-cache-dir --target=/app/deps -r requirements.txt

FROM python:3.7.9-slim
WORKDIR /app
COPY . .
COPY --from=tmp-build-env /app/deps /app/deps
ENV PYTHONPATH=/app/deps:$PYTHONPATH

EXPOSE 8080
CMD ["python3", "Q4_fast_api_server.py"]
