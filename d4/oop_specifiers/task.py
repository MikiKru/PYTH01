class Task:
    def __init__(self, task_name, task_status, task_id, secret):
        self.task_name = task_name
        self.task_status = task_status
        self._task_id = task_id
        self.__secret = secret
    def get_secret(self):
        return self.__secret
    def set_secret(self, secret):
        self.__secret = secret

