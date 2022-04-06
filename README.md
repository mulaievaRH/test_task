# Scrive test task
This project is responsible for the automated UI testing.


The test does the following:

 - Goes to https://staging.scrive.com/t/9221714692410699950/7348c782641060a9

 - Fills in the full name in the document.

 - Clickes on Next

 - Takes a screenshot of  confirmation modal.

 - Sign the document.

 - Verify that there is a text “Document signed” on the screen.

# Development

## Set Up Development
Create a virtualenv:

```
$ python3 -m venv --system-site-packages .venv

$ source .venv/bin/activate
```

Install following python dependencies:

```
$ pip3 install -r requirements.txt
```

## Usage

To ran script

```
pytest testcases/test_case.py --browser [OPTION]
Options:
    chrome         to run the test in the Chrome browser
    ff             to run the test in the FireFox browser

```
