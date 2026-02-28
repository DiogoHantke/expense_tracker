from funcs import *

def main():
    os.system('clear') if os.name != 'nt' else os.system('cls')

    args = createParser()

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
