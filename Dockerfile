FROM python:3

WORKDIR /usr/src/app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

CMD [ "python", "./backend/manage.py runserver" ]