# Todo Rest Automation

## Requirements
> ### Development environment
> - Python version: 2.7.12

> ### Python external libraries
> - pytest | 5.0.1 | _Purpose: Testing framework_
> - pytest-html |1.21.1| _Purpose: Html reporter for test_
> - requests |2.22.0| _Purpose: Rest client for api_

#### Run tests

> - Open windows terminal
> - CD to root directory of the project 
> - Activate virtual environment for windows os
> `venv\scripts\activate`

> Execute tests `python -m pytest -v  tests/ --html=report.html`

> Execute tests with log enabled ```python -m pytest -v  --log-file=test.log  tests/ --html=report.html```

#### View test report
>Open `report.html` file to see test run details


#### Tests delails  
*Total tests:  8*
---
*Passing tests*
> 1. Add a new task
> 2. Get all tasks
> 3. Get a single task with id
> 4. Update a task
> 5. Complete a task
> 6. Delete a task

*Failing tests*
> 1. Add a blank task
> 2. Add a task with wrong data
