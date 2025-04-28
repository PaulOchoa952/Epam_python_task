# Define the Python interpreter
PYTHON = python
PIP = $(PYTHON) -m pip

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available commands:"
	@echo "  make install      Install all required dependencies"
	@echo "  make lint         Run Ruff for code linting"
	@echo "  make test         Run Pytest for unit tests"
	@echo "  make clean        Clean up cache and temporary files"
	@echo "  make dict         Run the dictionary example (Add/Lookup entries)"
	@echo "  make lookup       Lookup entries in the dictionary"
	@echo "  make spend        Run the spending/tax calculation example"
	@echo "  make array        Run the letter concatenation example"

# Install dependencies
install:
	@echo "Installing required dependencies..."
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; else echo "No requirements.txt found!"; fi

# Lint Python code using Ruff
lint:
	@echo "Running Ruff linting on project files..."
	ruff check .

# Run tests using Pytest
test:
	@echo "Running tests using Pytest..."
	PYTHONPATH=. $(PYTHON) -m pytest

# Clean Python cache and temporary files
clean:
	@echo "Cleaning Python cache and temporary files..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Run the dictionary example with add options
dict:
	@echo "Running the dictionary example..."
	$(PYTHON) -c "from dictionary_task import Dictionary; d = Dictionary(); d.run()

# Run the spending/tax calculation example
spend:
	@echo "Running the spending/tax calculation example..."
	$(PYTHON) -c "from spend_task import add_item; add_item()"

# Run the nth letter array concatenation example
array:
	@echo "Running the nth letter concatenation array example..."
	$(PYTHON) -c "from array_task import get_the_word; get_the_word()"