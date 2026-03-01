<h1>Expense Tracker CLI</h1>

<p>
Expense Tracker é uma aplicação de linha de comando (CLI) desenvolvida em Python
para gerenciamento de despesas pessoais, com persistência de dados em arquivo JSON,
listagem formatada em tabela e geração de relatórios financeiros.
</p>

<p>
O sistema permite adicionar, atualizar, excluir e visualizar despesas,
além de gerar resumos anuais e comparações gráficas entre gastos e salário.
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

<p>Requisitos implementados:</p>

<ul>
    <li>Execução via linha de comando.</li>
    <li>Adicionar despesas com descrição e valor.</li>
    <li>Atualizar despesas existentes.</li>
    <li>Excluir despesas por ID.</li>
    <li>Listar despesas com filtros por mês e ano.</li>
    <li>Gerar resumo anual.</li>
    <li>Gerar gráfico comparando despesas e salário.</li>
</ul>

<hr>

<h2>Estrutura do Projeto</h2>

<pre><code>
.
├── main.py
├── expense.json
├── colors.py
└── README.md
</code></pre>

<hr>

<h2>Funcionalidades e Lógica Interna</h2>

<h3>readJson()</h3>

<p>
Responsável por carregar os dados do arquivo JSON.
Caso o arquivo não exista, ele é criado automaticamente.
Também trata possíveis erros de corrupção do arquivo.
</p>

<p>
Função central de persistência do sistema.
</p>

<hr>

<h3>writeJson(dict_data)</h3>

<p>
Responsável por salvar os dados atualizados no arquivo JSON.
É utilizada após operações de adição, atualização ou exclusão.
</p>

<hr>

<h3>createParser()</h3>

<p>
Define a interface da aplicação utilizando <code>argparse</code>.
Configura os subcomandos disponíveis:
</p>

<ul>
    <li>add</li>
    <li>addw</li>
    <li>dl</li>
    <li>ls</li>
    <li>up</li>
    <li>rs</li>
</ul>

<p>
A função retorna os argumentos processados para serem utilizados
pelas funções correspondentes.
</p>

<hr>

<h3>addExpense(args)</h3>

<p>
Adiciona uma nova despesa ao sistema.
</p>

<p>
Etapas internas:
</p>

<ul>
    <li>Validação de valor positivo.</li>
    <li>Geração automática de ID incremental.</li>
    <li>Registro da data atual.</li>
    <li>Inserção no JSON.</li>
    <li>Exibição da tabela atualizada.</li>
</ul>

<hr>

<h3>deleteExpense(args)</h3>

<p>
Remove uma despesa com base no ID informado.
Caso o ID não exista, uma mensagem de erro é exibida.
</p>

<hr>

<h3>updateExpense(args)</h3>

<p>
Permite atualizar descrição e/ou valor de uma despesa.
</p>

<p>
Antes de aplicar a alteração, o sistema:
</p>

<ul>
    <li>Exibe o registro atual.</li>
    <li>Mostra as modificações destacadas.</li>
    <li>Solicita confirmação do usuário.</li>
</ul>

<hr>

<h3>viewAllExpense(args)</h3>

<p>
Lista as despesas cadastradas.
Permite filtros por mês, ano ou visualização completa.
Caso nenhum filtro seja informado, exibe o mês e ano atual.
</p>

<hr>

<h3>resumeAllExpense(args)</h3>

<p>
Gera o resumo financeiro anual.
</p>

<p>
A função:
</p>

<ul>
    <li>Agrupa despesas por ano e mês.</li>
    <li>Calcula o total mensal.</li>
    <li>Calcula o total anual.</li>
    <li>Exibe tabela formatada.</li>
    <li>Gera gráfico comparando despesas com salário.</li>
</ul>

<hr>

<h3>graphsExpense()</h3>

<p>
Responsável por gerar gráficos no terminal utilizando a biblioteca
<code>plotext</code>.
</p>

<p>
O gráfico compara os valores de despesas mensais com o salário informado.
</p>

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

<pre><code>
git clone https://github.com/seu-usuario/expense-tracker.git
cd expense-tracker
</code></pre>

<p>Instalar dependências:</p>

<pre><code>
pip install tabulate
pip install plotext
</code></pre>

<hr>

<h2>Como Executar</h2>

<pre><code>
python main.py &lt;comando&gt; [argumentos]
</code></pre>

<hr>
<hr>

<h2>Exemplos de Uso</h2>

<h3>Adicionar despesa</h3>

<code>python main.py add --description "Lunch" --amount 25</code>

<br><br>
<img src="assets/add_terminal.png" alt="Add command output" width="700">
<br><br>

<hr>

<h3>Excluir despesa</h3>

<code>python main.py dl --id 1</code>

<br><br>
<img src="assets/del_terminal.png" alt="Delete command output" width="700">
<br><br>

<hr>

<h3>Listar despesas (mês atual)</h3>

<code>python main.py ls</code>

<br><br>
<img src="assets/ls_mth_terminal.png" alt="List month output" width="700">
<br><br>

<hr>

<h3>Listar despesas por ano</h3>

<code>python main.py ls --yr 2026</code>

<br><br>
<img src="assets/ls_yr_terminal.png" alt="List year output" width="700">
<br><br>

<hr>

<h3>Atualizar despesa</h3>

<code>python main.py up --id 1 --amount 40</code>

<br><br>
<img src="assets/up_terminal.png" alt="Update command output" width="700">
<br><br>

<hr>

<h3>Resumo anual com gráfico</h3>

<code>python main.py rs --wage 5000</code>

<br><br>
<img src="assets/rs_terminal.png" alt="Resume annual output" width="700">
<br><br>

<hr>

<h3>Resumo mensal com gráfico</h3>

<code>python main.py rm --mth 2 --wage 5000</code>

<br><br>
<img src="assets/rm_terminal.png" alt="Resume month output" width="700">
<br><br>

<hr>

<h3>Ajuda</h3>

<code>python main.py --help</code>

<br><br>
<img src="assets/help_terminal.png" alt="Help output" width="700">
<br><br>
<hr>

<h2>Decisões de Projeto</h2>

<ul>
    <li>Persistência baseada em JSON.</li>
    <li>Arquitetura funcional modular.</li>
    <li>Separação entre manipulação de dados e exibição.</li>
    <li>Uso de IDs automáticos.</li>
    <li>Validação básica de entrada.</li>
    <li>Geração de relatórios em tabela e gráfico.</li>
</ul>

<hr>

<h2>Melhorias Futuras</h2>

<ul>
    <li>Separação em módulos.</li>
    <li>Implementação de banco SQLite.</li>
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
organização de código e geração de relatórios financeiros.
</p>
