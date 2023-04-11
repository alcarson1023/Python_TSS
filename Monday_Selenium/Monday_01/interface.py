from PyQt5.QtWidgets import QComboBox, QApplication, QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QCheckBox

from monday_login import Monday_Login
from selenium_duplicate_check import Duplicate_Check
from monday_add_user import Monday_Add_User
from smartboard_create_contact import Smartboard_Create_Contact
from smartboard_message_contact import Smarboard_Message_Contact

class Interface(QDialog):
    def __init__(self):
        super().__init__()
        # Create a layout for the dialog
        layout = QGridLayout()

        self.left = 10
        self.top = 10
        self.headless = False

        # Set the window title
        self.setWindowTitle('Automatic Monday.com Entry')

        # Add a label and line edit for the username
        username_label = QLabel('TriSMART Email')
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText('example@trismartsolar.com')
        layout.addWidget(username_label, 0,0)
        layout.addWidget(self.username_edit, 1,0)

        # Add a label and line edit for the password
        monday_password_label = QLabel('Monday Password')
        self.monday_password_edit = QLineEdit()
        self.monday_password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(monday_password_label, 0,1)
        layout.addWidget(self.monday_password_edit, 1,1)

        # Add a label and line edit for the customer's full name
        customerName_label = QLabel('Customer Full Name')
        self.customerName_edit = QLineEdit()
        layout.addWidget(customerName_label, 2,0)
        layout.addWidget(self.customerName_edit, 3,0)

        # Add a label and line edit for the customer's home address
        smartboard_password_label = QLabel('SmartBoard Password')
        self.smartboard_password_edit = QLineEdit()
        self.smartboard_password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(smartboard_password_label, 2,1)
        layout.addWidget(self.smartboard_password_edit, 3,1)

        # Add a label and line edit for the source of the lead
        leadSource_label = QLabel('Lead Source')
        self.leadSource_edit = QLineEdit()
        layout.addWidget(leadSource_label, 4,0)
        layout.addWidget(self.leadSource_edit, 5,0)

        # Add a label and line edit for the customer's phone number
        phoneNumber_label = QLabel('Customer Phone Number')     # Add logic to put a 1 in front of whatever's entered for consistency. Do not add if there is already a 1.
        self.phoneNumber_edit = QLineEdit()
        layout.addWidget(phoneNumber_label, 4,1)
        layout.addWidget(self.phoneNumber_edit, 5,1)

        # Add a label and line edit for the customer's email address
        customerEmail_label = QLabel('Customer Email Address')
        self.customerEmail_edit = QLineEdit()
        layout.addWidget(customerEmail_label, 6,0)
        layout.addWidget(self.customerEmail_edit, 7,0)

        # Add a label and line edit for the customer's home address
        customerAddress_label = QLabel('Customer Home Address')
        self.customerAddress_edit = QLineEdit()
        layout.addWidget(customerAddress_label, 6,1)
        layout.addWidget(self.customerAddress_edit, 7,1)

        # Button to toggle confirmation methods for the CRMchange button text on click pyqt5
        self.confirmation_method_edit = QPushButton('CRM Confirmation: Email', self)
        self.confirmation_method_edit.setCheckable(True)
        self.confirmation_method_edit.clicked.connect(self.toggleConfirmation)
        layout.addWidget(self.confirmation_method_edit, 8,0)

        # Add an execute button to the layout
        login_button = QPushButton('Execute')
        login_button.clicked.connect(self.execute)
        layout.addWidget(login_button, 8, 1)

        # Add a blank section that can be updated with messages. Had to add "self." so that it could be accessed by display_result. Not sure why.
        self.results = QLabel('')
        layout.addWidget(self.results, 9,0,1,2)

        # Set the layout for the dialog
        self.setLayout(layout)

    def toggleConfirmation(self):
        if self.confirmation_method_edit.isChecked():
            self.confirmation_method_edit.setText('CRM Confirmation: Text')
        else:
            self.confirmation_method_edit.setText('CRM Confirmation: Email')

####################################################################################################################

    def execute(self):
        username = self.username_edit.text()
        monday_password = self.monday_password_edit.text()
        smartboard_password = self.smartboard_password_edit.text()
        fullName = self.customerName_edit.text()
        address = self.customerAddress_edit.text()
        source = self.leadSource_edit.text()
        phone = self.phoneNumber_edit.text()
        email = self.customerEmail_edit.text()
        confirmation = self.confirmation_method_edit.text()
        print('Credentials entered are: ' + username, monday_password, smartboard_password, fullName, address, phone, email, source, confirmation)

        monday_login = Monday_Login()
        self.results.setText(str(monday_login.monday_login(username, monday_password)))

# Setting the result of this one as a variable so that it can be accessed for the monday_add_user if statement.
        duplicate_check = Duplicate_Check()
        duplicate_status = str(duplicate_check.duplicate_check(phone))
        self.results.setText(duplicate_status)

# Only continue with the rest of the script if an existing user was not found in Monday.
        if('No users with matching numbers' in duplicate_status):
            monday_add_user = Monday_Add_User()
            self.results.setText(str(monday_add_user.monday_add_user(fullName, address, phone, email, source)))


# We can probably bump this out of the if statement, since Smartboard won't let you create duplicates either way. However, I like that the system stops if it finds a duplicate.
            smartboard_create_contact = Smartboard_Create_Contact()
            self.results.setText(str(smartboard_create_contact.smartboard_create_contact(username, smartboard_password, fullName, phone, email, confirmation)))

# Add logic to send the first template message depending on whether they came through Calendly or the Solar Calculator. If it's neither, don't send a message at all.
# Add logic to set the Opportunity when creating a new lead in SMARTBoard, either before or after sending the first message.







# Create the application object and UI window
app = QApplication([])
ui = Interface()
ui.show()

app.exec_()