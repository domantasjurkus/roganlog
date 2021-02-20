run_flask:
	FLASK_APP=roganlog_flask/app FLASK_ENV=development flask run

run:
	python3 roganlog_flask/app.py

init:
	python3 roganlog_flask/data/scrapped/pickle_dump.py
	FLASK_APP=roganlog_flask/app FLASK_ENV=development flask init-db
