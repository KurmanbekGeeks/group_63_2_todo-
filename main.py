import flet as ft 
from db import main_db


def main(page: ft.Page):
    page.title = 'ToDoList'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=20)

    def view_tasks(task_id, task_text, completed=None):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        checkbox_task = ft.Checkbox(value=bool(completed), 
                                    on_change=lambda e: toggle_task(task_id=task_id, is_completed=e.control.value))

        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else: 
                task_field.read_only = True
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()


        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        return ft.Row([checkbox_task, task_field, edit_button, save_button])
    
    def toggle_task(task_id, is_completed):
        print(is_completed)
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        print(int(is_completed))
        page.update()

    def add_task_db(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task=task)
            print(f'Задача {task} успешно в БД! Его ID - {task_id}')

            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))

            task_input.value = None
            page.update()


    task_input = ft.TextField(label='Введите задачу', expand=True, on_submit=add_task_db)
    send_button = ft.ElevatedButton('SEND', on_click=add_task_db)

    main_objects = ft.Row([task_input, send_button])

    page.add(main_objects, task_list)


if __name__ == '__main__':
    main_db.init_db()
    ft.app(main)