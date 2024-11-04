import json
import os

# Caminho para o arquivo de dados
DATA_FILE = "tasks.json"

# Carregar tarefas do arquivo JSON
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Salvar tarefas no arquivo JSON
def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Adicionar uma nova tarefa
def add_task():
    title = input("Título da tarefa: ")
    description = input("Descrição da tarefa (opcional): ")
    tasks = load_tasks()
    tasks.append({
        "title": title,
        "description": description,
        "completed": False
    })
    save_tasks(tasks)
    print(f"Tarefa '{title}' adicionada com sucesso!")

# Listar todas as tarefas
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{index}. {task['title']} - {task['description']} [{status}]")

# Marcar uma tarefa como concluída
def complete_task():
    list_tasks()
    try:
        task_index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
        tasks = load_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            save_tasks(tasks)
            print(f"Tarefa '{tasks[task_index]['title']}' marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

# Remover uma tarefa
def remove_task():
    list_tasks()
    try:
        task_index = int(input("Digite o número da tarefa para remover: ")) - 1
        tasks = load_tasks()
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Tarefa '{removed_task['title']}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

# Menu principal
def main_menu():
    while True:
        print("\nGerenciador de Tarefas CLI")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Saindo do Gerenciador de Tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
