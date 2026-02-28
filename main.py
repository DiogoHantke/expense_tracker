import argparse, os
from funcs import *

def main():
    os.system('clear') if os.name != 'nt' else os.system('cls')

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
        help="Adiciona um registro: add <description> <category> <amount>",
        description="Cria um novo registro financeiro informando descrição, categoria e valor."
    )
    add_parser.add_argument("description", type=str, help="Descrição do registro.")
    add_parser.add_argument("amount", type=float, help="Valor do registro (número decimal).")


    remove_parser = subparsers.add_parser(
        "dl",
        help="Remove um registro pelo ID: dl <id>",
        description="Exclui um registro existente informando seu identificador numérico."
    )
    remove_parser.add_argument("id", type=int, help="ID do registro que será removido.")


    view_parser = subparsers.add_parser(
        "ls",
        help="Lista registros: ls [--all] [--mth N]",
        description="Exibe registros armazenados, com opções de filtro."
    )
    view_parser.add_argument("--all", action="store_true", help="Mostra todos os registros, sem filtros.")
    view_parser.add_argument("--mth", type=int, help="Filtra registros por mês (1 a 12).")


    args = parser.parse_args()

    args_list = {
        'add' : addExpense,
        'up'  : updateExpense,
        'dl'  : deleteExpense,
        'ls'  : viewAllExpense,
        'rs'  : resumeAllExpense,
        'rm'  : resumeMonthExpense
    }

    result_func = args_list[args.command](args)

if __name__ == '__main__':
    main()
