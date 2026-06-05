# Seção 02 — Interface Gráfica de Usuário (GUI)

Visão geral
-----------
Esta seção apresenta exemplos simples de interfaces gráficas em Python usando PyQt5. O objetivo é mostrar como criar uma janela, capturar entradas do usuário, realizar cálculos e exibir resultados na própria interface.

Conteúdo desta seção
--------------------
- `Salario/`
  - `controle.py` — script principal que carrega a interface e implementa a lógica de cálculo.
  - `tela.ui` — arquivo de interface criado com Qt Designer (arquivo .ui). 

Descrição dos arquivos
---------------------
- `controle.py`
  - Carrega a interface `tela.ui` com `uic.loadUi` e conecta o botão `btnCalcular` à função `principal`.
  - A função `principal` lê os valores dos campos `txtSalario` e `txtDescontos`, converte para float, calcula o salário líquido aplicando o desconto percentual e calcula o FGTS mensal e anual. Em seguida atualiza os rótulos `lblResultado`, `lblFgtsMensal` e `lblFgtsAnual` com o resultado formatado.

- `tela.ui`
  - Layout criado no Qt Designer com campos de entrada e rótulos usados pelo `controle.py`. Pode ser editado no Qt Designer ou convertido para código Python com `pyuic5`.

Pré-requisitos
--------------
- Python 3.x
- PyQt5 (instale com pip)

Instalação rápida
-----------------
No terminal (bash):

```bash
python -m pip install --user pyqt5
```

Como executar
-------------
Abra um terminal e execute os comandos abaixo a partir da raiz do repositório ou diretamente na pasta `Salario`:

```bash
cd Secao_02_Interface_Grafica_de_Usuario/Salario
python controle.py
```

Observações
-----------
- Se o seu ambiente usa `python3` como comando, substitua `python` por `python3`.
- O script carrega `tela.ui` em tempo de execução; portanto `tela.ui` deve estar no mesmo diretório que `controle.py` ou fornecer o caminho correto.
- Para editar a interface visualmente abra `tela.ui` com o Qt Designer (parte do pacote Qt). Para gerar um módulo Python estático a partir do `.ui` use `pyuic5 tela.ui -o tela_ui.py` e importe o resultado no seu `controle.py` se preferir.

Campos esperados na interface
-----------------------------
Baseado em `controle.py`, a interface contém os seguintes objetos (nomes usados no código):
- `txtSalario` — campo de entrada do salário bruto.
- `txtDescontos` — campo de entrada do desconto em porcentagem.
- `btnCalcular` — botão que aciona o cálculo.
- `lblResultado` — rótulo que exibirá o salário líquido formatado.
- `lblFgtsMensal` — rótulo que exibirá o valor do FGTS mensal.
- `lblFgtsAnual` — rótulo que exibirá o valor do FGTS anual.

Melhorias sugeridas
-------------------
- Adicionar validação de entrada (tratamento de exceções para valores não numéricos e entradas vazias).
- Internacionalização/formatos de número (ex.: separador decimal com vírgula para PT-BR).
- Adicionar testes unitários para a função de cálculo (extrair a lógica de `principal` para uma função separada e testável).
- Permitir salvar relatórios em CSV ou imprimir os resultados.

Contribuindo
-----------
1. Faça um fork do repositório.
2. Crie uma branch com a sua alteração.
3. Abra um pull request descrevendo as mudanças.
