.PHONY: test dashboard all
all: dashboard test
dashboard:
	PYTHONPATH=src python src/build_dashboard.py
test:
	PYTHONPATH=. pytest -q
