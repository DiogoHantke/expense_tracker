import json, os
from colors import *

def readJson():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "expense.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses = json.load(file)
            return expenses

    except FileNotFoundError:
        
        with open(file_path, "w", encoding="utf-8") as file:
            expenses = {"expenses":[]}
            json.dump(expenses, file, ensure_ascii=False, indent=2) #estudar mais
            print(GREEN + "Arquivo de tarefas criado, adicione sua tarefa" + RESET)
            return expenses
        
    except json.JSONDecodeError:
        
        print(RED + "arquivo corrompido. " + RESET)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({"expenses": []}, file, ensure_ascii=False, indent=2)
        return None

def writeJson(dict_data = None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "expense.json")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dict_data, file, ensure_ascii=False, indent=2)
