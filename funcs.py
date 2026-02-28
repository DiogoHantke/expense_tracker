from colors import *
from jsonRead import *
from datetime import datetime
from tabulate import tabulate

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
    data = readJson()

    


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

    print(tableData(data['expenses']))
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