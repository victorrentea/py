class Task:
    def __init__(self, id):
        self.id = id
        self.started = False

    def set_started(self, start_status):
        self.started = start_status

    def __str__(self):
        return f'Task(id={self.id}, started={self.started})'


def boss_level(fluff, tasks, cr323):
    index = 0
    j = len(tasks)
    print("Logic1")
    task_ids = []
    if fluff:
        print("Logic3")
        for task in tasks:
            print(f"Starting {task}")
            task.set_started(True)

            task_ids.append(task.id)

            if cr323:
                print(f"My Logic: {task}")

            index += 1
            print(f"Audit task #{index}: {task}")
        print(f"Logic6 {j}")
        print(f"Task Ids: {task_ids}")
    else:
        print(f"Logic7 on fluff=false {tasks}")
    print("Logic8")
