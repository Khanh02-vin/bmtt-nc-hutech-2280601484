import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        uri = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key_2.toPlainText()
        }

        try:
            response = requests.post(uri, json=payload, timeout=5)  # Added timeout to avoid hanging
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                error_msg = f"API Error: Status Code {response.status_code}"
                print(error_msg)
                self.show_error_message(error_msg)
        except requests.exceptions.ConnectionError as e:
            error_msg = "Connection Error: Is the server running at 127.0.0.1:5000?"
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)
        except requests.exceptions.Timeout as e:
            error_msg = "Request timed out: Server took too long to respond."
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)
        except requests.exceptions.RequestException as e:
            error_msg = "An unexpected error occurred."
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)

    def call_api_decrypt(self):
        uri = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key_2.toPlainText()
        }
        
        try:
            response = requests.post(uri, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                error_msg = f"API Error: Status Code {response.status_code}"
                print(error_msg)
                self.show_error_message(error_msg)
        except requests.exceptions.ConnectionError as e:
            error_msg = "Connection Error: Is the server running at 127.0.0.1:5000?"
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)
        except requests.exceptions.Timeout as e:
            error_msg = "Request timed out: Server took too long to respond."
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)
        except requests.exceptions.RequestException as e:
            error_msg = "An unexpected error occurred."
            print(f"Error: {str(e)}")
            self.show_error_message(error_msg)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())