# IMPACTANALYZER
## Description
A tool that analyzes pull requests created by the development team to predict which ones are likely to break the Test Automation System (TAS).

## Usage

Command line:
```
python main.py -pt "webHMI fixes"
python main.py -pt "Move new event variables to audit data"
```

Flask application from command line:
```
set FLASK_PERSONAL_ACCESS_TOKEN="1234567890"
flask run
```