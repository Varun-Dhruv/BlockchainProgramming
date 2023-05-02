.PHONY : install start stop restart status

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
start:
	@echo "Starting server..."
	@uvicorn index:app --reload
