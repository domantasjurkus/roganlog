run:
	FLASK_APP=roganlog_flask FLASK_ENV=development flask run

dump:
	python3 roganlog_flask/data/scrapped/pickle_dump.py

init:
	make dump
	FLASK_APP=roganlog_flask FLASK_ENV=development flask init-db
