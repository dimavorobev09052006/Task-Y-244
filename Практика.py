import sqlite3
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
from datetime import datetime
import webbrowser

# Подключение к базе данных SQLite
connection = sqlite3.connect("task_manager.db")
cursor = connection.cursor()

# Создание таблицы задач, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    start_time TEXT NOT NULL,
    finish_time TEXT NOT NULL,
    remarks TEXT,
    place TEXT,
    participants TEXT
)
''')
connection.commit()

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Задачник")

        # Элементы интерфейса
        tk.Label(master, text="Введите название задачи:").pack()
        self.title_input = tk.Entry(master, width=30)
        self.title_input.pack()

        tk.Label(master, text="Дата и время начала (YYYY-MM-DD HH:MM):").pack()
        self.start_time_input = tk.Entry(master, width=30)
        self.start_time_input.pack()

        tk.Label(master, text="Дата и время окончания (YYYY-MM-DD HH:MM):").pack()
        self.finish_time_input = tk.Entry(master, width=30)
        self.finish_time_input.pack()

        tk.Label(master, text="Дополнительные заметки:").pack()
        self.remarks_input = tk.Entry(master, width=30)
        self.remarks_input.pack()

        tk.Label(master, text="Местоположение (для карт):").pack()
        self.place_input = tk.Entry(master, width=30)
        self.place_input.pack()

        tk.Label(master, text="Электронные адреса участников:").pack()
        self.participants_input = tk.Entry(master, width=30)
        self.participants_input.pack()

        tk.Button(master, text="Добавить задачу", command=self.add_task).pack()
        tk.Button(master, text="Показать все задачи", command=self.show_tasks).pack()

        self.tasks_box = tk.Listbox(master, width=50)
        self.tasks_box.pack()

    def add_task(self):
        # Сбор данных из полей ввода
        task_title = self.title_input.get()
        start_time = self.start_time_input.get()
        finish_time = self.finish_time_input.get()
        remarks = self.remarks_input.get()
        place = self.place_input.get()
        participants = self.participants_input.get()

        # Добавление задачи в базу данных
        cursor.execute("INSERT INTO tasks (title, start_time, finish_time, remarks, place, participants) VALUES (?, ?, ?, ?, ?, ?)",
                       (task_title, start_time, finish_time, remarks, place, participants))
        connection.commit()

        # Запуск уведомления о задаче в отдельном потоке
        threading.Thread(target=self.notification_timer, args=(start_time, task_title)).start()

        messagebox.showinfo("Успех", "Задача добавлена!")
        self.clear_inputs()

    def notification_timer(self, start_time, task_title):
        now = datetime.now()
        start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        
        # Вычисление времени до уведомления
        delay = (start_datetime - now).total_seconds()

        if delay > 0:
            time.sleep(delay)
            messagebox.showinfo("Напоминание!", f"Время для: {task_title}")

    def show_tasks(self):
        self.tasks_box.delete(0, tk.END)
        cursor.execute("SELECT title, start_time, finish_time FROM tasks")
        all_tasks = cursor.fetchall()

        for task in all_tasks:
            self.tasks_box.insert(tk.END, f"{task[0]} | Начало: {task[1]} | Конец: {task[2]}")

    def clear_inputs(self):
        self.title_input.delete(0, tk.END)
        self.start_time_input.delete(0, tk.END)
        self.finish_time_input.delete(0, tk.END)
        self.remarks_input.delete(0, tk.END)
        self.place_input.delete(0, tk.END)
        self.participants_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()

    # Закрытие подключения к базе данных при выходе
    connection.close()
