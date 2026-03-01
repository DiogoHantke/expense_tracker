<h1>Expense Tracker CLI</h1>

<p>
Expense Tracker é um <strong>gerenciador de despesas via linha de comando (CLI)</strong>,
desenvolvido como projeto educacional para praticar fundamentos de engenharia de software,
incluindo manipulação de argumentos, persistência de dados, organização modular e geração de relatórios.
</p>

<p>
O aplicativo permite registrar despesas com descrição, valor e data, visualizar listagens formatadas,
gerar resumos gerais e resumos mensais, onde contém gráficos de despesa baseados no salário cadastrado.
</p>

<h2>Demonstração</h2>

<p>GIF de demonstração do uso do CLI:</p>

<img src="assets/demo.gif" alt="Demonstração do Expense Tracker CLI">

<hr>

<h2>Enunciado do Projeto</h2>

<p>
Este projeto foi desenvolvido com base no desafio proposto pela
<a href="https://roadmap.sh/projects/expense-tracker" target="_blank">
Roadmap.sh - Expense Tracker Project
</a>.
</p>

<blockquote>
Crie um aplicativo de rastreamento de despesas simples para gerenciar suas finanças.
O aplicativo deve permitir que os usuários adicionem, excluam e visualizem suas despesas.
A aplicação também deve fornecer um resumo das despesas.
</blockquote>

<p>Requisitos principais:</p>

<ul>
    <li>Executar a partir da linha de comando.</li>
    <li>Adicionar despesas com descrição e valor.</li>
    <li>Atualizar despesas existentes.</li>
    <li>Excluir despesas.</li>
    <li>Visualizar todas as despesas.</li>
    <li>Visualizar resumo geral.</li>
    <li>Visualizar resumo por mês do ano atual.</li>
</ul>

<p>
O projeto faz parte dos exercícios educacionais disponíveis na
<a href="https://roadmap.sh" target="_blank">Roadmap.sh</a>,
plataforma de aprendizado voltada ao desenvolvimento de software.
</p>

<hr>

<h2>Funcionalidades</h2>

<ul>
    <li>Operação exclusiva via CLI</li>
    <li>Persistência de dados em arquivo JSON</li>
    <li>Listagem de despesas em formato tabular</li>
    <li>Resumo financeiro geral</li>
    <li>Resumo financeiro mensal</li>
    <li>Estrutura preparada para gráficos no terminal</li>
</ul>

<p>Cada despesa pode conter:</p>

<ul>
    <li>ID único</li>
    <li>Descrição</li>
    <li>Valor</li>
    <li>Data de registro</li>
    <li>Categoria (opcional)</li>
</ul>

<hr>

<h2>Tecnologias utilizadas</h2>

<ul>
    <li>Python 3</li>
    <li>Módulos nativos: <code>argparse</code>, <code>json</code>, <code>os</code></li>
    <li><code>tabulate</code> para exibição formatada de tabelas</li>
    <li>Biblioteca opcional para gráficos no terminal (ex: <code>plotext</code>)</li>
</ul>

<hr>

<h2>Instalação</h2>

<pre><code>
git clone https://github.com/seu-usuario/expense-tracker.git
cd expense-tracker
</code></pre>

<p>Instale as dependências:</p>

<pre><code>
pip install tabulate
</code></pre>

<p>Se utilizar gráficos no terminal:</p>

<pre><code>
pip install plotext
</code></pre>

<p>Para visualizar os comandos disponíveis:</p>

<pre><code>
python main.py --help
</code></pre>

<hr>

<h2>Estrutura do projeto</h2>

<pre><code>
.
├── main.py
├── storage.py
├── analytics.py
├── data/
│   └── expenses.json
├── assets/
│   └── demo.gif
└── README.md
</code></pre>

<hr>

<h2>Como executar</h2>

<pre><code>
python main.py &lt;comando&gt; [argumentos]
</code></pre>

<hr>

<h2>Comandos disponíveis</h2>

<h3>Adicionar despesa</h3>
<pre><code>
python main.py add "Descrição" 25.50
</code></pre>

<h3>Atualizar despesa</h3>
<pre><code>
python main.py update 1 "Nova descrição" 30.00
</code></pre>

<h3>Excluir despesa</h3>
<pre><code>
python main.py delete 1
</code></pre>

<h3>Listar despesas</h3>
<pre><code>
python main.py list
</code></pre>

<h3>Resumo geral</h3>
<pre><code>
python main.py summary
</code></pre>

<h3>Resumo mensal</h3>
<pre><code>
python main.py monthly &lt;mês&gt;
</code></pre>

<hr>

<h2>Decisões de projeto</h2>

<ul>
    <li><strong>Arquitetura modular:</strong> separação entre interface CLI, persistência e análise de dados.</li>
    <li><strong>Persistência em JSON:</strong> formato simples, legível e portável.</li>
    <li><strong>Exibição tabular:</strong> uso de tabulate para melhor legibilidade no terminal.</li>
    <li><strong>Extensibilidade:</strong> estrutura preparada para futuras funcionalidades como gráficos e categorias.</li>
</ul>

<hr>

<h2>Melhorias futuras</h2>

<ul>
    <li>Sistema completo de categorias</li>
    <li>Controle de orçamento mensal</li>
    <li>Exportação para CSV</li>
    <li>Gráficos diretamente no terminal</li>
    <li>Testes automatizados</li>
    <li>Refatoração orientada a objetos</li>
</ul>

<hr>

<h2>Objetivo educacional</h2>

<p>
Projeto desenvolvido para consolidar conhecimentos em lógica de programação,
manipulação de arquivos, desenvolvimento de aplicações CLI e organização de código,
seguindo desafios propostos pela plataforma Roadmap.sh.
</p>

<hr>

<h2>Licença</h2>

<p>
Projeto livre para estudo, modificação e uso educacional.
</p>
