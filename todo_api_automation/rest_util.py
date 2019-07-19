import requests
import json


def _url(end_point):
    return 'http://localhost:5000' + end_point


class Rest_Util:
    def get_tasks(self):
        uri = _url('/tasks')
        print('Get all todo tasks: ' + uri)
        return requests.get(_url('/tasks'))

    def get_task(self, task_id):
        uri = _url('/tasks/{0}').format(task_id)
        print('Get single todo tasks: ' + uri)
        return requests.get(uri)

    def add_task(self, summary):
        uri = _url('/tasks')
        print('Add new tasks with summary: ' + summary)

        return requests.post(_url('/tasks'), json={
            'task': summary,
            'completed': False
        })

    def task_done(task_id):
        pass

    def update_task(self, task_id, summary):
        uri = _url('/tasks/{0}'.format(task_id))
        print('Update tasks with summary: ' + summary)

        return requests.put(uri, json={
            'task': summary,
            'completed': False
        })

    def complete_task(self, task_id):
        uri = _url('/tasks/{0}'.format(task_id))
        print('Complete tasks with id: ' + task_id)

        return requests.post(uri, json={
            'completed': True
        })

    def delete_task(self, task_id):
        uri = _url('/tasks/{0}'.format(task_id))
        print('Delete tasks with id: ' + task_id)
        return requests.delete(uri)
