FROM python:3.11.6
WORKDIR /srv
COPY . /srv
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["python","app.py"]