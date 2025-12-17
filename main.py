import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from ui_form.login import Ui_Form
from PyQt5 import QtWidgets



def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    login = Ui_Form()
    login.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()