import argparse, os

def main():
    os.system('clear')
    
    parser = argparse.ArgumentParser(
        prog='Expense_Tracker',
        description=(
            'Aplicativo de rastreamento de despesas executado via linha de comando. \n'
            'Permite adicionar, atualizar, excluir e visualizar despesas, \n'
            'além de gerar resumos gerais e resumos mensais do ano atual.\n'
        ),
        epilog='Use os comandos disponíveis para gerenciar suas despesas.'
    )

    parser.add_argument("--add", type=str, help='adicionar uma despesa com uma descrição e quantidade')
    parser.add_argument("--up", type=str, help='tualizar uma despesa')
    parser.add_argument("--dp", type=str, help='excluir uma despesa')
    parser.add_argument("--ls", type=str, help='visualizar todas as despesas')
    parser.add_argument("--rs", type=str, help='visualizar um resumo de todas as despesas')
    parser.add_argument("--rm", type=str, help='visualizar um resumo das despesas por um mês específico (do ano atual)')

    args = parser.parse_args()

    print(args)



if __name__ == '__main__':
    main()
