NEW_PYTHONPATH="`pwd`/src:$(PYTHONPATH)"

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

clean:
	@find . -name "*.pyc" -delete

tornado: clean
	@echo "The tornado is coming..."
	PYTHONPATH="$(NEW_PYTHONPATH)" python -m servers.tornado_server
