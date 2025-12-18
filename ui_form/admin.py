import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.user_action import create_user_role, delete_user, block_user, unblock_user


from PyQt5 import QtCore, QtGui, QtWidgets


class Admin_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 358)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 371, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 47, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(4, 77, 351, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 20, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(180, 17, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 371, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(176, 14, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 10, 121, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(104, 50, 251, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 270, 371, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 20, 171, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 50, 351, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 371, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setGeometry(QtCore.QRect(120, 30, 131, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_9.setGeometry(QtCore.QRect(280, 30, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        #=========================================================
        self.groupBox.setDisabled(True)
        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(True)
        self.radioButton_7.toggled.connect(self.active_create_user_box)
        self.radioButton_8.toggled.connect(self.active_block_user_box)
        self.radioButton_9.toggled.connect(self.active_delete_user_box)
        self.pushButton.clicked.connect(self.block_or_unblock_user)
        self.pushButton_2.clicked.connect(self.create_user)
        self.pushButton_4.clicked.connect(self.delete_user)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "admin panel"))
        self.groupBox.setTitle(_translate("Form", "new user role"))
        self.radioButton.setText(_translate("Form", "student"))
        self.radioButton_2.setText(_translate("Form", "professor"))
        self.pushButton_2.setText(_translate("Form", "create"))
        self.label.setText(_translate("Form", "username"))
        self.label_2.setText(_translate("Form", "password"))
        self.groupBox_2.setTitle(_translate("Form", "block and unblock user"))
        self.label_3.setText(_translate("Form", "username"))
        self.radioButton_3.setText(_translate("Form", "block user"))
        self.radioButton_4.setText(_translate("Form", "unblok user"))
        self.pushButton.setText(_translate("Form", "commit"))
        self.groupBox_3.setTitle(_translate("Form", "delete user"))
        self.label_5.setText(_translate("Form", "username"))
        self.pushButton_4.setText(_translate("Form", "delete permanently"))
        self.groupBox_4.setTitle(_translate("Form", "which section"))
        self.radioButton_7.setText(_translate("Form", "create user"))
        self.radioButton_8.setText(_translate("Form", "block and unblock user"))
        self.radioButton_9.setText(_translate("Form", "delete user"))

    def active_create_user_box(self):
        self.groupBox.setDisabled(False)
        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(True)

    def active_block_user_box(self):
        self.groupBox.setDisabled(True)
        self.groupBox_2.setDisabled(False)
        self.groupBox_3.setDisabled(True)

    def active_delete_user_box(self):
        self.groupBox.setDisabled(True)
        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(False)
    
    def block_or_unblock_user(self):
        username = self.lineEdit_3.text()
        if self.radioButton_3.isChecked():
            block_user(username)
            self.lineEdit_3.setText("")
            print ("user blocked")
        elif self.radioButton_4.isChecked():
            unblock_user(username)
            self.lineEdit_3.setText("")
            print ("user unblocked")

    def create_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            role = "student"
        elif self.radioButton_2.isChecked():
            role = "professor"
        create_user_role(username, password, role)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        print ("user created")
        

    def delete_user(self):
        username = self.lineEdit_5.text()
        delete_user(username)
        self.lineEdit_5.setText("")
        print ("user deleted")

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Admin_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
