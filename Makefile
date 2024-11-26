INFECTION_DIR := infection
NAME := stockholm.py
PYTHON_VENV := venv

all:
	@echo "Run makeconfigure and then python3 stockholm.py"
	@echo ":D"

configure:
	@mkdir -p ~/${INFECTION_DIR}
	@python3 -m venv ${PYTHON_VENV}
	@${PYTHON_VENV}/bin/pip3 install -r requirements.txt

fclean:
	@rm -rf ${PYTHON_VENV} ~/${INFECTION_DIR}

re: clean configure
