import tkinter as tk
from tkinter import messagebox
import requests # type: ignore
import json

def fetch_repo_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория в формате 'owner/repo'")
        return

    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)

    if response.status_code == 200:
        repo_data = response.json()
        result = {
            'company': None,
            'created_at': repo_data.get('created_at'),
            'email': None,
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': f"https://api.github.com/users/{repo_data.get('owner', {}).get('login')}"
        }

        with open(f"{repo_data.get('name')}_info.json", 'w') as json_file:
            json.dump(result, json_file, indent=4)

        messagebox.showinfo("Успех", f"Информация о репозитории сохранена в файл {repo_data.get('name')}_info.json")
    else:
        messagebox.showerror("Ошибка", f"Не удалось получить данные о репозитории: {response.status_code} ({response.text})")

root = tk.Tk()
root.title("GitHub Repo Info Fetcher")

tk.Label(root, text="Введите имя репозитория (в формате 'owner/repo'):").pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Получить информацию", command=fetch_repo_info).pack(pady=20)

root.mainloop()