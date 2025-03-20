import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 데이터베이스를 관리하는 클래스
class DatabaseManager:
    def __init__(self, db_name="ProductList.db"):
        """ 데이터베이스 초기화 및 연결 """
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        self.initialize_db()

    def initialize_db(self):
        """ 테이블이 없으면 생성 """
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Price INTEGER
            );
        """)
        self.con.commit()

    def add_product(self, name, price):
        """ 제품 추가 """
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        """ 제품 정보 수정 """
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        """ 제품 삭제 """
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def get_products(self):
        """ 모든 제품 정보 조회 """
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 파일 로드
form_class = uic.loadUiType("ProductList3.ui")[0]

# 메인 윈도우 클래스
class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DatabaseManager()
        
        # 테이블 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 엔터 입력 시 다음 컨트롤로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        
        # 테이블 더블 클릭 시 데이터 로드
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        
    def show_message(self, message):
        """ 오류 메시지 출력 """
        QMessageBox.warning(self, "입력 오류", message)

    def addProduct(self):
        """ 제품 추가 """
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        
        if not name or not price:
            self.show_message("제품 이름과 가격을 입력하세요.")
            return
        
        if not price.isdigit():
            self.show_message("가격은 숫자로 입력해야 합니다.")
            return
        
        self.db.add_product(name, int(price))
        self.getProduct()

    def updateProduct(self):
        """ 제품 수정 """
        prod_id = self.prodID.text().strip()
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        
        if not prod_id or not name or not price:
            self.show_message("제품 ID, 이름, 가격을 입력하세요.")
            return
        
        if not price.isdigit():
            self.show_message("가격은 숫자로 입력해야 합니다.")
            return
        
        self.db.update_product(int(prod_id), name, int(price))
        self.getProduct()

    def removeProduct(self):
        """ 제품 삭제 """
        prod_id = self.prodID.text().strip()
        
        if not prod_id:
            self.show_message("삭제할 제품 ID를 입력하세요.")
            return
        
        self.db.remove_product(int(prod_id))
        self.getProduct()

    def getProduct(self):
        """ 테이블 데이터 새로고침 """
        self.tableWidget.clearContents()
        products = self.db.get_products()
        row = 0 
        
        for item in products:
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1

    def doubleClick(self):
        """ 테이블에서 선택한 데이터를 입력 필드에 로드 """
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 프로그램 실행
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
