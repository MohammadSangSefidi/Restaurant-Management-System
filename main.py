import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import dataBaseFunctions

dataBaseFunctions.createTable()


class WellcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.ui = CreateAdmin()
        self.ui2 = MainPage()

    def initUi(self):
        self.setting()
        self.style()
        self.labels()
        self.progressBar()
        self.timer()

    def setting(self):
        self.setGeometry(450, 200, 600, 300)
        self.resize(600, 300)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setObjectName('WP')

    def style(self):
        self.wellcomeStyle = 'font: 57 30pt "Dubai Medium";'
        self.style1 = 'font: 57 18pt "Dubai Medium";'

    def labels(self):
        self.appNameLabel = QLabel(self)
        self.appNameLabel.setText('نرم افزار مدیریت رستوران')
        self.appNameLabel.setStyleSheet(self.wellcomeStyle)
        self.appNameLabel.move(100, 50)

        self.wellcomeLabel = QLabel(self)
        self.wellcomeLabel.setText('خوش آمدید')
        self.wellcomeLabel.setStyleSheet(self.style1)
        self.wellcomeLabel.move(250, 150)
        self.wellcomeLabel.adjustSize()

    def timer(self):
        self.timer = QTimer(self)
        self.timer.start(15)
        self.timer.timeout.connect(self.fillProgressBar)

    def progressBar(self):
        self.pBar = QProgressBar(self)
        self.pBar.setGeometry(112, 200, 410, 30)

        self.pBar.setValue(0)
        self.pBar.setFormat('')

    # =====Function=====#
    def fillProgressBar(self):
        value = self.pBar.value()
        if value < 100:
            value += 1
            self.pBar.setValue(value)
        else:
            self.timer.stop()
            adminMade = dataBaseFunctions.checkAdminMade()
            if adminMade == 'True':
                self.ui2.show()
            else:
                self.ui.show()
            self.close()


class CreateAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.ui = AddUser()

    def initUi(self):
        self.setting()
        self.style()
        self.lineEdit()
        self.label()
        self.pushButton()

    def style(self):
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 8pt "Dubai Medium";color:red'

    def setting(self):
        self.setGeometry(510, 210, 450, 300)
        self.setMinimumSize(450, 300)
        self.setMaximumSize(450, 300)
        self.setWindowTitle('ثبت نام')
        self.setWindowIcon(QIcon('./icons/log-in.ico'))

        # self.shortKey = QShortcut(QKeySequence('Return'),self)
        # self.shortKey.activated.connect(self.saveAdmin)

    def label(self):
        self.nameLabel = QLabel('نام کاربری', self)
        self.nameLabel.setStyleSheet(self.labelsStyle)
        self.nameLabel.setGeometry(240, 98, 160, 35)

        self.passWordLabel = QLabel('رمز عبور', self)
        self.passWordLabel.setStyleSheet(self.labelsStyle)
        self.passWordLabel.setGeometry(240, 148, 160, 35)

        self.commentLabel = QLabel('یک نام و رمز عبور برای مدیر یا مالک رستوران انتخاب کنید', self)
        self.commentLabel.setStyleSheet(self.labelsStyle)
        self.commentLabel.move(50, 50)
        self.commentLabel.adjustSize()

        self.errorLabel = QLabel(self)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)
        self.errorLabel.move(250, 210)

    def lineEdit(self):
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setStyleSheet(self.lineEditStyle)
        self.nameLineEdit.setGeometry(55, 100, 280, 35)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setStyleSheet(self.lineEditStyle)
        self.passwordLineEdit.setGeometry(55, 150, 280, 35)

    def pushButton(self):
        self.savePushButton = QPushButton('ثبت', self)
        self.savePushButton.setStyleSheet(self.labelsStyle)
        self.savePushButton.setGeometry(180, 200, 60, 35)
        self.savePushButton.clicked.connect(self.saveAdmin)
        self.savePushButton.setShortcut('Return')

    def massegeBox(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText('آیا از اطلاعات وارد شده مطمئن هستید؟')
        self.msgBox.setWindowTitle('اخطار')
        self.msgBox.setStyleSheet(self.labelsStyle)
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.answer = self.msgBox.exec()
        if self.answer == QMessageBox.Ok:
            dataBaseFunctions.addUser(self.nameLineEdit.text(), self.passwordLineEdit.text(), 'True')
            self.ui.show()
            self.close()
        else:
            pass

    # =====Function=====#
    def saveAdmin(self):
        if len(self.nameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0:
            if len(self.passwordLineEdit.text()) > 5:
                self.massegeBox()
            else:
                self.errorLabel.setText('رمز عبور باید بیشتر از پنج کاراکتر باشد')
        else:
            self.errorLabel.setText('لطفا همه کادر های خالی را پر کنید')

        self.errorLabel.adjustSize()


class AddUser(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = AddInformation()
        self.num = 0
        self.allUser = []
        self.initUi()

    def initUi(self):
        self.setting()
        self.styles()
        self.listWidget()
        self.lineEdit()
        self.labels()
        self.pushButtons()

    def styles(self):
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'

    def setting(self):
        self.setGeometry(400, 180, 610, 460)
        self.setMinimumSize(610, 460)
        self.setMaximumSize(610, 460)
        self.setWindowTitle('کاربران')
        self.setWindowIcon(QIcon('./icons/set-users.ico'))

    def listWidget(self):
        self.userList = QListWidget(self)
        self.userList.setGeometry(30, 30, 300, 400)
        self.userList.setStyleSheet(self.itemsListStyle)

    def labels(self):
        self.commantLabel = QLabel('مشخصات کاربران عادی را اضافه کنید', self)
        self.commantLabel.move(350, 30)
        self.commantLabel.setStyleSheet(self.labelsStyle)

        self.errorLabel = QLabel(self)
        self.errorLabel.move(350, 80)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)

        self.userNameLabel = QLabel('نام کاربری', self)
        self.userNameLabel.setGeometry(420, 130, 150, 25)
        self.userNameLabel.setStyleSheet(self.labelsStyle)

        self.userNameLabel = QLabel('رمز عبور', self)
        self.userNameLabel.setGeometry(420, 180, 150, 25)
        self.userNameLabel.setStyleSheet(self.labelsStyle)

    def pushButtons(self):
        self.saveInListPushButton = QPushButton('اضافه کردن', self)
        self.saveInListPushButton.setStyleSheet(self.lineEditStyle)
        self.saveInListPushButton.setGeometry(350, 230, 220, 40)
        self.saveInListPushButton.setShortcut('Return')
        self.saveInListPushButton.clicked.connect(self.saveItem)

        self.deleteItemPushButton = QPushButton('حذف', self)
        self.deleteItemPushButton.setStyleSheet(self.lineEditStyle)
        self.deleteItemPushButton.setGeometry(350, 300, 100, 30)
        self.deleteItemPushButton.setShortcut('Delete')
        self.deleteItemPushButton.clicked.connect(self.deleteItem)

        self.clearPushButton = QPushButton('خالی کردن لیست', self)
        self.clearPushButton.setStyleSheet(self.lineEditStyle)
        self.clearPushButton.setGeometry(470, 300, 100, 30)
        self.clearPushButton.clicked.connect(self.clearUserList)

        self.saveAllInfoPushButton = QPushButton('ثبت', self)
        self.saveAllInfoPushButton.setStyleSheet(self.lineEditStyle)
        self.saveAllInfoPushButton.setGeometry(350, 390, 220, 40)
        self.saveAllInfoPushButton.clicked.connect(self.saveUsers)

    def lineEdit(self):
        self.userNameLineEdit = QLineEdit(self)
        self.userNameLineEdit.setGeometry(350, 130, 150, 25)
        self.userNameLineEdit.setStyleSheet(self.lineEditStyle)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setGeometry(350, 180, 150, 25)
        self.passwordLineEdit.setStyleSheet(self.lineEditStyle)

    # =====Functions=====#
    def saveItem(self):
        if len(self.userNameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0:
            if len(self.passwordLineEdit.text()) > 5:
                self.showUser = f'{self.userNameLineEdit.text()} : {self.passwordLineEdit.text()}'
                self.userList.insertItem(self.num, self.showUser)
                self.allUser.append({'name': self.userNameLineEdit.text(), 'password': self.passwordLineEdit.text()})
                self.num += 1
                self.errorLabel.setText('')
                self.userNameLineEdit.setText('')
                self.passwordLineEdit.setText('')
            else:
                self.errorLabel.setText('رمز عبور باید بیشتر از پنج کاراکتر باشد')
        else:
            self.errorLabel.setText('نام کاربری و رمز عبور فرد را وارد کنید')
        self.errorLabel.adjustSize()

    def deleteItem(self):
        try:
            self.item = self.userList.currentItem()
            itemName = self.item.text()
            itemName = itemName.split(':')
            itemName = itemName[0]
            itemName = itemName.strip()
            self.userList.takeItem(self.userList.currentRow())
            for i in self.allUser:
                if i['name'] == itemName:
                    self.allUser.remove(i)
        except:
            pass

    def clearUserList(self):
        self.userList.clear()
        self.allUser = []

    def saveUsers(self):
        if len(self.allUser) > 0:
            for item in self.allUser:
                dataBaseFunctions.addUser(item['name'], item['password'], 'False')
                self.adminMade = dataBaseFunctions.checkAdminMade()
                self.ui.show()
                self.close()


class AddInformation(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = MainPage()
        self.initUi()
        self.num = 0
        self.allItems = []

    def initUi(self):
        self.setting()
        self.styles()
        self.labels()
        self.lineEdits()
        self.pushButtons()
        self.listWidget()

    def styles(self):
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'

    def setting(self):
        self.setGeometry(280, 200, 900, 500)
        self.setMinimumSize(900, 500)
        self.setMaximumSize(900, 500)
        self.setWindowTitle('محصولات')
        self.setWindowIcon(QIcon('./icons/fast-food.ico'))

    def labels(self):
        self.commantLabel = QLabel('محصولات رستوران خود را وارد کنید', self)
        self.commantLabel.move(300, 30)
        self.commantLabel.setStyleSheet(self.labelsStyle)

        self.itemNameLabel = QLabel('نام محصول:', self)
        self.itemNameLabel.move(640, 78)
        self.itemNameLabel.setStyleSheet(self.labelsStyle)

        self.priceOfItemLabel = QLabel('قیمت محصول:', self)
        self.priceOfItemLabel.move(290, 78)
        self.priceOfItemLabel.setStyleSheet(self.labelsStyle)

        self.TumanLabel1 = QLabel('تومان', self)
        self.TumanLabel1.move(60, 78)
        self.TumanLabel1.setStyleSheet(self.labelsStyle)

        self.errorLabel = QLabel(self)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)
        self.errorLabel.move(590, 150)

        self.serviceChargeLabel = QLabel('هزینه خدمات:', self)
        self.serviceChargeLabel.setStyleSheet(self.labelsStyle)
        self.serviceChargeLabel.move(760, 280)

        self.TumanLabel2 = QLabel('تومان', self)
        self.TumanLabel2.move(560, 280)
        self.TumanLabel2.setStyleSheet(self.labelsStyle)

        self.paidLabel = QLabel('مالیات:', self)
        self.paidLabel.setStyleSheet(self.labelsStyle)
        self.paidLabel.move(760, 330)

        self.percentLabel2 = QLabel('درصد', self)
        self.percentLabel2.move(560, 330)
        self.percentLabel2.setStyleSheet(self.labelsStyle)

    def lineEdits(self):
        self.itemNameLineEdit = QLineEdit(self)
        self.itemNameLineEdit.setGeometry(450, 80, 180, 25)
        self.itemNameLineEdit.setStyleSheet(self.lineEditStyle)

        self.priceOfItemLineEdit = QLineEdit(self)
        self.priceOfItemLineEdit.setGeometry(100, 80, 180, 25)
        self.priceOfItemLineEdit.setStyleSheet(self.lineEditStyle)

        self.serviceChargeLineEdit = QLineEdit(self)
        self.serviceChargeLineEdit.setGeometry(600, 280, 150, 25)
        self.serviceChargeLineEdit.setStyleSheet(self.lineEditStyle)

        self.paidLineEdit = QLineEdit(self)
        self.paidLineEdit.setGeometry(600, 330, 150, 25)
        self.paidLineEdit.setStyleSheet(self.lineEditStyle)

    def pushButtons(self):
        self.saveInListPushButton = QPushButton('اضافه کردن', self)
        self.saveInListPushButton.setStyleSheet(self.lineEditStyle)
        self.saveInListPushButton.setGeometry(750, 78, 100, 30)
        self.saveInListPushButton.setShortcut('Return')
        self.saveInListPushButton.clicked.connect(self.saveItem)

        self.deleteItemPushButton = QPushButton('حذف', self)
        self.deleteItemPushButton.setStyleSheet(self.lineEditStyle)
        self.deleteItemPushButton.setGeometry(480, 150, 100, 30)
        self.deleteItemPushButton.setShortcut('Delete')
        self.deleteItemPushButton.clicked.connect(self.deleteItem)

        self.clearPushButton = QPushButton('خالی کردن لیست', self)
        self.clearPushButton.setStyleSheet(self.lineEditStyle)
        self.clearPushButton.setGeometry(480, 200, 100, 30)
        self.clearPushButton.clicked.connect(self.clearItemsList)

        self.saveInformationPushButton = QPushButton('ثبت اطلاعات', self)
        self.saveInformationPushButton.setStyleSheet(self.lineEditStyle)
        self.saveInformationPushButton.setGeometry(610, 380, 120, 50)
        self.saveInformationPushButton.clicked.connect(self.saveAllInfo)

    def listWidget(self):
        self.itemsList = QListWidget(self)
        self.itemsList.setGeometry(55, 130, 400, 300)
        self.itemsList.setStyleSheet(self.itemsListStyle)

    # =====Functions=====#
    def saveItem(self):
        if len(self.itemNameLineEdit.text()) > 0 and len(self.priceOfItemLineEdit.text()) > 0:
            try:
                int(self.priceOfItemLineEdit.text())
                self.showItem = f'{self.itemNameLineEdit.text()}:{self.priceOfItemLineEdit.text()}'
                self.itemsList.insertItem(self.num, self.showItem)
                self.allItems.append({'name': self.itemNameLineEdit.text(), 'price': self.priceOfItemLineEdit.text()})
                self.num += 1
                self.errorLabel.setText('')
                self.itemNameLineEdit.setText('')
                self.priceOfItemLineEdit.setText('')
            except:
                self.errorLabel.setText('قیمت کالا باید به صورت عدد وارد شود')
        else:
            self.errorLabel.setText('نام محصول و قیمت آن را وارد کنید')
        self.errorLabel.adjustSize()

    def deleteItem(self):
        try:
            self.item = self.itemsList.currentItem()
            itemName = self.item.text()
            itemName = itemName.split(':')
            itemName = itemName[0]
            itemName = itemName.strip()
            for i in self.allItems:
                if i['name'].strip() == itemName:
                    self.allItems.remove(i)
            self.itemsList.takeItem(self.itemsList.currentRow())
        except:
            pass

    def clearItemsList(self):
        self.itemsList.clear()
        self.allItems = []

    def saveAllInfo(self):
        if len(self.allItems) > 0:
            if len(self.serviceChargeLineEdit.text()) > 0 and len(self.paidLineEdit.text()) > 0:
                try:
                    int(self.serviceChargeLineEdit.text())
                    float(self.paidLineEdit.text())
                    if 0 < float(self.paidLineEdit.text()) < 101:
                        for i in self.allItems:
                            dataBaseFunctions.saveItems(i['name'], i['price'])
                        dataBaseFunctions.saveAppInfo('True', self.serviceChargeLineEdit.text(),
                                                      self.paidLineEdit.text())
                        self.ui.show()
                        self.close()
                        self.errorLabel.setText('')
                    else:
                        self.errorLabel.setText('درصد مالیات را به درستی وارد کنید')
                except:
                    self.errorLabel.setText('درصد مالیات و هزینه خدمات باید بصورت عدد وارد شود')
            else:
                self.errorLabel.setText('هنوز درصد مالیات و هزینه خدمات را وارد نکرده اید')
        else:
            self.errorLabel.setText('هنوز هیچ محصولی وارد نکرده اید')
        self.errorLabel.adjustSize()


class MainPage(QMainWindow):
    user = ''

    def __init__(self):
        super().__init__()
        self.initUi()
        self.userUi = UserPage()
        self.adminUi = AdminPage()

    def initUi(self):
        self.setting()
        self.styles()
        self.labels()
        self.lineEdits()
        self.pushBottons()

    def setting(self):
        self.setGeometry(280, 170, 950, 550)
        self.setMinimumSize(950, 550)
        self.setMaximumSize(950, 550)

        self.setWindowTitle('ورود')
        self.setWindowIcon(QIcon('./icons/log-in.ico'))

    def styles(self):
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'
        self.backgroundRightStyle = 'background-color:  rgb(211, 171, 255);'

    def labels(self):
        self.backgroundRight = QLabel(self)
        self.backgroundRight.setGeometry(685, -10, 350, 750)
        self.backgroundRight.setStyleSheet(self.backgroundRightStyle)

        self.iconLabel = QLabel(self)
        self.iconLabel.setGeometry(695, 100, 250, 250)
        self.iconLabel.setPixmap(QPixmap('./icons/user-profile 1.png'))

        self.commandLabel = QLabel('نام کاربری و رمز عبور وارد کنید', self)
        self.commandLabel.move(235, 130)
        self.commandLabel.setStyleSheet(self.labelsStyle)
        self.commandLabel.adjustSize()

        self.userNameLabel = QLabel('نام کاربری', self)
        self.userNameLabel.move(380, 180)
        self.userNameLabel.setStyleSheet(self.labelsStyle)
        self.userNameLabel.adjustSize()

        self.userPasswordLabel = QLabel('رمز عبور', self)
        self.userPasswordLabel.move(390, 230)
        self.userPasswordLabel.setStyleSheet(self.labelsStyle)
        self.userPasswordLabel.adjustSize()

        self.errorLabel = QLabel(self)
        self.errorLabel.move(250, 270)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)

    def lineEdits(self):
        self.userNameLineEdit = QLineEdit(self)
        self.userNameLineEdit.setGeometry(220, 180, 150, 25)
        self.userNameLineEdit.setStyleSheet(self.lineEditStyle)

        self.userPasswordLineEdit = QLineEdit(self)
        self.userPasswordLineEdit.setGeometry(220, 230, 150, 25)
        self.userPasswordLineEdit.setStyleSheet(self.lineEditStyle)

    def pushBottons(self):
        self.singInPushBotton = QPushButton('ورود', self)
        self.singInPushBotton.setGeometry(220, 320, 220, 35)
        self.singInPushBotton.setStyleSheet(self.labelsStyle)
        self.singInPushBotton.setShortcut('Return')
        self.singInPushBotton.clicked.connect(self.signIn)

    # =====Fonctions=====#
    def signIn(self):
        if len(self.userNameLineEdit.text()) > 0 and len(self.userPasswordLineEdit.text()) > 0:
            self.allUser = dataBaseFunctions.gotAllUser()
            checkUser = False
            isAdmin = False
            for i in self.allUser:
                if self.userNameLineEdit.text() == i['name'] and self.userPasswordLineEdit.text() == i['password']:
                    checkUser = True
                    if i['admin'] == 'True':
                        isAdmin = True
            if checkUser == True:
                global user
                MainPage.user = self.userNameLineEdit.text()
                if isAdmin == True:
                    self.close()
                    self.adminUi.show()
                else:
                    self.close()
                    self.userUi.show()
            else:
                self.errorLabel.setText('نام کاربری یا رمز عبور درست نیست')

        else:
            self.errorLabel.setText('نام کاربری و رمز عبور را وارد کنید')
        self.errorLabel.adjustSize()


class UserPage(QWidget):
    def __init__(self):
        super().__init__()
        self.num1 = 0
        self.num2 = 0
        self.selectedItems = []
        self.initUi()

    def initUi(self):
        self.styles()
        self.setting()
        self.labels()
        self.lineEdits()
        self.pushButtons()
        self.listWidgets()

    def setting(self):
        self.setGeometry(280, 170, 950, 550)
        self.setMinimumSize(950, 550)
        self.setMaximumSize(950, 550)
        self.setWindowTitle('ثبت صورتحساب')
        self.setWindowIcon(QIcon('./icons/fast-food.ico'))

    def styles(self):
        self.menuStyle = 'font: 57 18pt "Dubai Medium";border: 2px solid black;box-shadow: 0px 0px 15px black;border-radius: 20%;background-color:white;'
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.buttonStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'
        self.backgroundRightStyle = 'background-color:  rgb(211, 171, 255);'

    def labels(self):
        self.menuLabel = QLabel('منوی غذا', self)
        self.menuLabel.move(160, 30)
        self.menuLabel.setStyleSheet(self.menuStyle)

        self.numberLabel = QLabel('تعداد', self)
        self.numberLabel.move(290, 488)
        self.numberLabel.setStyleSheet(self.labelsStyle)

        self.backgroundRight = QLabel(self)
        self.backgroundRight.setGeometry(685, -10, 350, 750)
        self.backgroundRight.setStyleSheet(self.backgroundRightStyle)

        self.iconLabel = QLabel(self)
        self.iconLabel.setGeometry(750, 320, 250, 250)
        self.iconLabel.setPixmap(QPixmap('./icons/restaurant.png'))

        self.factorLabel = QLabel('صورتحساب', self)
        self.factorLabel.move(750, 60)
        self.factorLabel.setStyleSheet(self.menuStyle)

        self.totalFoodsLabel = QLabel('جمع غذا:', self)
        self.totalFoodsLabel.move(875, 147)
        self.totalFoodsLabel.setStyleSheet(self.labelsStyle)

        self.serviceChargeLabel = QLabel('سرویس:', self)
        self.serviceChargeLabel.move(875, 187)
        self.serviceChargeLabel.setStyleSheet(self.labelsStyle)

        self.paidLabel = QLabel('مالیات:', self)
        self.paidLabel.move(875, 227)
        self.paidLabel.setStyleSheet(self.labelsStyle)

        self.totalLabel = QLabel('مجموع:', self)
        self.totalLabel.move(875, 267)
        self.totalLabel.setStyleSheet(self.labelsStyle)

        self.errorLabel = QLabel(self)
        self.errorLabel.move(410, 50)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)

    def lineEdits(self):
        self.numberOfProudouctLineEdit = QLineEdit(self)
        self.numberOfProudouctLineEdit.setGeometry(230, 488, 50, 25)
        self.numberOfProudouctLineEdit.setStyleSheet(self.lineEditStyle)

        self.totalFoodsLineEdit = QLineEdit(self)
        self.totalFoodsLineEdit.setGeometry(720, 150, 150, 25)
        self.totalFoodsLineEdit.setStyleSheet(self.lineEditStyle)

        self.serviceChargeLineEdit = QLineEdit(self)
        self.serviceChargeLineEdit.setGeometry(720, 190, 150, 25)
        self.serviceChargeLineEdit.setStyleSheet(self.lineEditStyle)

        self.paidLineEdit = QLineEdit(self)
        self.paidLineEdit.setGeometry(720, 230, 150, 25)
        self.paidLineEdit.setStyleSheet(self.lineEditStyle)

        self.totalLineEdit = QLineEdit(self)
        self.totalLineEdit.setGeometry(720, 270, 150, 25)
        self.totalLineEdit.setStyleSheet(self.lineEditStyle)

    def pushButtons(self):
        self.addPushButton = QPushButton('اضافه کردن', self)
        self.addPushButton.setGeometry(90, 480, 120, 40)
        self.addPushButton.setStyleSheet(self.buttonStyle)
        self.addPushButton.setShortcut('Return')
        self.addPushButton.clicked.connect(self.addItem)

        self.deletePushButton = QPushButton('حذف', self)
        self.deletePushButton.setGeometry(590, 480, 60, 40)
        self.deletePushButton.setStyleSheet(self.buttonStyle)
        self.deletePushButton.setShortcut('Delete')
        self.deletePushButton.clicked.connect(self.deleteItem)

        self.clearPushButton = QPushButton('خالی کردن لیست', self)
        self.clearPushButton.setGeometry(465, 480, 120, 40)
        self.clearPushButton.setStyleSheet(self.buttonStyle)
        self.clearPushButton.clicked.connect(self.clearSelectList)

        self.calculationPushButton = QPushButton('محاسبه', self)
        self.calculationPushButton.setGeometry(400, 480, 60, 40)
        self.calculationPushButton.setStyleSheet(self.buttonStyle)
        self.calculationPushButton.clicked.connect(self.calculationFactor)

        self.saveInDataBaseButton = QPushButton('ثبت فاکتور', self)
        self.saveInDataBaseButton.setGeometry(720, 310, 130, 40)
        self.saveInDataBaseButton.setStyleSheet(self.buttonStyle)
        self.saveInDataBaseButton.clicked.connect(self.saveFactor)

        self.clearDataButton = QPushButton('پاک کردن', self)
        self.clearDataButton.setGeometry(855, 310, 70, 40)
        self.clearDataButton.setStyleSheet(self.buttonStyle)
        self.clearDataButton.clicked.connect(self.clearData)

    def listWidgets(self):
        self.menuList = QListWidget(self)
        self.menuList.setGeometry(30, 80, 350, 380)
        self.menuList.setStyleSheet(self.itemsListStyle)

        self.menu = dataBaseFunctions.gotMenu()
        for i in self.menu:
            self.menuList.insertItem(self.num1, f'{i["name"]}:{i["price"]}')
            self.num1 += 1

        self.selectList = QListWidget(self)
        self.selectList.setGeometry(400, 80, 250, 380)
        self.selectList.setStyleSheet(self.itemsListStyle)

    # =====Functions=====#
    def addItem(self):
        if self.menuList.currentItem() != None:
            if len(self.numberOfProudouctLineEdit.text()) > 0:
                try:
                    int(self.numberOfProudouctLineEdit.text())
                    if int(self.numberOfProudouctLineEdit.text()) > 0:
                        item = self.menuList.currentItem()
                        itemText = item.text()
                        itemList = itemText.split(':')
                        self.selectList.insertItem(self.num2,
                                                   f'{itemList[0]} X{self.numberOfProudouctLineEdit.text()} : {int(itemList[1]) * int(self.numberOfProudouctLineEdit.text())}')
                        self.selectedItems.append({'name': itemList[0], 'price': itemList[1],
                                                   'number': self.numberOfProudouctLineEdit.text()})
                        self.errorLabel.setText('')
                    else:
                        self.errorLabel.setText('تعداد محصولات درست وارد کنید')
                except:
                    self.errorLabel.setText('تعداد محصولات باید بصورت عدد وارد شود')
            else:
                self.errorLabel.setText('لطفا تعداد را وارد کنید')
        else:
            self.errorLabel.setText('لطفا یک محصول را انتخاب کنید')
        self.errorLabel.adjustSize()

    def deleteItem(self):
        try:
            self.item = self.selectList.currentItem()
            item = self.item.text()
            itemList = item.split('X')
            itemName = itemList[0]
            numberOfItem = itemList[1]
            itemName = itemName.strip()
            for i in self.selectedItems:
                if i['name'] == itemName and i['number'] == numberOfItem:
                    self.selectedItems.remove(i)
                print(self.selectedItems)
            self.selectList.takeItem(self.selectList.currentRow())
        except:
            pass

    def clearSelectList(self):
        self.selectList.clear()
        self.selectedItems = []

    def calculationFactor(self):
        if len(self.selectedItems) > 0:
            appInfo = dataBaseFunctions.gotAppInfo()
            totalFoods = 0
            for i in self.selectedItems:
                totalItem = int(i['price']) * int(i['number'])
                totalFoods += totalItem
            serviceCharge = int(appInfo[2])
            paid = (int(appInfo[3]) * totalFoods) / 100
            total = totalFoods + serviceCharge + paid

            self.totalFoodsLineEdit.setText(str(totalFoods))
            self.serviceChargeLineEdit.setText(str(serviceCharge))
            self.paidLineEdit.setText(str(paid))
            self.totalLineEdit.setText(str(total))
        else:
            self.errorLabel.setText('هنوز محصولی انتخاب نشده است')
        self.errorLabel.adjustSize()

    def clearData(self):
        self.totalFoodsLineEdit.setText('')
        self.serviceChargeLineEdit.setText('')
        self.paidLineEdit.setText('')
        self.totalLineEdit.setText('')

    def saveFactor(self):
        if len(self.selectedItems) > 0 and len(self.totalFoodsLineEdit.text()) and len(
                self.paidLineEdit.text()) > 0 and len(self.totalLineEdit.text()):
            import datetime
            nowDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.user = MainPage.user
            self.foods = '__'
            for i in self.selectedItems:
                foodName = i['name']
                number = i['number']
                self.foods += f'{foodName}X{number}__'
            dataBaseFunctions.saveFactor(self.user, self.foods, self.totalFoodsLineEdit.text(),
                                         self.paidLineEdit.text(), self.totalLineEdit.text(), nowDateTime)
            self.errorLabel.setText('')
            self.totalFoodsLineEdit.setText('')
            self.serviceChargeLineEdit.setText('')
            self.paidLineEdit.setText('')
            self.totalLineEdit.setText('')
        else:
            self.errorLabel.setText('اول باید قیمت محصولات محاسبه شود')
        self.errorLabel.adjustSize()


class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui1 = ChangeUser()
        self.ui2 = FactorsPage()
        self.ui3 = ChangeAdmin()
        self.num = 0
        self.menu = dataBaseFunctions.gotMenu()
        self.appInfo = dataBaseFunctions.gotAppInfo()
        self.initUi()

    def initUi(self):
        self.setting()
        self.styles()
        self.labels()
        self.pushButtons()
        self.lineEdits()
        self.listWidget()

    def setting(self):
        self.setGeometry(280, 170, 950, 550)
        self.setMinimumSize(950, 550)
        self.setMaximumSize(950, 550)
        self.setWindowTitle('مدیریت رستوران')
        self.setWindowIcon(QIcon('./icons/fast-food.ico'))

    def styles(self):
        self.menuStyle = 'font: 57 18pt "Dubai Medium";border: 2px solid black;box-shadow: 0px 0px 15px black;border-radius: 20%;background-color:white;'
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.buttonStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'
        self.backgroundRightStyle = 'background-color:  rgb(211, 171, 255);'
        self.messageLabelStyle = 'font: 57 11pt "Dubai Medium";color:green'
        self.userBackgroundStyle = 'background-color: white ;border: 1px solid black; border-radius:10% ;'

    def labels(self):
        self.backgroundRight = QLabel(self)
        self.backgroundRight.setGeometry(685, -10, 350, 750)
        self.backgroundRight.setStyleSheet(self.backgroundRightStyle)

        self.menuLabel = QLabel('منوی غذا', self)
        self.menuLabel.move(270, 20)
        self.menuLabel.setStyleSheet(self.menuStyle)

        self.itemNameLabel = QLabel('نام محصول:', self)
        self.itemNameLabel.move(540, 78)
        self.itemNameLabel.setStyleSheet(self.labelsStyle)

        self.priceOfItemLabel = QLabel('قیمت محصول:', self)
        self.priceOfItemLabel.move(250, 78)
        self.priceOfItemLabel.setStyleSheet(self.labelsStyle)

        self.serviceChargeLabel = QLabel('هزینه خدمات:', self)
        self.serviceChargeLabel.setStyleSheet(self.labelsStyle)
        self.serviceChargeLabel.move(530, 480)

        self.TumanLabel1 = QLabel('تومان', self)
        self.TumanLabel1.move(330, 480)
        self.TumanLabel1.setStyleSheet(self.labelsStyle)

        self.paidLabel = QLabel('مالیات:', self)
        self.paidLabel.setStyleSheet(self.labelsStyle)
        self.paidLabel.move(250, 480)

        self.percentLabel2 = QLabel('درصد', self)
        self.percentLabel2.move(50, 480)
        self.percentLabel2.setStyleSheet(self.labelsStyle)

        self.errorLabel = QLabel(self)
        self.errorLabel.move(90, 440)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)

        self.messageLabel = QLabel(self)
        self.messageLabel.move(487, 250)
        self.messageLabel.setStyleSheet(self.messageLabelStyle)

    def lineEdits(self):
        self.itemNameLineEdit = QLineEdit(self)
        self.itemNameLineEdit.setGeometry(350, 80, 180, 25)
        self.itemNameLineEdit.setStyleSheet(self.lineEditStyle)

        self.priceOfItemLineEdit = QLineEdit(self)
        self.priceOfItemLineEdit.setGeometry(60, 80, 180, 25)
        self.priceOfItemLineEdit.setStyleSheet(self.lineEditStyle)

        self.serviceChargeLineEdit = QLineEdit(self)
        self.serviceChargeLineEdit.setGeometry(370, 480, 150, 25)
        self.serviceChargeLineEdit.setStyleSheet(self.lineEditStyle)
        self.serviceChargeLineEdit.setText(str(self.appInfo[2]))

        self.paidLineEdit = QLineEdit(self)
        self.paidLineEdit.setGeometry(90, 480, 150, 25)
        self.paidLineEdit.setStyleSheet(self.lineEditStyle)
        self.paidLineEdit.setText(str(self.appInfo[3]))

    def pushButtons(self):
        self.saveInListPushButton = QPushButton('اضافه کردن', self)
        self.saveInListPushButton.setStyleSheet(self.lineEditStyle)
        self.saveInListPushButton.setGeometry(487, 129, 130, 35)
        self.saveInListPushButton.setShortcut('Return')
        self.saveInListPushButton.clicked.connect(self.saveItem)

        self.deleteItemPushButton = QPushButton('حذف', self)
        self.deleteItemPushButton.setStyleSheet(self.lineEditStyle)
        self.deleteItemPushButton.setGeometry(487, 300, 130, 35)
        self.deleteItemPushButton.setShortcut('Delete')
        self.deleteItemPushButton.clicked.connect(self.deleteItem)

        self.clearPushButton = QPushButton('خالی کردن لیست', self)
        self.clearPushButton.setStyleSheet(self.lineEditStyle)
        self.clearPushButton.setGeometry(487, 340, 130, 35)
        self.clearPushButton.clicked.connect(self.clearItemsList)

        self.changeInfoPushButton = QPushButton('ذخیره تغییرات', self)
        self.changeInfoPushButton.setStyleSheet(self.lineEditStyle)
        self.changeInfoPushButton.setGeometry(487, 395, 130, 35)
        self.changeInfoPushButton.clicked.connect(self.changeInfo)

        self.showFactorsPushButton = QPushButton('صورتحساب ها', self)
        self.showFactorsPushButton.setGeometry(760, 200, 120, 40)
        self.showFactorsPushButton.setStyleSheet(self.labelsStyle)
        self.showFactorsPushButton.clicked.connect(self.showFactorsPage)

        self.showAllUserPushButton = QPushButton('کاربران', self)
        self.showAllUserPushButton.setGeometry(760, 250, 120, 40)
        self.showAllUserPushButton.setStyleSheet(self.labelsStyle)
        self.showAllUserPushButton.clicked.connect(self.showChangeUser)

        self.showChangeAdminPushButton = QPushButton('اطلاعات حساب', self)
        self.showChangeAdminPushButton.setGeometry(760, 150, 120, 40)
        self.showChangeAdminPushButton.setStyleSheet(self.labelsStyle)
        self.showChangeAdminPushButton.clicked.connect(self.showChangeAdmin)

    def listWidget(self):
        self.itemsList = QListWidget(self)
        self.itemsList.setGeometry(55, 130, 400, 300)
        self.itemsList.setStyleSheet(self.itemsListStyle)

        for i in self.menu:
            self.itemsList.insertItem(self.num, f'{i["name"]}:{i["price"]}')
            self.num += 1

    # =====Functions=====#
    def saveItem(self):
        if len(self.itemNameLineEdit.text()) > 0 and len(self.priceOfItemLineEdit.text()) > 0:
            try:
                int(self.priceOfItemLineEdit.text())
                self.showItem = f'{self.itemNameLineEdit.text()}:{self.priceOfItemLineEdit.text()}'
                self.itemsList.insertItem(self.num, self.showItem)
                self.menu.append({'name': self.itemNameLineEdit.text(), 'price': self.priceOfItemLineEdit.text()})
                self.num += 1
                self.errorLabel.setText('')
                self.itemNameLineEdit.setText('')
                self.priceOfItemLineEdit.setText('')
            except:
                self.errorLabel.setText('قیمت کالا باید به صورت عدد وارد شود')
        else:
            self.errorLabel.setText('نام محصول و قیمت آن را وارد کنید')
        self.errorLabel.adjustSize()

    def deleteItem(self):
        try:
            self.item = self.itemsList.currentItem()
            itemName = self.item.text()
            itemName = itemName.split(':')
            itemName = itemName[0]
            itemName = itemName.strip()
            for i in self.menu:
                if i['name'].strip() == itemName:
                    self.menu.remove(i)
            self.itemsList.takeItem(self.itemsList.currentRow())
        except:
            pass

    def changeInfo(self):
        if len(self.menu) > 0:
            if len(self.serviceChargeLineEdit.text()) > 0 and len(self.paidLineEdit.text()) > 0:
                try:
                    int(self.serviceChargeLineEdit.text())
                    float(self.paidLineEdit.text())
                    if 0 < float(self.paidLineEdit.text()) < 101:
                        dataBaseFunctions.clearItems()
                        for i in self.menu:
                            dataBaseFunctions.saveItems(i['name'], i['price'])
                        dataBaseFunctions.changeAppInfo(self.serviceChargeLineEdit.text(), self.paidLineEdit.text())
                        self.messageLabel.setText('تغییرات ذخیره شد')
                        self.errorLabel.setText('')
                    else:
                        self.errorLabel.setText('درصد مالیات را به درستی وارد کنید')
                        self.messageLabel.setText('')
                except:
                    self.errorLabel.setText('درصد مالیات و هزینه خدمات باید بصورت عدد وارد شود')
                    self.messageLabel.setText('')
            else:
                self.errorLabel.setText('هزینه سرویس یا مالیات خالی است')
                self.messageLabel.setText('')
        else:
            self.errorLabel.setText('لیست محصولات خالی است')
            self.messageLabel.setText('')

        self.errorLabel.adjustSize()
        self.messageLabel.adjustSize()

    def clearItemsList(self):
        self.itemsList.clear()
        self.menu = []

    def showChangeUser(self):
        self.ui1.show()

    def showFactorsPage(self):
        self.ui2.show()

    def showChangeAdmin(self):
        self.ui3.show()


