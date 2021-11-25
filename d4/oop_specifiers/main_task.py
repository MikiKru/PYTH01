from d4.oop_specifiers.task import Task

t = Task("Programming", True, 1, "XXX")
print(t.task_name, t.task_status, t._task_id)
t._task_id = 33
print(t.task_name, t.task_status, t._task_id)
t.set_secret("i can see")
print(t.get_secret())