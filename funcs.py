from colors import *
from datetime import datetime
from tabulate import tabulate
import argparse, os, json

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
        return {"expenses": []}

def writeJson(dict_data = None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "expense.json")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dict_data, file, ensure_ascii=False, indent=2)
    

def createParser():
    parser = argparse.ArgumentParser(
        prog='Expense_Tracker',
        usage='%(prog)s [options]',
        description=('''
                CLI tool for financial expense management.
                Designed for learning CLI architecture,
                data persistence and structured software design.
        ''')
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser(
        "add",
        help="Adiciona um registro: add [--description] <description> [--category] <category> [--amount] <amount>",
        description="Cria um novo registro financeiro informando descrição, categoria e valor."
    )
    add_parser.add_argument("--description", type=str, required=True, help="Descrição do registro.")
    add_parser.add_argument("--amount", type=float, required=True, help="Valor do registro (número decimal).")


    remove_parser = subparsers.add_parser(
        "dl",
        help="Remove um registro pelo ID: dl <id>",
        description="Exclui um registro existente informando seu identificador numérico."
    )
    remove_parser.add_argument("--id", type=int, help="ID do registro que será removido.")


    view_parser = subparsers.add_parser(
        "ls",
        help="Lista registros: ls [--all] [--mth]",
        description="Exibe registros armazenados, com opções de filtro."
    )
    view_parser.add_argument("--all", action="store_true", help="Mostra todos os registros, sem filtros.")
    view_parser.add_argument("--mth", type=int, help="Filtra registros por mês (1 a 12).")

    update_parser = subparsers.add_parser(
        "up",
        help="Lista registros: up [--id] [--description]",
        description="Exibe registros armazenados, com opções de filtro."
    )
    update_parser.add_argument("--id", type=int, required=True, help="--id <id>")
    update_parser.add_argument("--description", type=str, help="--description <description>")
    update_parser.add_argument("--amount", type=float, help="--amount <amount>")

    args = parser.parse_args()

    return args


def addExpense(args):
    data = readJson()

    try:
        new_id = max(expense.get("id", 0) for expense in data["expenses"]) + 1

    except ValueError:
        new_id = 1

    date = '-'.join(str(datetime.now()).split()[0].split('-')[::-1])

    new_data = {
        'id': new_id,
        'description': args.description,
        'amount': '%.2f R$' % args.amount,
        'date': date
    }

    data['expenses'].append(new_data)

    print(tableData(data['expenses']))
    writeJson(data)


def deleteExpense(args):
    data, expense_id = readJson(), args.id

    if not data['expenses']:
        return None

    try:
        expenses_index = [
            index
            for index, expense in enumerate(data["expenses"])
            if expense.get('id', 0) == expense_id
        ][0]

        data['expenses'].pop(expenses_index)

        writeJson(data)

    except IndexError:
        print(RED + 'esse id não existe' + RESET)


def updateExpense(args):
    data, index = readJson(), -1

    try:
        item, index = next((item, index) for index, item in enumerate(data['expenses']) if item['id'] == args.id)
        print(f'despesa escolhida\n{tableData([item])}')

    except StopIteration:
        print(f'o id {args.id} não existe')
        return None

    dataUp = {
        'id' : item['id'],
        'description' : args.description if args.description is not None else item['description'],
        'amount' : '%.2f R$' % args.amount if args.amount is not None else item['amount'],
        'date' : item['date']
    }

    printData, keys = dataUp.copy(), dataUp.keys()
    
    for key in keys:
        if dataUp[key] !=  item[key]:
            printData[key] = RED + f'{dataUp[key]}' + RESET

    print(f'\nessa despesa será a alteração, certeza que quer alterar o dado ?\n{tableData([printData])}')
    
    if int(input('0 - Não\n1 - sim\n\n')) is not 0:
        data['expenses'][index] = dataUp
        writeJson(data)
        print(f'despesa alterada com sucesso. \n\n{tableData([dataUp])}')

    else:
        print(f'despesa mantida. \n\n{tableData([item])}')

        
def viewAllExpense(args):
    data, datas = readJson(), []

    if not data['expenses']:
        print("sem despesas.")
        return None

    current_month = str(datetime.now()).split('-')[1]
    
    for expense in data['expenses']:
        if not args.mth:
            if int(expense['date'].split('-')[1]) == int(current_month) or args.all:
                datas.append(expense)
        else:
            if int(expense['date'].split('-')[1]) == args.mth:
                datas.append(expense)

    print(tableData(datas))

    return None
        

def resumeAllExpense(args):
    ...


def resumeMonthExpense(args):
    ...


def tableData(expenses):
    data =  []

    for index, item in enumerate(expenses):
        data.append(expenses[index].values())

    headers = ["id", "description", "amount", "date"]
    table = tabulate(data, headers=headers, tablefmt="rounded_grid")

    return table


def graphsExpense():
    ...