venv:
	virtualenv venv
	./venv/bin/pip3 install -r requirements.txt

run: venv
	./venv/bin/python3 src/main.py

rootpw:
	@cat /dev/urandom | \
		tr -dc 'a-zA-Z0-9' | \
		fold -w 32 | \
		head -n 1 | \
		tee ./config/rootpw.txt
