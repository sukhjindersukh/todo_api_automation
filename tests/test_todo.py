import pytest
from datetime import datetime

from todo_api_automation.rest_util import Rest_Util

pytestmark = pytest.mark.sanity

rest = Rest_Util()


class Test_Todo:
    """ This is a test class to perform all sanity test for app's rest api """

    task_id = ''  # Hold task id to use in different tests
    summary = ''  # Hold summary to use in different tests

    def test_add_new_task(self):
        print ('Test: Verify new task should be created')
        now = datetime.now()
        task_summary = 'This is automation ' + str(now)
        Test_Todo.summary = task_summary
        res = rest.add_task(task_summary)
        assert res.status_code == 200

        Test_Todo.task_id = res.json().get('task_id')
        print ('Task created with id ' + Test_Todo.task_id)

        print ('Verify new task added with summary: ' + task_summary)
        res = rest.get_task(Test_Todo.task_id)
        dict = {}
        dict = res.json()

        assert dict.get('task') == task_summary

    def test_get_tasks(self):
        print('Test: Get all the tasks')
        res = rest.get_tasks()
        print('Verify status code should be 200')
        assert res.status_code == 200

        print ('Verify Content-Type should be "application/json"')
        assert res.headers.get('Content-Type') == 'application/json'

    def test_get_task_with_id(self):
        print ('Test: Verify task should be retrieved by using task id')
        res = rest.get_task(Test_Todo.task_id)

        print('Verify status code should be 200')
        assert res.status_code == 200

        print('Verify task retrieved as "write server mock"')
        dict = {}
        dict = res.json()

        assert dict.get('task') == Test_Todo.summary

    def test_update_task(self):
        print ('Test: Verify existing task can be updated')

        now = datetime.now()
        task_summary = 'This is updated summary ' + str(now)
        res = rest.update_task(Test_Todo.task_id, task_summary)

        assert res.status_code == 200

        task_id = res.json().get('task_id')
        print (task_id)

        print ('Verify task updated with new summary: ' + task_summary)
        res = rest.get_task(task_id)
        dict = {}
        dict = res.json()

        assert dict.get('task') == task_summary

    def test_complete_task(self):
        print ('Test: Verify existing task can not be updated whe using method post')
        res = rest.complete_task(Test_Todo.task_id)
        print ('Contents from post to update existing tasks using id: ' + Test_Todo.task_id)
        print ('Contents: ' + res.content)
        assert res.status_code == 405

    def test_delete_task(self):
        print ('Test: Verify existing task can be deleted')
        res = rest.delete_task(Test_Todo.task_id)
        assert res.status_code == 200

        print ('Verify task deleted ')
        res = rest.get_task(Test_Todo.task_id)
        dict = {}
        dict = res.json()
        assert len(dict.keys()) == 0

    if __name__ == '__main__':
        pytest.main()
