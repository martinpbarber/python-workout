VENV := .venv
VENV_ACTIVATE := . $(VENV)/bin/activate

.PHONY: test
test: venv format lint
	$(VENV_ACTIVATE) && python -m pytest tests -v --cov=src/ --cov-report term-missing

.PHONY: lint
lint: venv
	$(VENV_ACTIVATE) && pylint src/ tests/


.PHONY: format
format: venv
	$(VENV_ACTIVATE) && black src/ tests/

.PHONY: venv
venv: $(VENV)/bin/activate 
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(VENV_ACTIVATE) && pip install --upgrade pip
	$(VENV_ACTIVATE) && pip install -r requirements.txt

.PHONY: type
type: venv
	$(VENV_ACTIVATE) && mypy src/ tests/

.PHONY: clean
clean:
	rm -rf $(VENV)/
	rm -rf .pytest_cache/
	find . -name '__pycache__' -exec rm -fr {} +
