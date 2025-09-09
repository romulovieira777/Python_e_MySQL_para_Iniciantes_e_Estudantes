from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cadastro_produtos"
)


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

formulario.show()
app.exec()
