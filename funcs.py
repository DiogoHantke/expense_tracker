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
    
    expenses_index = [index for index, expense in enumerate(data["expenses"]) if expense.get('id', 0) == expense_id][0]

    data['expenses'].pop(expenses_index)

    writeJson(data)


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


def table():
    ...

def graphs():
    ...
