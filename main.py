import argparse, os

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
    print("""

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

def main():
    os.system('clear')

    parser = argparse.ArgumentParser(
        prog='Expense_Tracker',
        description=('''
            CLI tool for financial expense management.

            Features:
            - Add expenses
            - Update expenses
            - Delete expenses
            - List expenses
            - Generate general summary
            - Generate monthly summary

            Designed for learning CLI architecture,
            data persistence and structured software design.
    ''')
    )

    parser.add_argument("--add", type=str, help='adicionar uma despesa com uma descrição e quantidade')
    parser.add_argument("--up", type=str, help='tualizar uma despesa')
    parser.add_argument("--dl", type=str, help='excluir uma despesa')
    parser.add_argument("--ls", type=str, help='visualizar todas as despesas')
    parser.add_argument("--rs", type=str, help='visualizar um resumo de todas as despesas')
    parser.add_argument("--rm", type=str, help='visualizar um resumo das despesas por um mês específico (do ano atual)')
    parser.add_argument("--dsc", type=str, help='mostra uma descrição geral do aplicativo')

    args = parser.parse_args()

    args_list = {
        'add' : [args.add, lambda : addExpense(args.add)],
        'up'  : [args.up, lambda : updateExpense(args.up)],
        'dl'  : [args.dl, lambda : deleteExpense(args.dl)],
        'ls'  : [args.ls, lambda : viw_allExpense(args.ls)],
        'rs'  : [args.rs, lambda : resumeAllExpense(args.rs)],
        'rm'  : [args.rm, lambda : resumeMonthExpense(args.rm)],
        'dsc' : [args.dsc, lambda : description()]
    }

    args_list[[key for key, value in args_list.items() if value is not None][0]][1]

if __name__ == '__main__':
    main()
