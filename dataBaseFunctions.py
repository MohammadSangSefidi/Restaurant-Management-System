import sqlite3

def createTable ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql1 = """
        CREATE TABLE IF NOT EXISTS user(
        userId INTEGER PRIMARY KEY AUTOINCREMENT, 
        userName VARCHAR,
        password VARCHAR,
        isAdmin VARCHAR 
        )
        
    """
    sql2 =  """
        CREATE TABLE IF NOT EXISTS products(
        productId INTEGER PRIMARY KEY AUTOINCREMENT,
        productName VARCHAR,
        priceOfProduct INTEGER 
        )
    """
    sql3 = """
        CREATE TABLE IF NOT EXISTS appInfo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        adminMade VARCHAR,
        serviceCharge INTEGER ,
        paid INTEGER 
        )
    """
    sql4 = """
        CREATE TABLE IF NOT EXISTS factors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userName VARCHAR,
        foods VARCHAR ,
        totalFoods INTEGER ,
        paid INTEGER , 
        total INTEGER ,
        dataAndTime VARCHAR 
        )
    """

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)

    connect.commit()

    cursor = connect.cursor()
    sql5 = "INSERT INTO appInfo VALUES (1,'False',0,0);"
    check = checkAppInfo()

    if len(check) == 0:
        cursor.execute(sql5)
    else:
        pass

    connect.commit()
    connect.close()

def addUser (userName,password,isAdmin):
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "INSERT INTO user VALUES (NULL,?,?,?);"
    cursor.execute(sql,(userName, password, isAdmin))
    connect.commit()
    connect.close()

def saveItems (itemName,priceOfItem):
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "INSERT INTO products VALUES (NULL,?,?);"
    cursor.execute(sql,(itemName,priceOfItem))
    connect.commit()
    connect.close()

def saveAppInfo(adminMade,serviceCharge,paid):
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "UPDATE appInfo SET adminMade = ? , serviceCharge = ? , paid = ? WHERE id = 1"
    cursor.execute(sql,(adminMade,serviceCharge,paid))
    connect.commit()
    connect.close()

def checkAdminMade ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT adminMade FROM appInfo "
    cursor.execute(sql)

    adminMade = (list(cursor))
    adminMade = adminMade[0]
    adminMade = list(adminMade)
    adminMade = adminMade[0]


    connect.commit()
    connect.close()

    return adminMade

def gotAllUser ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT * FROM user "
    cursor.execute(sql)

    dictAllUser = []
    allUser = (list(cursor))
    for i in allUser:
        listUser = list(i)
        dictAllUser.append({'name':listUser[1],'password':listUser[2],'admin':listUser[3]})

    connect.commit()
    connect.close()
    return dictAllUser

def gotMenu ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT * FROM products "
    cursor.execute(sql)

    dictMenu = []
    menu = (list(cursor))
    for i in menu:
        listMenu = list(i)
        dictMenu.append({'name': listMenu[1], 'price': listMenu[2]})

    connect.commit()
    connect.close()
    return dictMenu

def checkAppInfo ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT * FROM appInfo "
    cursor.execute(sql)

    info = (list(cursor))
    connect.commit()
    connect.close()

    return info

def gotAppInfo ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT * FROM appInfo "
    cursor.execute(sql)

    info = (list(cursor))
    info = info[0]

    connect.commit()
    connect.close()

    return info

def saveFactor (userName,foods,totalFoods,paid,total,dataAndTime):
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "INSERT INTO factors VALUES (NULL,?,?,?,?,?,?);"
    cursor.execute(sql,(userName,foods,totalFoods,paid,total,dataAndTime))
    connect.commit()
    connect.close()

def changeAppInfo (serviceCharge,paid) :
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "UPDATE appInfo SET serviceCharge = ? , paid = ? WHERE id = 1 "
    cursor.execute(sql,(serviceCharge, paid))
    connect.commit()
    connect.close()

def clearItems ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "DELETE FROM products"
    cursor.execute(sql)
    connect.commit()
    connect.close()

def deleteUser ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "DELETE FROM user WHERE isAdmin = 'False'"
    cursor.execute(sql)
    connect.commit()
    connect.close()

def gotFactors ():
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "SELECT * FROM factors"
    cursor.execute(sql)

    factors = (list(cursor))

    connect.commit()
    connect.close()

    return factors

def changeAdmin (newUserName,newPassword):
    connect = sqlite3.connect('./appDataBase')
    cursor = connect.cursor()
    sql = "UPDATE user SET userName = ? , password = ? WHERE isAdmin = 'True' "
    cursor.execute(sql, (newUserName,newPassword))
    connect.commit()
    connect.close()

