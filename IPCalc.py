import ipaddress
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout


class IPAddressCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # создаем виджеты
        self.ip_label = QLabel("IP-адрес:")
        self.ip_textbox = QLineEdit()
        self.mask_label = QLabel("Маска сети:")
        self.mask_combobox = QComboBox()
        self.mask_combobox.addItems([
            "255.255.255.255 (32)",
            "255.255.255.254 (31)",
            "255.255.255.252 (30)",
            "255.255.255.248 (29)",
            "255.255.255.240 (28)",
            "255.255.255.224 (27)",
            "255.255.255.192 (26)",
            "255.255.255.128 (25)",
            "255.255.255.0 (24)",
            "255.255.254.0 (23)",
            "255.255.252.0 (22)",
            "255.255.248.0 (21)",
            "255.255.240.0 (20)",
            "255.255.224.0 (19)",
            "255.255.192.0 (18)",
            "255.255.128.0 (17)",
            "255.255.0.0 (16)",
            "255.254.0.0 (15)",
            "255.252.0.0 (14)",
            "255.248.0.0 (13)",
            "255.240.0.0 (12)",
            "255.224.0.0 (11)",
            "255.192.0.0 (10)",
            "255.128.0.0 (9)",
            "255.0.0.0 (8)",
            "254.0.0.0 (7)",
            "252.0.0.0 (6)",
            "248.0.0.0 (5)",
            "240.0.0.0 (4)",
            "224.0.0.0 (3)",
            "192.0.0.0 (2)",
            "128.0.0.0 (1)",
            "0.0.0.0 (0)",
        ])
        self.calculate_button = QPushButton("Вычислить")
        self.result_label = QLabel()

        # создаем макет
        layout = QVBoxLayout()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_textbox)
        layout.addWidget(self.mask_label)
        layout.addWidget(self.mask_combobox)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # подключаем обработчики событий
        self.calculate_button.clicked.connect(self.calculate)

        # настраиваем окно
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Калькулятор IP-адресов")
        self.show()

    def calculate(self):
        # получаем значения из виджетов
        ip = self.ip_textbox.text()
        mask = self.mask_combobox.currentText().split()[0]
        # переводим значение нашего ip в двоичный вид
        ip_binary = ''.join([bin(int(x) + 256)[3:] for x in ip.split('.')])

        # создаем объект ipaddress.IPv4Network из IP-адреса и маски
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

        # выводим информацию о сети
        self.result_label.setText(f"""
            Сеть: {network.network_address}
            Широковещательный адрес: {network.broadcast_address}
            Маска сети: {network.netmask}
            Количество хостов: {network.num_addresses}
            IP адрес в двоичном виде: {ip_binary}
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = IPAddressCalculator()
    sys.exit(app.exec_())