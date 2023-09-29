from PyQt5 import uic, QtWidgets


def principal():
    salario = formulario.txtSalario.text()
    salario = float(salario)
    desconto = formulario.txtDescontos.text()
    desconto = float(desconto)
    resultado = (-salario / 100 * desconto) + salario
    fgtsMensal = salario / 100 * 8
    fgtsAnual = fgtsMensal * 12

    formulario.lblResultado.setText(str(f'R$ {resultado:.2f}'))
    formulario.lblFgtsMensal.setText(str(f'R$ {fgtsMensal:.2f}'))
    formulario.lblFgtsAnual.setText(str(f'R$ {fgtsAnual:.2f}'))


app = QtWidgets.QApplication([])
formulario = uic.loadUi("tela.ui")
formulario.btnCalcular.clicked.connect(principal)

formulario.show()
app.exec()
