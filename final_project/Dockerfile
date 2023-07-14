FROM python:alpine3.7
COPY . \app
WORLDIR \app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]