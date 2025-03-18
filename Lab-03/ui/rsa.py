from PyQt5 import QtCore, QtGui, QtWidgets
import rsa
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 170, 61, 16))
        self.label_5.setObjectName("label_5")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(60, 300, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(270, 300, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(600, 290, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(820, 280, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.txt_plain_text = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(100, 60, 401, 81))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_cipher_text = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(100, 170, 401, 91))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_info = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(620, 50, 401, 81))
        self.txt_info.setObjectName("txt_info")
        self.txt_sign = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(620, 170, 401, 81))
        self.txt_sign.setObjectName("txt_sign")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.btn_decrypt.clicked.connect(self.decrypt)
        self.btn_sign.clicked.connect(self.sign)
        self.btn_verify.clicked.connect(self.verify)
        self.btn_gen_keys.clicked.connect(self.generate_keys)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "plaintext:"))
        self.label_3.setText(_translate("MainWindow", "Iformation"))
        self.label_4.setText(_translate("MainWindow", "Cipher text :"))
        self.label_5.setText(_translate("MainWindow", "Siganarute:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Vertify"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))

    def generate_keys(self):
        (pubkey, privkey) = rsa.newkeys(512)
        with open('public.pem', 'wb') as p:
            p.write(pubkey.save_pkcs1('PEM'))
        with open('private.pem', 'wb') as p:
            p.write(privkey.save_pkcs1('PEM'))
        self.txt_info.setText("Keys generated and saved to files.")

    def encrypt(self):
        with open('public.pem', 'rb') as p:
            pubkey = rsa.PublicKey.load_pkcs1(p.read())
        message = self.txt_plain_text.text().encode('utf8')
        ciphertext = rsa.encrypt(message, pubkey)
        self.txt_cipher_text.setText(ciphertext.hex())

    def decrypt(self):
        with open('private.pem', 'rb') as p:
            privkey = rsa.PrivateKey.load_pkcs1(p.read())
        ciphertext = bytes.fromhex(self.txt_cipher_text.text())
        message = rsa.decrypt(ciphertext, privkey).decode('utf8')
        self.txt_plain_text.setText(message)

    def sign(self):
        with open('private.pem', 'rb') as p:
            privkey = rsa.PrivateKey.load_pkcs1(p.read())
        message = self.txt_plain_text.text().encode('utf8')
        signature = rsa.sign(message, privkey, 'SHA-1')
        self.txt_sign.setText(signature.hex())

    def verify(self):
        with open('public.pem', 'rb') as p:
            pubkey = rsa.PublicKey.load_pkcs1(p.read())
        message = self.txt_plain_text.text().encode('utf8')
        signature = bytes.fromhex(self.txt_sign.text())
        try:
            rsa.verify(message, signature, pubkey)
            self.txt_info.setText("Signature verified.")
        except rsa.VerificationError:
            self.txt_info.setText("Signature verification failed.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())