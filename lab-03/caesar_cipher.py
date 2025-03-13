import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.textEdit.toPlainText(),
            "key": self.ui.plainTextEdit.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textBrowser.setText(data["encrypted_message"])  # Corrected key for response
                self.show_message("Encrypted Successfully")
            else:
                self.show_message(f"Error {response.status_code}: {response.text}", error=True)
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {str(e)}", error=True)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.textBrowser.toPlainText(),
            "key": self.ui.plainTextEdit.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])  # Corrected key for response
                self.show_message("Decrypted Successfully")
            else:
                self.show_message(f"Error {response.status_code}: {response.text}", error=True)
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {str(e)}", error=True)

    def show_message(self, message, error=False):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical if error else QMessageBox.Information)
        msg.setText(message)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
