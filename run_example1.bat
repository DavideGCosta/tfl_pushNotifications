@echo off
:: Batch file for running a Python script in a virtual environment

:: Change directory to the directory where the batch file resides
cd %~dp0

:: Activate the virtual environment - delete row if you want to run in global env
call venv\Scripts\Activate

:: Run the Python script with the specified argument
:: In this case, it runs the second example from examples.py
python examples.py 1

:: Deactivate the virtual environment
deactivate
