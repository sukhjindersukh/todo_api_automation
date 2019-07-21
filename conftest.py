"""This is just an empty file in order to pytest work properly for internal imports """


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print ("Test started", item)


def pytest_runtest_teardown(item):
    print ("Test finished", item)