class ChangeUser(QWidget):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.allUser = []
        self.initUi()

    def initUi(self):
        self.setting()
        self.styles()
        self.listWidget()
        self.lineEdit()
        self.labels()
        self.pushButtons()

    def styles(self):
        self.menuStyle = 'font: 57 18pt "Dubai Medium";border: 2px solid black;box-shadow: 0px 0px 15px black;border-radius: 20%;background-color:white;'
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 11pt "Dubai Medium";color:red'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'

    def setting(self):
        self.setGeometry(400, 200, 610, 460)
        self.setMinimumSize(610, 460)
        self.setMaximumSize(610, 460)
        self.setWindowTitle('کاربران')
        self.setWindowIcon(QIcon('./icons/set-users.ico'))

    def listWidget(self):
        self.userList = QListWidget(self)
        self.userList.setGeometry(30, 30, 300, 400)
        self.userList.setStyleSheet(self.itemsListStyle)

        self.user = dataBaseFunctions.gotAllUser()
        for i in self.user:
            if i['admin'] == 'False':
                self.userList.insertItem(self.num, f'{i["name"]} : {i["password"]}')
                self.allUser.append({'name': i["name"], 'password': i["password"]})

    def labels(self):
        self.commantLabel = QLabel('کاربران', self)
        self.commantLabel.move(430, 30)
        self.commantLabel.setStyleSheet(self.menuStyle)

        self.errorLabel = QLabel(self)
        self.errorLabel.move(350, 80)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)

        self.userNameLabel = QLabel('نام کاربری', self)
        self.userNameLabel.setGeometry(420, 130, 150, 25)
        self.userNameLabel.setStyleSheet(self.labelsStyle)

        self.userNameLabel = QLabel('رمز عبور', self)
        self.userNameLabel.setGeometry(420, 180, 150, 25)
        self.userNameLabel.setStyleSheet(self.labelsStyle)

    def pushButtons(self):
        self.saveInListPushButton = QPushButton('اضافه کردن', self)
        self.saveInListPushButton.setStyleSheet(self.lineEditStyle)
        self.saveInListPushButton.setGeometry(350, 230, 220, 40)
        self.saveInListPushButton.setShortcut('Return')
        self.saveInListPushButton.clicked.connect(self.saveItem)

        self.deleteItemPushButton = QPushButton('حذف', self)
        self.deleteItemPushButton.setStyleSheet(self.lineEditStyle)
        self.deleteItemPushButton.setGeometry(350, 300, 100, 30)
        self.deleteItemPushButton.setShortcut('Delete')
        self.deleteItemPushButton.clicked.connect(self.deleteItem)

        self.clearPushButton = QPushButton('خالی کردن لیست', self)
        self.clearPushButton.setStyleSheet(self.lineEditStyle)
        self.clearPushButton.setGeometry(470, 300, 100, 30)
        self.clearPushButton.clicked.connect(self.clearUserList)

        self.saveAllInfoPushButton = QPushButton('ثبت', self)
        self.saveAllInfoPushButton.setStyleSheet(self.lineEditStyle)
        self.saveAllInfoPushButton.setGeometry(350, 390, 220, 40)
        self.saveAllInfoPushButton.clicked.connect(self.saveUsers)

    def lineEdit(self):
        self.userNameLineEdit = QLineEdit(self)
        self.userNameLineEdit.setGeometry(350, 130, 150, 25)
        self.userNameLineEdit.setStyleSheet(self.lineEditStyle)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setGeometry(350, 180, 150, 25)
        self.passwordLineEdit.setStyleSheet(self.lineEditStyle)

    # =====Functions=====#
    def saveItem(self):
        if len(self.userNameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0:
            if len(self.passwordLineEdit.text()) > 5:
                self.showUser = f'{self.userNameLineEdit.text()} : {self.passwordLineEdit.text()}'
                self.userList.insertItem(self.num, self.showUser)
                self.allUser.append({'name': self.userNameLineEdit.text(), 'password': self.passwordLineEdit.text()})
                self.num += 1
                self.errorLabel.setText('')
                self.userNameLineEdit.setText('')
                self.passwordLineEdit.setText('')
            else:
                self.errorLabel.setText('رمز عبور باید بیشتر از پنج کاراکتر باشد')
        else:
            self.errorLabel.setText('نام کاربری و رمز عبور فرد را وارد کنید')
        self.errorLabel.adjustSize()

    def deleteItem(self):
        try:
            self.item = self.userList.currentItem()
            itemName = self.item.text()
            itemName = itemName.split(':')
            itemName = itemName[0]
            itemName = itemName.strip()
            self.userList.takeItem(self.userList.currentRow())
            for i in self.allUser:
                if i['name'] == itemName:
                    self.allUser.remove(i)
        except:
            pass

    def clearUserList(self):
        self.userList.clear()
        self.allUser = []

    def saveUsers(self):
        if len(self.allUser) > 0:
            dataBaseFunctions.deleteUser()
            for item in self.allUser:
                dataBaseFunctions.addUser(item['name'], item['password'], 'False')
            self.close()


class FactorsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setting()
        self.style()
        self.listWidget()
        self.labels()

    def setting(self):
        self.setGeometry(400, 200, 610, 480)
        self.setMinimumSize(610, 480)
        self.setMaximumSize(610, 480)
        self.setWindowTitle('صورتحساب ها')
        self.setWindowIcon(QIcon('./icons/notes.ico'))

    def style(self):
        self.menuStyle = 'font: 57 18pt "Dubai Medium";border: 2px solid black;box-shadow: 0px 0px 15px black;border-radius: 20%;background-color:white;'
        self.itemsListStyle = 'background-color:white;font: 57 12pt "Dubai Medium";'

    def labels(self):
        self.titelLabel = QLabel('صورتحساب ها', self)
        self.titelLabel.move(230, 10)
        self.titelLabel.setStyleSheet(self.menuStyle)

    def listWidget(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 70, 510, 380)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['کاربر', 'غذا ها', 'جمع غذاها', 'مالیات', 'جمع کل', 'تاریخ'])
        self.tableWidget.setColumnWidth(5, 160)
        self.tableWidget.setStyleSheet(self.itemsListStyle)

        self.factors = dataBaseFunctions.gotFactors()

        for i in self.factors:
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(f'{i[1]}'))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(f'{i[2]}'))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f'{i[3]}'))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f'{i[4]}'))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(f'{i[5]}'))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f'{i[6]}'))


class ChangeAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setting()
        self.style()
        self.lineEdit()
        self.label()
        self.pushButton()

    def style(self):
        self.labelsStyle = 'font: 57 12pt "Dubai Medium";'
        self.lineEditStyle = 'font: 57 10pt "Dubai Medium";'
        self.errorLabelStyle = 'font: 57 8pt "Dubai Medium";color:red'

    def setting(self):
        self.setGeometry(510, 210, 450, 300)
        self.setMinimumSize(450, 300)
        self.setMaximumSize(450, 300)

        self.setWindowTitle('اطلاعات حساب')
        self.setWindowIcon(QIcon('./icons/edit (1).ico'))

    def label(self):
        self.nameLabel = QLabel('نام کاربری', self)
        self.nameLabel.setStyleSheet(self.labelsStyle)
        self.nameLabel.setGeometry(240, 98, 160, 35)

        self.passWordLabel = QLabel('رمز عبور', self)
        self.passWordLabel.setStyleSheet(self.labelsStyle)
        self.passWordLabel.setGeometry(240, 148, 160, 35)

        self.commentLabel = QLabel('یک نام و رمز عبور جدید وارد کنید', self)
        self.commentLabel.setStyleSheet(self.labelsStyle)
        self.commentLabel.move(110, 50)
        self.commentLabel.adjustSize()

        self.errorLabel = QLabel(self)
        self.errorLabel.setStyleSheet(self.errorLabelStyle)
        self.errorLabel.move(250, 210)

    def lineEdit(self):
        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.setStyleSheet(self.lineEditStyle)
        self.nameLineEdit.setGeometry(55, 100, 280, 35)

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setStyleSheet(self.lineEditStyle)
        self.passwordLineEdit.setGeometry(55, 150, 280, 35)

    def pushButton(self):
        self.savePushButton = QPushButton('ثبت', self)
        self.savePushButton.setStyleSheet(self.labelsStyle)
        self.savePushButton.setGeometry(180, 200, 60, 35)
        self.savePushButton.setShortcut('Return')
        self.savePushButton.clicked.connect(self.saveAdmin)

    def massegeBox(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText('آیا از اطلاعات وارد شده مطمئن هستید؟')
        self.msgBox.setWindowTitle('اخطار')
        self.msgBox.setStyleSheet(self.labelsStyle)
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.answer = self.msgBox.exec()
        if self.answer == QMessageBox.Ok:
            dataBaseFunctions.changeAdmin(self.nameLineEdit.text(), self.passwordLineEdit.text())
            self.close()
        else:
            pass

    # =====Function=====#
    def saveAdmin(self):
        if len(self.nameLineEdit.text()) > 0 and len(self.passwordLineEdit.text()) > 0:
            if len(self.passwordLineEdit.text()) > 5:
                self.massegeBox()
            else:
                self.errorLabel.setText('رمز عبور باید بیشتر از پنج کاراکتر باشد')
        else:
            self.errorLabel.setText('لطفا همه کادر های خالی را پر کنید')

        self.errorLabel.adjustSize()


def main():
    app = QApplication(sys.argv)
    wellcomePage = WellcomePage()
    wellcomePage.show()
    sys.exit(app.exec_())


main()
