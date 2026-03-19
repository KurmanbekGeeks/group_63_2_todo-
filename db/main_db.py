import sqlite3
from db import queries
from config import path_db


# def init_db():
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.task_table)
#     print('БД подключена!')
#     conn.commit()
#     conn.close()

def init_db():
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.task_table)
    print('БД подключена!')


# def add_task(task):
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_task, (task, ))
#     conn.commit()
#     task_id = cursor.lastrowid 
#     conn.close()
#     return task_id

def add_task(task):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(queries.insert_task, (task, ))
        task_id = cursor.lastrowid 
    return task_id


def update_task(task_id, new_task=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute(queries.update_task, (new_task, task_id))
    elif completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))

    conn.commit()
    conn.close()

# all - completed - uncompleted
def get_tasks(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'all':
        cursor.execute(queries.select_task)
    elif filter_type == 'completed':
        cursor.execute(queries.select_task_completed)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.select_task_uncompleted)

    tasks = cursor.fetchall()
    conn.close()
    return tasks 
