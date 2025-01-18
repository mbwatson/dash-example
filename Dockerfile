FROM python:3.14.0a4-slim-bookworm

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy in remaining code
COPY . ./

EXPOSE 8050

CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8050", "app:server"]
