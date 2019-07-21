#Todo Rest Automation

##Requirements
>###Development environment
> - Python version: 2.7.12

>###Python external libraries
> - pytest | 5.0.1 | _Purpose: Testing framework_
> - pytest-html |1.21.1| _Purpose: Html reporter for test_
> - requests |2.22.0| _Purpose: Rest client for api_

####Run tests

> - Open windows terminal
> - CD to root directory of the project 
> - Activate virtual environment for windows os
> `venv\scripts\activate`

> Execute tests `python -m pytest -v  tests/ --html=report.html`
> Execute tests with log enabled `python -m pytest -v  --log-file=test.log  tests/ --html=report.html`

####View test report
>Open `report.html` file to see test run details
