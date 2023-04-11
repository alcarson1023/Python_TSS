from PyQt5.QtWidgets import QApplication
from interface import Interface
from selenium_login import Login
from selenium_duplicate_check import Duplicate_Check

def main(username, password, fullName, address, phone, email, submittedDate):
    interface = Interface()
    interface.create_ui()

    login = Login()
    login(username, password)

    duplicate_check = Duplicate_Check
    duplicate_check(phone)