task_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0 
    )
"""

# CRUD - CREATE - READ - UPDATE - DELETE
# INSERT SELECT UPDATE DELETE

insert_task = "INSERT INTO tasks (task) VALUES (?)"

select_task = 'SELECT id, task FROM tasks'

update_task = "UPDATE tasks SET task = ? WHERE id = ?"

delete_task = "DELETE FROM tasks WHERE id = ?"

