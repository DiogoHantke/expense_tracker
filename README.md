<h1>Expense Tracker CLI</h1>

<p>
Expense Tracker é uma aplicação de linha de comando (CLI) desenvolvida em Python
para gerenciamento de despesas pessoais, com persistência de dados em arquivo JSON,
listagem formatada em tabela e geração de relatórios financeiros.
</p>

<p>
O sistema permite adicionar, atualizar, excluir e visualizar despesas,
além de gerar resumos anuais, resumos mensais e comparações gráficas entre gastos e salário.
</p>

<hr>

<h2>Enunciado do Projeto</h2>

<p>
Este projeto foi desenvolvido com base no desafio proposto pela
<a href="https://roadmap.sh/projects/expense-tracker" target="_blank">
Roadmap.sh - Expense Tracker Project
</a>.
</p>

<blockquote>
Criar uma aplicação de rastreamento de despesas que permita adicionar,
remover e visualizar despesas, além de gerar resumos financeiros.
</blockquote>

<hr>

<h2>Requisitos Implementados</h2>

<ul>
    <li>Execução via linha de comando.</li>
    <li>Adicionar despesas com descrição e valor.</li>
    <li>Atualizar despesas existentes.</li>
    <li>Excluir despesas por ID.</li>
    <li>Listar despesas com filtros por mês e ano.</li>
    <li>Gerar resumo anual.</li>
    <li>Gerar resumo mensal.</li>
    <li>Gerar gráfico comparando despesas e salário.</li>
</ul>

<hr>

<h2>Estrutura do Projeto</h2>

<pre><code>
.
├── expense_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── funcs.py
│   ├── colors.py
│
├── assets/
├── expense.json
├── pyproject.toml
├── README.md
└── requirements.txt
</code></pre>

<hr>

<h2>Tecnologias Utilizadas</h2>

<ul>
    <li>Python 3</li>
    <li>argparse</li>
    <li>json</li>
    <li>os</li>
    <li>datetime</li>
    <li>tabulate</li>
    <li>plotext</li>
</ul>

<hr>

<h2>Instalação</h2>

<p>Instalar dependências manualmente:</p>

<pre><code>
pip install tabulate
pip install plotext
</code></pre>

<hr>

<h2>Instalação como Ferramenta Global</h2>

<p>
Este projeto pode ser instalado como um comando de sistema utilizando
o mecanismo de <strong>entry points</strong> do Python.
</p>

<p>
Instalação em modo desenvolvimento:
</p>

<pre><code>
pip install -e .
</code></pre>

<p>
Após a instalação, o comando pode ser executado diretamente:
</p>

<pre><code>
exp --help
</code></pre>

<p>
Também é possível utilizar <code>pipx</code> para instalação global isolada:
</p>

<pre><code>
pipx install .
</code></pre>

<p>
Isso permite utilizar o software como uma ferramenta de linha de comando,
sem necessidade de chamar <code>python main.py</code>.
</p>

<hr>

<h2>Como Executar (Modo Tradicional)</h2>

<pre><code>
python main.py &lt;comando&gt; [argumentos]
</code></pre>

<hr>

<h2>Exemplos de Uso</h2>

<h3>Adicionar despesa</h3>

<code>exp add --description "Lunch" --amount 25</code>

<br><br>
<img src="assets/add_terminal.png" width="700">
<br><br>

<hr>

<h3>Excluir despesa</h3>

<code>exp dl --id 1</code>

<br><br>
<img src="assets/del_terminal.png" width="700">
<br><br>

<hr>

<h3>Listar despesas</h3>

<code>exp ls</code>

<br><br>
<img src="assets/ls_mth_terminal.png" width="700">
<br><br>

<hr>

<h3>Atualizar despesa</h3>

<code>exp up --id 1 --amount 40</code>

<br><br>
<img src="assets/up_terminal.png" width="700">
<br><br>

<hr>

<h3>Resumo anual com gráfico</h3>

<code>exp rs --wage 5000</code>

<br><br>
<img src="assets/rs_terminal.png" width="700">
<br><br>

<hr>

<h3>Resumo mensal com gráfico</h3>

<code>exp rm --mth 2 --wage 5000</code>

<br><br>
<img src="assets/rm_terminal.png" width="700">
<br><br>

<hr>

<h3>Ajuda</h3>

<code>exp --help</code>

<br><br>
<img src="assets/help_terminal.png" width="700">
<br><br>

<hr>

<h2>Decisões de Projeto</h2>

<ul>
    <li>Persistência baseada em JSON.</li>
    <li>Arquitetura funcional modular.</li>
    <li>Separação entre lógica e apresentação.</li>
    <li>Uso de IDs automáticos.</li>
    <li>Validação básica de entrada.</li>
    <li>Geração de relatórios em tabela e gráfico.</li>
    <li>Suporte a instalação como ferramenta CLI.</li>
</ul>

<hr>

<h2>Melhorias Futuras</h2>

<ul>
    <li>Separação completa em camadas.</li>
    <li>Implementação com SQLite.</li>
    <li>Testes automatizados.</li>
    <li>Sistema de categorias.</li>
    <li>Controle de orçamento mensal.</li>
    <li>Exportação para CSV.</li>
    <li>Refatoração orientada a objetos.</li>
</ul>

<hr>

<h2>Objetivo Educacional</h2>

<p>
Projeto desenvolvido para consolidar conhecimentos em lógica de programação,
manipulação de arquivos, desenvolvimento de aplicações CLI,
organização de código, empacotamento de software e geração de relatórios financeiros.
</p>
