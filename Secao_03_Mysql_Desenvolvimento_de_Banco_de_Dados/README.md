# Seção 03 — MySQL: Desenvolvimento de Banco de Dados

Visão geral
-----------
Esta seção contém scripts SQL e referências para criar e manipular um banco de dados MySQL de exemplo. O material cobre criação de banco de dados, criação de tabelas, inserção de dados, consultas SELECT, filtros com WHERE, atualização de registros (UPDATE) e remoção (DELETE). É ideal para praticar operações básicas de SQL e entender o fluxo de manipulação de dados.

Estrutura do diretório
----------------------
- `Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/`
  - `Links/`
    - `Links.txt` — links úteis relacionados ao ambiente (ex.: XAMPP).
  - `SQL_Code/`
    - `01_Create_Database.sql` — script para criar a base de dados `usuarios`.
    - `02_Create_Table.sql` — script para criar a tabela `tb_usuarios`.
    - `03_Insert_Into.sql` — exemplos de instruções `INSERT` com vários registros.
    - `04_Select.sql` — exemplos de consultas `SELECT` com diferentes colunas.
    - `05_Where.sql` — exemplos de filtros com a cláusula `WHERE`.
    - `06_Update.sql` — exemplos de atualização de registros com `UPDATE`.
    - `07_Delete.sql` — exemplos de remoção de registros com `DELETE`.

Descrição dos scripts SQL
-------------------------
- `01_Create_Database.sql`
  - Cria a base de dados `usuarios`.

- `02_Create_Table.sql`
  - Cria a tabela `tb_usuarios` com os campos:
    - `id_usuario` (INT, chave primária, auto-incremento)
    - `nome` (VARCHAR(150), NOT NULL)
    - `renda` (FLOAT, NOT NULL)
    - `data_de_admissao` (DATE, NOT NULL)

- `03_Insert_Into.sql`
  - Insere vários registros de exemplo na tabela `tb_usuarios`. Observe que as datas estão em formato numérico (AAAAMMDD) — ao usar o MySQL é preferível fornecer strings no formato `YYYY-MM-DD` ou usar funções de data.

- `04_Select.sql`
  - Exemplos de consultas `SELECT`:
    - Selecionar todas as colunas (`SELECT * FROM tb_usuarios;`).
    - Selecionar colunas específicas (`renda, nome`).
    - Selecionar `nome` e `data_de_admissao`.

- `05_Where.sql`
  - Exemplos de consultas filtradas com `WHERE`:
    - Filtrar por `renda` maior que 6000 ou menor que 2000.
    - Filtrar por nome exato (`nome = 'Wagner Cardoso'`).

- `06_Update.sql`
  - Exemplos de `UPDATE` para alterar o nome de usuários com `id_usuario` específico, seguidos de `SELECT` para verificar a alteração.

- `07_Delete.sql`
  - Exemplos de `DELETE` para remover registros por `id_usuario`, seguidos de `SELECT` para verificar o resultado.

Pré-requisitos
--------------
- MySQL server (ou MariaDB) ou um bundle como XAMPP que inclua MySQL e phpMyAdmin.
- Cliente MySQL ou phpMyAdmin para executar os scripts.

Links úteis
-----------
- XAMPP — instalador e informações: https://www.apachefriends.org/pt_br/download.html (conforme `Links/Links.txt`).

Como executar os scripts SQL
---------------------------
1. Inicie o servidor MySQL (ou XAMPP).
2. Abra um cliente MySQL (linha de comando) ou phpMyAdmin.

Exemplo usando linha de comando MySQL:

```bash
# Entrar no MySQL (ajuste usuário/senha conforme seu ambiente)
mysql -u root -p

# No prompt do MySQL, execute os scripts na ordem:
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/01_Create_Database.sql;
USE usuarios;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/02_Create_Table.sql;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/03_Insert_Into.sql;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/04_Select.sql;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/05_Where.sql;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/06_Update.sql;
source /c/path/to/repo/Secao_03_Mysql_Desenvolvimento_de_Banco_de_Dados/SQL_Code/07_Delete.sql;
```

Observações e sugestões
----------------------
- Ajuste os formatos de data em `03_Insert_Into.sql` para `YYYY-MM-DD` para evitar problemas de interpretação de data.
- Antes de executar `DELETE` ou `UPDATE`, recomendo fazer `SELECT` de verificação e/ou trabalhar em um ambiente de testes.
- Adicionar um arquivo `seed.sql` que contenha os inserts com datas corretamente formatadas facilitaria a reprodução do ambiente.
- Para uso em aplicações Python, considere usar um ORM (ex.: SQLAlchemy) ou o conector `mysql-connector-python` e parametrizar consultas para evitar SQL injection.

Contribuindo
-----------
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Abra um pull request com a descrição das mudanças.
