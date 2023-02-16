from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *

class RegWindow(QMainWindow):
  def __init__(self)->None:
    super().__init__()
    self.setUpWindow()
  def setUpWindow(self):
    self.lbl_name = QLabel("Ismingizni kiriting: ")
    self.name_edit = QLineEdit()
    self.name_edit.setPlaceholderText("ismingizni kiriting")
    layout = QHBoxLayout()
    layout.addWidget(self.lbl_name)
    layout.addWidget(self.name_edit)

    layout_em = QHBoxLayout()
    self.lbl_email = QLabel("Emailingizni kiriting: ")
    self.email_edit = QLineEdit()
    self.email_edit.setPlaceholderText("ism@gmail.com")
    layout_em.addWidget(self.lbl_email)
    layout_em.addWidget(self.email_edit)

    layout_pas = QHBoxLayout()
    self.lbl_pass = QLabel("Parolingizni kiriting: ")
    self.pass_edit = QLineEdit()
    self.pass_edit.setPlaceholderText("parolni kiriting: ")
    self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
    layout_pas.addWidget(self.lbl_pass)
    layout_pas.addWidget(self.pass_edit)

    lay_id = QHBoxLayout()
    self.lbl_id = QLabel("Telegram id kiriting: ")
    self.tid_edit = QLineEdit()
    self.tid_edit.setPlaceholderText("123456789")
    lay_id.addWidget(self.lbl_id)
    lay_id.addWidget(self.tid_edit)

    self.id_check = QCheckBox("Men telegram botdan royhatdan o'tganman")
    self.id_check.setChecked(False)

    self.send_btn = QPushButton("Royhatdan o'tish")
    self.can_btn = QPushButton("Bekor qilish")
    btn_lay = QHBoxLayout()
    btn_lay.addWidget(self.send_btn)
    btn_lay.addWidget(self.can_btn)
    style = """
    QPushButton {
      border-radius: 30px;
      background-color: green;
    }
    QPushButton::hover{
      border:1px solid white;
      border-radius:10px;
    }
    
    """
    self.send_btn.setStyleSheet(style)
    self.can_btn.setStyleSheet(style)

    v_lay = QVBoxLayout()
    
    v_lay.addLayout(layout)
    v_lay.addLayout(layout_em)
    v_lay.addLayout(layout_pas)
    v_lay.addLayout(lay_id)


    v_lay.addStretch(4)
    v_lay.addWidget(self.id_check)

    v_lay.addLayout(btn_lay)
    
    center = QWidget()
    center.setLayout(v_lay)
    self.setCentralWidget(center)

    
