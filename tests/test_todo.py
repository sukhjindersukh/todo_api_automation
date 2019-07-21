import pytest
from datetime import datetime

from todo_api_automation.rest_util import Rest_Util
from todo_api_automation.log_util import Log_Util

# Initialize Rest_Util()
rest = Rest_Util()

# This class contains all tests as a sanity suite
pytestmark = pytest.mark.sanity


class Test_Todo:
    """ This is a test class to perform all sanity test for app's rest api """

    task_id = ''  # Hold task id to use in different tests
    summary = ''  # Hold summary to use in different tests

    def test_add_new_task(self):
        Log_Util().info('Test: Verify new task should be created')

        now = datetime.now()
        task_summary = 'This is automation ' + str(now)
        Log_Util().info('Create a task with summary: ' + task_summary)
        Test_Todo.summary = task_summary
        res = rest.add_task(task_summary, False)
        assert res.status_code == 200

        Test_Todo.task_id = res.json().get('task_id')
        Log_Util().info('Task created with id ' + Test_Todo.task_id)

        Log_Util().info('Verify new task added with summary: ' + task_summary)
        res = rest.get_task(Test_Todo.task_id)
        dict = {}
        dict = res.json()

        assert dict.get('task') == task_summary
        Log_Util().info('Test: PASS')

    def test_get_tasks(self):
        Log_Util().info('Test: Get all the tasks')

        res = rest.get_tasks()
        Log_Util().info('Verify status code should be 200')
        assert res.status_code == 200

        Log_Util().info('Verify Content-Type should be "application/json"')
        assert res.headers.get('Content-Type') == 'application/json'
        Log_Util().info('Test: PASS')

    def test_get_task_with_id(self):
        Log_Util().info('Test: Verify task should be retrieved by using task id')

        Log_Util().info('Task id: ' + Test_Todo.task_id)
        res = rest.get_task(Test_Todo.task_id)
        Log_Util().info('Verify status code should be 200')
        assert res.status_code == 200

        Log_Util().info('Verify task retrieved successfully with summary: ' + Test_Todo.summary)
        dict = {}
        dict = res.json()

        assert dict.get('task') == Test_Todo.summary
        Log_Util().info('Test: PASS')

    def test_update_task(self):
        Log_Util().info('Test: Verify existing task can be updated')

        now = datetime.now()
        task_summary = 'This is updated summary ' + str(now)
        Log_Util().info('Updated summary: ' + task_summary)
        res = rest.update_task(Test_Todo.task_id, task_summary)

        assert res.status_code == 200

        task_id = res.json().get('task_id')
        Log_Util().info('Task id retrieved: ' + task_id)

        Log_Util().info('Verify task updated with new summary: ' + task_summary)
        res = rest.get_task(task_id)
        dict = {}
        dict = res.json()
        assert dict.get('task') == task_summary
        Log_Util().info('Test: PASS')

    def test_complete_task(self):
        Log_Util().info('Test: Verify existing task can not be completed when using method post')

        Log_Util().info('Complete a task with id: ' + Test_Todo.task_id)
        res = rest.complete_task(Test_Todo.task_id)
        Log_Util().info('Contents from post to update existing tasks ')
        Log_Util().info('Contents: ' + res.content)
        assert res.status_code == 405
        Log_Util().info('Test: PASS')

    def test_delete_task(self):
        Log_Util().info('Test: Verify existing task can be deleted')

        Log_Util().info('Delete a task with id: '+ Test_Todo.task_id)
        res = rest.delete_task(Test_Todo.task_id)
        assert res.status_code == 200

        Log_Util().info('Verify task deleted ')
        res = rest.get_task(Test_Todo.task_id)
        dict = {}
        dict = res.json()
        assert len(dict.keys()) == 0
        Log_Util().info('Test: PASS')

    # This test will fail due wrong implementation in api.
    # Send wrong data type
    def test_verify_wrong_data_type(self):
        Log_Util().info('Test: Verify wrong type')

        Log_Util().info('Submit invalid data competed="INVALID" ')
        res = rest.add_task('', 'INVALID')
        task_id = res.json().get('task_id')
        Log_Util().info('Task id of a wrong data : ' + task_id)
        assert res.status_code != 200
        Log_Util().info('Test: PASS')

    # This test will fail due wrong implementation in api.
    # Sending summary and completed=Blank string, should not allow to create any record. Status should be 400
    def test_add_new__blank_task(self):
        Log_Util().info('Test: Verify blank task should not be created')

        res = rest.add_task('', True)
        task_id = res.json().get('task_id')
        Log_Util().info('Task id of a blank task: ' + task_id)
        assert res.status_code != 200
        Log_Util().info('Test: PASS')


if __name__ == '__main__':
    pytest.main()
