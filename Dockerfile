FROM python:3.7.4 AS tmp-build-env
WORKDIR /app
ADD . /app
RUN pip3 install --upgrade pip && pip3 install  --no-cache-dir -r ./requirements.txt

FROM python:3.8.7-alpine3.12
COPY --from=tmp-build-env /app /app
COPY --from=tmp-build-env /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

EXPOSE 8000

CMD ["python3", "Q4_fast_api_server.py"]
