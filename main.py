import argparse, os

RED    = "\033[33m"
GREEN  = "\033[32m"
RESET  = "\033[0m"

def addExpense(args):
    ...

def updateExpense(args):
    ...

def deleteExpense(args):
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
    """
    +
    RESET
    +
    """
    
    Visão Geral
    -----------
    O Expense Tracker CLI é uma aplicação executada via linha de comando desenvolvida
    para gerenciamento estruturado de despesas financeiras. O sistema permite registrar
    transações, manter persistência local utilizando arquivo JSON, gerar relatórios
    e analisar gastos diretamente no terminal.

    O projeto foi construído com foco em arquitetura limpa, organização modular,
    extensibilidade e boas práticas de engenharia de software.

    Repositório Oficial:
    https://github.com/DiogoHantke/expense_tracker

    -------------------------------------------------------------------------------------

    Funcionalidades Principais
    --------------------------
    • Adicionar novas despesas com descrição e valor
    • Atualizar despesas existentes utilizando identificador único
    • Excluir despesas pelo ID
    • Listar todas as despesas em formato de tabela
    • Gerar resumo financeiro geral
    • Gerar resumo mensal referente ao ano atual
    • Persistência de dados em arquivo JSON
    • Interface estruturada via argparse
    • Preparado para integração com gráficos no terminal

    -------------------------------------------------------------------------------------

    Arquitetura do Projeto
    ----------------------
    • Separação entre interface de linha de comando e lógica de negócio
    • Camada dedicada para manipulação de dados
    • Estrutura modular
    • Design preparado para expansão futura
    • Organização voltada para escalabilidade

    -------------------------------------------------------------------------------------

    Objetivos de Aprendizado
    ------------------------
    • Desenvolvimento de aplicações CLI
    • Manipulação de argumentos com argparse
    • Leitura e escrita de arquivos
    • Persistência de dados com JSON
    • Organização de código em módulos
    • Estruturação de sistemas de relatório
    • Boas práticas de engenharia de software

    -------------------------------------------------------------------------------------

    Melhorias Futuras
    -----------------
    • Sistema de categorias
    • Controle de orçamento mensal
    • Exportação para CSV
    • Implementação de gráficos no terminal
    • Validação avançada de entradas
    • Testes automatizados
    • Refatoração com arquitetura orientada a objetos

    =====================================================================================
    """)
    return

def main():
    os.system('cls')

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

    add_parser = subparsers.add_parser("add", help='add <descrição> <valor>')
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("amount", type=float)

    remove_parser = subparsers.add_parser("rm", help='remove <id>')
    remove_parser.add_argument("id", type=int)

    args = parser.parse_args()

    args_list = {
        'add' : [args.command, lambda : addExpense(args)],
        'up'  : [args.command,  lambda : updateExpense(args)],
        'dl'  : [args.command,  lambda : deleteExpense(args)],
        'ls'  : [args.command,  lambda : viw_allExpense(args)],
        'rs'  : [args.command,  lambda : resumeAllExpense(args)],
        'rm'  : [args.command,  lambda : resumeMonthExpense(args)],
        'dsc' : [args.command, lambda : description()]
    }
    
    args_list[[key for key, item in args_list.items() if item[0] is not None][0]][1]()

if __name__ == '__main__':
    main()
