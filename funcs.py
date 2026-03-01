from colors import *
from datetime import datetime
from tabulate import tabulate
import argparse, os, json
import plotext as plt

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
            json.dump({"expenses":[]}, file, ensure_ascii=False, indent=2)
        return {"expenses":[]}


def writeJson(dict_data = None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "expense.json")

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dict_data, file, ensure_ascii=False, indent=2)
    
    return None
    

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
        help="Adiciona um registro: add [--description] [--category] [--amount]",
        description="Cria um novo registro financeiro informando descrição, categoria e valor."
    )
    add_parser.add_argument("--description", type=str, required=True, help="Descrição do registro.")
    add_parser.add_argument("--amount", type=float, required=True, help="Valor do registro (número decimal).")

    remove_parser = subparsers.add_parser(
        "dl",
        help="Remove um registro pelo ID: dl <id>",
        description="Exclui um registro existente informando seu identificador numérico."
    )
    remove_parser.add_argument("--id", type=int, required= True, help="ID do registro que será removido.")


    view_parser = subparsers.add_parser(
        "ls",
        help="Lista registros: ls [--all] [--mth]",
        description="Exibe registros armazenados, com opções de filtro."
    )
    view_parser.add_argument("--all", action="store_true", help="Mostra todos os registros, sem filtros.")
    view_parser.add_argument("--mth", type=int, help="Filtra registros por mês (1 a 12).")
    view_parser.add_argument("--yr", type=int, help="Filtra registros por ano.")

    update_parser = subparsers.add_parser(
        "up",
        help="Lista registros: up [--id] [--description]",
        description="Exibe registros armazenados, com opções de filtro."
    )
    update_parser.add_argument("--id", type=int, required=True, help="--id <id>")
    update_parser.add_argument("--description", type=str, help="--description <description>")
    update_parser.add_argument("--amount", type=float, help="--amount <amount>")

    resume_all_parser = subparsers.add_parser(
        "rs",
        help="Lista registros: rs",
        description="Exibe registros armazenados, com opções de filtro."
    )

    resume_all_parser.add_argument("--wage", type=float, required=True, help="--wage <name>")

    resume_month_parser = subparsers.add_parser(
        "rm",
        help="Lista registros: rs",
        description="Exibe registros armazenados, com opções de filtro."
    )

    resume_month_parser.add_argument("--wage", type=float, required=True, help="--wage <name>")
    resume_month_parser.add_argument("--mth", type=int, required=True, help="--mth <name>")
    
    args = parser.parse_args()

    return args


def addExpense(args):
    data = readJson()

    if args.amount <= 0:
        print(RED + 'despesa com valor negativo' + RESET)
        return None

    try:
        new_id = max(expense.get("id", 0) for expense in data["expenses"]) + 1

    except ValueError:
        new_id = 1

    date = '-'.join(str(datetime.now()).split()[0].split('-')[::-1])

    new_data = {
        'id': new_id,
        'date': date,
        'description': args.description,
        'amount': args.amount
    }

    data['expenses'].append(new_data)

    writeJson(data)

    if data['expenses'] != []:
        print(tableData(data['expenses']))

    else:
        print(RED + 'não existe despesas.' + RESET)

    return None


def deleteExpense(args):
    data, expense_id = readJson(), args.id

    if not data['expenses']:
        return None

    try:
        for index, expense in enumerate(data["expenses"]):
            if expense["id"] == expense_id:
                break
        else:
            print(RED + 'esse id não existe' + RESET)
            return

        data['expenses'].pop(index)

        writeJson(data)

        if data['expenses'] != []:
            print(tableData(data['expenses']))

        else:
            print(RED + 'não existe despesas.' + RESET)

        return None

    except IndexError:
        print(RED + 'esse id não existe' + RESET)
        return None


def updateExpense(args):
    data, index = readJson(), -1

    if args.amount is not None:
        if args.amount <= 0:
            print(RED + 'despesa negativa' + RESET)
            return None

    try:
        item, index = next((item, index) for index, item in enumerate(data['expenses']) if item['id'] == args.id)
        print(f'despesa escolhida\n{tableData([item])}')

    except StopIteration:
        print(f'o id {args.id} não existe')
        return None

    dataUp = {
        'id' : item['id'],
        'date' : item['date'],
        'description' : args.description if args.description is not None else item['description'],
        'amount' : args.amount if args.amount is not None and args.amount > 0 else item['amount']
    }

    printData, keys = dataUp.copy(), dataUp.keys()
    
    for key in keys:
        if dataUp[key] !=  item[key]:
            printData[key] = RED + f'{dataUp[key]}' + RESET

    print(f'\nessa despesa será a alteração, certeza que quer alterar o dado ?\n{tableData([printData])}')
    
    if int(input('0 - Não\n1 - sim\n\n')) != 0:
        data['expenses'][index] = dataUp
        writeJson(data)
        print(f'despesa alterada com sucesso. \n\n{tableData([dataUp])}')

    else:
        print(f'despesa mantida. \n\n{tableData([item])}')
    
    return None

        
