import requests


def _url(end_point):
    """ The function to create uri with end point

    Parameters:
        end_point

     Returns:
            Rest resource uri
    """

    return 'http://localhost:5000' + end_point


class Rest_Util:
    """ This class to perform all the operation with app's rest api """

    def get_tasks(self):
        """
        The function to get all tasks from apps's rest server.

        Parameters:

        Returns:
            Response: This function will return rest response
        """

        uri = _url('/tasks')
        return requests.get(uri)

    def get_task(self, task_id):
        """
                The function to get single task from apps's rest server.

                Parameters:
                    task_id

                Returns:
                    Response: This function will return rest response
                """
        uri = _url('/tasks/{0}').format(task_id)
        return requests.get(uri)

    def add_task(self, summary, completed):
        """
                        The function to add new task in apps's rest server.

                        Parameters:
                            summary
                            completed

                        Returns:
                            Response: This function will return rest response
                        """
        uri = _url('/tasks')
        return requests.post(uri, json={
            'task': summary,
            'completed': completed
        })

    def update_task(self, task_id, summary):
        """
                                The function to update existing task in apps's rest server.

                                Parameters:
                                    task_id
                                    summary

                                Returns:
                                    Response: This function will return rest response
                                """
        uri = _url('/tasks/{0}'.format(task_id))
        return requests.put(uri, json={
            'task': summary,
            'completed': False
        })

    def complete_task(self, task_id):
        """
                                The function to mark as complete existing task in apps's rest server.

                                Parameters:
                                    task_id

                                Returns:
                                    Response: This function will return rest response
                                """

        uri = _url('/tasks/{0}'.format(task_id))

        return requests.post(uri, json={
            'completed': True
        })

    def delete_task(self, task_id):
        """
                                The function to delete a single task in apps's rest server.

                                Parameters:
                                    task_id

                                Returns:
                                    Response: This function will return rest response
                                """

        uri = _url('/tasks/{0}'.format(task_id))
        return requests.delete(uri)
