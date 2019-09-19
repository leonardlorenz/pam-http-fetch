venv:
	virtualenv venv
	./venv/bin/pip3 install -r requirements.txt

run:
	./venv/bin/python3 src/main.py
