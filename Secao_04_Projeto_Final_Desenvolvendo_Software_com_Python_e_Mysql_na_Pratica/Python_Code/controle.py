from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro_produtos"
)


def editar():
    dados = lista.tableWidget.currentRow()


def lista():
    lista.show()
    cursor = conexao.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()

    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(4)

    for i in range(0, len(leitura_banco)):
        for j in range(0, 4):
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))


def inserir():
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    estoque = formulario.txtEstoque.txt()

    cursor = conexao.cursor()
    comando_SQL = "INSERT INTO produtos (produto, preco, estoque) VALUES (%s, %s, %s)"
    dados = (str(produto), str(preco), str(estoque))
    cursor.execute(comando_SQL, dados)
    conexao.commit()
    cursor.close()

    formulario.txtProduto.setText("")
    formulario.txtPreco.setText("")
    formulario.txtEstoque.setText("")
    formulario.lblConfirmacao.setText("Produto cadastrado com sucesso!")


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.btnCadastrar.clicked.connect(inserir)
formulario.btnRelatorio.clicked.connect(lista)
lista = uic.loadUi("lista.ui")
editar = uic.loadUi("editar.ui")

formulario.show()
app.exec()
