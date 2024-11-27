INFECTION_DIR := ~/infection
NAME := stockholm.py
PYTHON_VENV := venv
TEST_FILES:= ${INFECTION_DIR}/test.txt ${INFECTION_DIR}/test.sql ${INFECTION_DIR}/test.mp3 ${INFECTION_DIR}/test.bad
REC_DIR:= ${INFECTION_DIR}/test_dir
REC_TEST_FILES:= ${REC_DIR}/test.txt ${REC_DIR}/test.sql ${REC_DIR}/test.mp3 ${REC_DIR}/test.bad

all:
	@echo "Run \"make configure\", \"source venv/bin/activate\" and then \"python3 stockholm.py\""
	@echo ":D"

configure:
	@mkdir -p ${INFECTION_DIR} ${REC_DIR}
	@touch ${TEST_FILES} ${REC_TEST_FILES}
	@python3 -m venv ${PYTHON_VENV}
	@${PYTHON_VENV}/bin/pip3 install -r requirements.txt

fclean:
	@rm -rf ${PYTHON_VENV} ${INFECTION_DIR} key

re: clean configure