def viewAllExpense(args):
    data, datas = readJson(), []
    
    if not data['expenses']:
        print("sem despesas.")
        return None

    current_month = str(datetime.now()).split('-')[1]
    current_year = str(datetime.now()).split('-')[0]
    
    for expense in data['expenses']:
        if (args.mth is None ) and (args.yr is None) and not args.all:
            if (int(expense['date'].split('-')[1]) == int(current_month) and (int(expense['date'].split('-')[2]) == int(current_year))):
                datas.append(expense)

        elif args.yr and (args.mth is None) and not args.all:
            if int(int(expense['date'].split('-')[2]) == int(args.yr)):
                datas.append(expense)

        elif (args.yr is None) and args.mth and not args.all:
            if int(expense['date'].split('-')[1]) == int(args.mth) and (int(expense['date'].split('-')[2]) == int(current_year)):
                datas.append(expense)

        elif args.yr and args.mth and not args.all:
            if int(expense['date'].split('-')[2]) == int(args.yr) and (int(expense['date'].split('-')[1]) == int(args.mth)):
                datas.append(expense)       
        
        else:
            datas.append(expense)

    if datas is not None and datas != []:
        print(tableData(datas))
    else:
        print(RED + 'essa data não existe' + RESET)

    return None
        

def resumeAllExpense(args):
    expenses = readJson()
    total = {}

    for item in expenses['expenses']:

        year = item['date'].split('-')[2]
        month = item['date'].split('-')[1]

        if year not in total:
            total[year] = {}

        if month not in total[year]:
            total[year][month] = 0

        total[year][month] += item['amount']

    table, result = [], 0

    for year, mounths in total.items():
        
        for mounth, value in mounths.items():
            table.append([mounth, value])
            result += value

        print(tabulate([[f'       {year}      ']], headers=["year"], tablefmt="rounded_grid"))
        print(tabulate(table, headers=["Month", "total"], tablefmt="rounded_grid"))
        print()

        print(tabulate([[f'    {result} R$  ']], headers=['total anual'], tablefmt="rounded_grid"))
    
        graphsExpense(args.wage, table, result)

        print('\n\n')
        
        table = []
        result = 0


def resumeMonthExpense(args):
    data = readJson()

    if not data['expenses']:
        print("sem despesas.")
        return None

    current_year = datetime.now().year
    selected_month = int(args.mth)

    if selected_month < 1 or selected_month > 12:
        print("Mês inválido.")
        return None

    monthly_expenses = []

    for expense in data['expenses']:
        day, month, year = expense['date'].split('-')

        if int(month) == selected_month and int(year) == current_year:
            monthly_expenses.append(expense)

    if not monthly_expenses:
        print("Nenhuma despesa encontrada para esse mês no ano atual.")
        return None

    total = sum(exp['amount'] for exp in monthly_expenses)

    table = [
        [exp['id'], exp['date'], exp['description'], exp['amount']]
        for exp in monthly_expenses
    ]

    print(tabulate(
        table,
        headers=["ID", "Date", "Description", "Amount"],
        tablefmt="rounded_grid"
    ))

    print()
    print(tabulate(
        [[f"{total:.2f} R$"]],
        headers=["Total do Mês"],
        tablefmt="rounded_grid"
    ))

    graph_data = {}

    for exp in monthly_expenses:
        day = exp['date'].split('-')[0]

        if day not in graph_data:
            graph_data[day] = 0

        graph_data[day] += exp['amount']

    graph_table = sorted(
        [(day, value) for day, value in graph_data.items()],
        key=lambda x: int(x[0])
    )

    graphsExpense(args.wage, graph_table, total)

    return None


def tableData(expenses):
    data =  []

    for index, item in enumerate(expenses):
        expense = list(item.values())
        expense[len(expense)-1] = f'{expense[-1:][0]} R$'
        data.append(expense)

    headers = ["id", "date","description", "amount"]
    table = tabulate(data, headers=headers, tablefmt="rounded_grid")

    return table


def graphsExpense(wage, mounths, result):
    labels = [item[0] for item in mounths]
    expenses = [item[1] for item in mounths]

    wages_final = [wage - expense for expense in expenses if wage > expense]

    if(wages_final == []):
        print(RED + "os gastos são maiores que o sálario colocado." + RESET)
        return
    
    plt.simple_stacked_bar(
        labels,
        [expenses, wages_final],
        width=50,
        labels=["expenses", "wage"],
        title="Mostra os gastos anuais VS o salário anual"
    )

    plt.show()