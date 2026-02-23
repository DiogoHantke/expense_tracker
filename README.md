<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Expense Tracker CLI</title>
</head>

<body>

<h1>Expense Tracker CLI</h1>

<p>
Aplicativo de rastreamento de despesas executado via linha de comando.
Permite adicionar, atualizar, excluir e visualizar despesas,
além de gerar resumos gerais e resumos mensais do ano atual.
</p>

<hr>

<h2>Demonstração</h2>

<p>
Adicione um arquivo GIF na pasta <code>assets/</code> do projeto.
</p>

<img src="assets/demo.gif" alt="Demonstração do Expense Tracker" width="600">

<hr>

<h2>Funcionalidades</h2>

<ul>
    <li>Adicionar despesas</li>
    <li>Atualizar despesas</li>
    <li>Excluir despesas</li>
    <li>Listar todas as despesas</li>
    <li>Resumo geral das despesas</li>
    <li>Resumo mensal (ano atual)</li>
</ul>

<hr>

<h2>Tecnologias</h2>

<ul>
    <li>Python 3</li>
    <li>argparse</li>
    <li>os</li>
</ul>

<hr>

<h2>Instalação</h2>

<pre>
git clone https://github.com/seu-usuario/expense-tracker.git
cd expense-tracker
</pre>

<p>Para visualizar os comandos disponíveis:</p>

<pre>
python main.py --help
</pre>

<hr>

<h2>Exemplos de Uso</h2>

<h3>Adicionar despesa</h3>

<pre>
python main.py --add "Almoço 25.50"
</pre>

<h3>Atualizar despesa</h3>

<pre>
python main.py --up "ID_NOVO_VALOR"
</pre>

<h3>Excluir despesa</h3>

<pre>
python main.py --dp "ID"
</pre>

<h3>Listar despesas</h3>

<pre>
python main.py --ls
</pre>

<h3>Resumo geral</h3>

<pre>
python main.py --rs
</pre>

<h3>Resumo mensal</h3>

<pre>
python main.py --rm 2
</pre>

<hr>

<h2>Estrutura do Projeto</h2>

<pre>
expense-tracker/
│
├── main.py
├── README.md
└── assets/
    └── demo.gif
</pre>

<hr>

<h2>Melhorias Futuras</h2>

<ul>
    <li>Persistência em arquivo JSON</li>
    <li>Exportação para CSV</li>
    <li>Sistema de categorias</li>
    <li>Controle de orçamento mensal</li>
    <li>Validação de entradas</li>
    <li>Implementação com subcomandos</li>
</ul>

<hr>

<h2>Licença</h2>

<p>Projeto desenvolvido para fins educacionais.</p>

</body>
</html>