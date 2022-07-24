
Installation
Install the following tools

Python
Python IDE (Pycharm etc.)
Python Pytest
Selenium
Adding Dependencies
Use the requirements.txt file to install all the dependencies required for this project using the following command.

cat requirements.txt | xargs -n 1 pip install
Running test suite
Use the following command to start the execution of python test-suite.

pytest -v -s File Path
pytest -v -s testCases/test_login.py

