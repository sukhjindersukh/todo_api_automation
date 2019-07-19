*Todo Rest Automation*

*Requirements*
>_Development environment_
> - Python version: 2.7.12
> - IDE: PyCharm version: 2018.3.7

>_Python external libraries_
> - pytest version: 5.0.1
> - pytest-html verion: 1.21.1
> - requests version: 2.22.0

*Run tests*

> - Open windows terminal
> - CD to root directory of the project 
> - Activate virtual environment for window
> `venv\scripts\activate`

> Execute all tests `python -m pytest --html=report.html`

> Execute with marker `python -m pytest -m sanity  --html=report.html`

*View test report*
>Open `report.html` file to see test run details
