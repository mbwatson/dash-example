# Dash Example Application

## 🚧 Development


1. clone this repo & move into project dir
2. start virtual environment, `pipenv shell` ([Pipenv](https://pipenv.pypa.io/en/latest/) or other virtualenv management tool)
3. install deps, `pipenv install`
4. create an `.env` file with the following contents:
```
REACT_VERSION=18.2.0
```
5. start dev server, `python app.py`

```bash
$ python app.py
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app'
 * Debug mode: on
```

## 📦 Production

1. build image, `docker build -t dash-app .`
2. run container, `docker run --rm -p 80:8050 dash-app`
```bash
$ docker run --rm -p 80:8050 dash-app
[2025-01-16 15:28:42 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2025-01-16 15:28:42 +0000] [1] [INFO] Listening at: http://0.0.0.0:8050 (1)
[2025-01-16 15:28:42 +0000] [1] [INFO] Using worker: sync
[2025-01-16 15:28:42 +0000] [7] [INFO] Booting worker with pid: 7
# etc
```