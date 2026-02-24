import argparse, os
from funcs import *

def main():
    os.system('clear')

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

    add_parser = subparsers.add_parser("add", help='add <descrição> <category> <valor>')
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("category", type=str)
    add_parser.add_argument("amount", type=float)

    remove_parser = subparsers.add_parser("dl", help='remove <id>')
    remove_parser.add_argument("id", type=int)

    description_parser = subparsers.add_parser("dsc", help='description')

    args = parser.parse_args()

    args_list = {
        'add' : addExpense,
        'up'  : updateExpense,
        'dl'  : deleteExpense,
        'ls'  : viw_allExpense,
        'rs'  : resumeAllExpense,
        'rm'  : resumeMonthExpense,
        'dsc' : description
    }

    result_func = args_list[args.command](args)

if __name__ == '__main__':
    main()
