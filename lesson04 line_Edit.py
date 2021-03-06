import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)  # تفعيل النافذة من النظام

window = QWidget()  # إنشاء متغير من الفصيلة ويدجت (كائن رسومي)
window.setWindowTitle("PyQt5 Application Example")  # ضبط عنوان النافذة
window.setToolTip("This is the main window")  # ضبط الرسالة السحابية تظهر عند إشارة الفأرة Tool Tip
window.setWindowIcon(QIcon("PyQt.png"))  # تغيير أيقونة البرنامج بملف صورة يجب وضعها فى مجلد المشروع

# إحدى طرق ضبط أبعاد النافذة ومكان ظهرها على الشاشة
# window.resize(300, 100) # إعادة ضبط حجم النافذة (الرأسى ,الأفقى)
# window.move(200, 100) # ضبط إبتعاد النافذة عن الركن اليسار الأعلى للشاشة (البعد الرأسى , البعد الأفقى)
# طريقة أخرى لضبط أبعاد النافذة ومكان ظهورها
window.setGeometry(300, 200, 400,300)  # (الطول الرأسى ,الطول الأفقى ,البعد الرأسى , البعد الأفقى)

# إنشاء متغير صندوق الكتابة
txt = QLineEdit(window) # (داخل النافذة الأم)
txt2 = QLineEdit(window)
# يمكن استخدام نفس دوال ضبط النافذة
txt.setGeometry(100,100,200,40)
txt.setToolTip("This is txt box")
txt2.move(100,150)

txt.setPlaceholderText("Enter Your name") # ضبط قيمة إفتراضية تظهر داخل الصندوق كإرشاد
txt2.setPlaceholderText("Enter Password")
txt.setText("PyQt") # ضبط قيمة إفتراضية داخل الصندوق
txt2.setEchoMode(QLineEdit.Password) # إظهار الكتابة مخفية بنظام كلمة السر
print(txt.text()) # استيراد القيمة الكتوبة داخل الصندوق

window.show()  # إظهار النافذة

app.exec_()  # تنفيذ البرنامج (exec_) دالة تابعة لمكتبة Qt أما exec دالة تابعة للغة بايثون
