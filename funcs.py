from colors import *
from jsonRead import *
from datetime import datetime

def addExpense(args):
    data = readJson()

    try:
        new_id = max(expense.get("id", 0) for expense in data["expenses"])+1

    except IndexError:
        new_id = 1

    date = '-'.join(str(datetime.now()).split()[0].split('-')[::-1])

    new_data = {
        'id' : new_id,
        'amount' : args.amount,
        'category' : args.category,
        'date' : date,
        'description' : args.description
    }

    data['expenses'].append(new_data)
    writeJson(data)


def deleteExpense(args):
    data, expense_id = readJson(), args.id

    if data['expenses'] == []:
        return None
    
    try:
        expenses_index = [index for index, expense in enumerate(data["expenses"]) if expense.get('id', 0) == expense_id][0]

        data['expenses'].pop(expenses_index)

        writeJson(data)

    except IndexError:
        print(RED+'esse id não existe'+RESET)


def updateExpense(args):
    ...

def viw_allExpense(args):
    ...

def resumeAllExpense(args):
    ...

def resumeMonthExpense(args):
    ...

def description():
    print(RED + """

    ██████████████████████████████████████████████████████████████████████████████████████
    ══════════════════════════════════════════════════════════════════════════════════════
                ███████╗██╗  ██╗██████╗ ███████╗███╗   ██╗ ███████╗  ███████╗
                ██╔════╝██║  ██║██╔══██╗██╔════╝████╗  ██║██╔═════╝  ██╔════╝
                █████╗    ███  ║██████╔╝█████╗  ██╔██╗ ██║ ███████═╗ █████╗  
                ██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██║╚██╗██║ ╚════███║ ██╔══╝  
                ███████╗██║  ██║██║     ███████╗██║ ╚████║ ███████║  ███████╗
                ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚══════╝  ╚══════╝
    ██████████████████████████████████████████████████████████████████████████████████████
    ══════════════════════════════════════════════════════════════════════════════════════
    """+RESET)
    return


def table():
    ...

def graphs():
    ...
