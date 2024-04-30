import sys
import random
import sqlite3

from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QListWidgetItem, QMessageBox, QDialog, QVBoxLayout, \
    QPushButton, QLineEdit, QLabel
from PySide6.QtCore import QTimer, Qt, Signal

from SkyFly import Ui_MainWindow
from TicketInfo import Ui_TicketInfo
from Flight import Flight, calculate_ticket_price
from airlines import airlines

class MainWindow(QMainWindow):
    search_triggered = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ButtonMoreInfo.clicked.connect(self.show_more_info)

        # Connect buttons
        self.ui.AdultPPlus.clicked.connect(self.increase_adults)
        self.ui.AdultPMinus.clicked.connect(self.decrease_adults)
        self.ui.ChildrenPPlus.clicked.connect(self.increase_children)
        self.ui.ChildrenPMinus.clicked.connect(self.decrease_children)
        self.ui.BabyPPlus.clicked.connect(self.increase_babies)
        self.ui.BabyPMinus.clicked.connect(self.decrease_babies)
        self.ui.ButtonSeacherTickets.clicked.connect(self.search_triggered.emit)

        # Connect radio buttons
        self.ui.RadButt_Business.toggled.connect(self.update_seat_type)
        self.ui.RadButt_Comfort.toggled.connect(self.update_seat_type)
        self.ui.RadButt_Economy.toggled.connect(self.update_seat_type)
        self.ui.RadButt_FirstClass.toggled.connect(self.update_seat_type)

        # Initial passenger counts
        self.adults = 0
        self.children = 0
        self.babies = 0
        self.update_passenger_counts()

        # Флаг для отслеживания, была ли дата уже обновлена
        self.date_initialized = False

        # Инициализация даты и времени только один раз при запуске
        self.initialize_date_time()

        # Update date and time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Connect to the database
        self.conn = sqlite3.connect('countries.db')
        self.cursor = self.conn.cursor()

        # Load countries and cities for autocomplete
        self.load_countries()

        # Initialize last search params
        self.last_search_params = None

        # Connect search signal
        self.search_triggered.connect(self.search_tickets)


    def load_countries(self):
        self.cursor.execute("SELECT state || ', ' || capital FROM countries")
        countries = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(countries, self.ui.Line_Where_ON)
        self.ui.Line_Where_ON.setCompleter(completer)
        completer = QCompleter(countries, self.ui.Line_Where_OFF)
        self.ui.Line_Where_OFF.setCompleter(completer)

    def get_selected_seat_type(self):
        if self.ui.RadButt_Business.isChecked():
            return "Business"
        elif self.ui.RadButt_Comfort.isChecked():
            return "Comfort"
        elif self.ui.RadButt_Economy.isChecked():
            return "Economy"
        elif self.ui.RadButt_FirstClass.isChecked():
            return "First Class"
        else:
            return "Unknown"

    def update_seat_type(self):
        if self.ui.RadButt_Business.isChecked():
            seat_type = "Бизнес"
        elif self.ui.RadButt_Comfort.isChecked():
            seat_type = "Комфорт"
        elif self.ui.RadButt_Economy.isChecked():
            seat_type = "Эконом"
        elif self.ui.RadButt_FirstClass.isChecked():
            seat_type = "Первый класс"
        else:
            seat_type = "Неизвестный"

        print(f"Тип обслуживания: {seat_type}")

    def initialize_date_time(self):
        if not self.date_initialized:
            current_time = datetime.now()  # Get current local time
            self.ui.WhenDate.setDate(current_time.date())
            self.ui.WhenDate.setTime(current_time.time())
            self.ui.WhenBackDate.setDate(current_time.date() + timedelta(days=1))  # Устанавливаем завтрашнюю дату
            self.ui.WhenBackDate.setTime(current_time.time())
            self.date_initialized = True

    def update_date_time(self):

        # Если фокус на обоих виджетах даты, то оставляем их значения неизменными
        if self.ui.WhenDate.hasFocus() and self.ui.WhenBackDate.hasFocus():
            return

        # Если фокус только на дате отправления, оставляем дату возвращения неизменной
        if self.ui.WhenDate.hasFocus():
            return_date = self.ui.WhenBackDate.dateTime().toPython()
            self.ui.WhenBackDate.setDateTime(return_date)

        # Если фокус только на дате возвращения, оставляем дату отправления неизменной
        elif self.ui.WhenBackDate.hasFocus():
            departure_date = self.ui.WhenDate.dateTime().toPython()
            self.ui.WhenDate.setDateTime(departure_date)

    def increase_adults(self):
        if self.adults < 10:
            self.adults += 1
        self.update_passenger_counts()

    def decrease_adults(self):
        if self.adults > 0:
            self.adults -= 1
        self.update_passenger_counts()

    def increase_children(self):
        if self.children < 10:
            self.children += 1
        self.update_passenger_counts()

    def decrease_children(self):
        if self.children > 0:
            self.children -= 1
        self.update_passenger_counts()

    def increase_babies(self):
        if self.babies < 10:
            self.babies += 1
        self.update_passenger_counts()

    def decrease_babies(self):
        if self.babies > 0:
            self.babies -= 1
        self.update_passenger_counts()

    def update_passenger_counts(self):
        self.ui.AdultPCounter.setValue(self.adults)
        self.ui.ChildrenPCounters.setValue(self.children)
        self.ui.BabyPCounter.setValue(self.babies)

        print(f"Количество пассажиров: {'Взрослые:', self.adults, 'Дети:', self.children, 'Малыши:', self.babies}")

    def search_tickets(self):
        from_location = self.ui.Line_Where_ON.text()
        to_location = self.ui.Line_Where_OFF.text()

        if not self.check_country_exists(from_location) or not self.check_country_exists(to_location):
            self.show_error_message("Ошибка ввода", "Одна или обе страны введены не корректно")
            return

        departure_date = self.ui.WhenDate.dateTime().toString("yyyy-MM-dd")
        return_date = self.ui.WhenBackDate.dateTime().toString("yyyy-MM-dd")

        # Проверяем, были ли введены новые данные по сравнению с предыдущим поиском
        current_search_params = (from_location, to_location, departure_date, return_date,
                                 self.adults, self.children, self.babies,
                                 self.get_selected_seat_type())

        if current_search_params == self.last_search_params:
            return

        self.last_search_params = current_search_params

        if not from_location or not to_location:
            self.show_error_message("Ошибка ввода", "Укажите точку вылета и точку прилета.")
            return

        if self.adults == 0:
            self.show_error_message("Ошибка ввода", "Вы должны выбрать хотя бы одного взрослого пассажира.")
            return

        if self.babies > 0 and self.adults == 0:
            self.show_error_message("Ошибка ввода", "Нельзя забронировать место для младенца без взрослого пассажира.")
            return

        if self.children > 0 and self.adults == 0:
            self.show_error_message("Ошибка ввода", "Нельзя забронировать место для ребенка без взрослого пассажира.")
            return

        # Включаем эффект загрузки
        self.ui.List_FoundTickets.clear()
        self.ui.List_FoundTickets.addItem("Идет поиск билетов...")
        self.ui.ButtonMoreInfo.setEnabled(False)

        ticket_flight = Flight("SomeFlightNumber", from_location, to_location, departure_date, return_date,
                               self.adults, self.children, self.babies)

        try:
            # Рассчитываем цену билета
            ticket_flight.price = calculate_ticket_price(ticket_flight, self.get_selected_seat_type())
        except Exception as e:
            self.show_error_message("Ошибка", str(e))
            return

        # Запускаем поиск билетов асинхронно
        QTimer.singleShot(2000, lambda: self.execute_search(ticket_flight))

    def check_country_exists(self, country_name):
        self.cursor.execute("SELECT COUNT(*) FROM countries WHERE state || ', ' || capital = ?", (country_name,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def execute_search(self, flight):
        tickets = self.generate_ticket_info(flight)
        self.ui.List_FoundTickets.clear()
        for ticket_info in tickets:
            item = QListWidgetItem(ticket_info)
            item.setFlags(item.flags() | Qt.ItemIsSelectable)
            item.setData(Qt.UserRole, ticket_info)  # Сохраняем всю информацию о билете в пользовательские данные элемента
            self.ui.List_FoundTickets.addItem(item)
        self.ui.ButtonMoreInfo.setEnabled(True)

    def generate_ticket_info(self, flight):
        tickets = []
        random_count = random.randint(1, 10)
        for i in range(random_count):
            flight_number = f"{i + 1}"
            company_name = random.choice(airlines)  # Случайный выбор названия авиакомпании
            flight_info = f"{flight_number}, {company_name} , {flight.from_location} - {flight.to_location} "
            tickets.append(flight_info)
        return tickets

    def show_more_info(self):
        selected_item = self.ui.List_FoundTickets.currentItem()
        if selected_item:
            ticket_details = selected_item.data(Qt.UserRole)
            ticket_info_dialog = TicketInfoDialog(ticket_details, self.ui.WhenDate.dateTime())
            ticket_info_dialog.exec()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите билет для просмотра подробной информации.")

    def show_error_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()


class TicketInfoDialog(QDialog):
    ticket_count = None  # Переменная для хранения количества билетов

    def __init__(self, ticket_info, flight_date):
        super(TicketInfoDialog, self).__init__()
        self.ui = Ui_TicketInfo()
        self.ui.setupUi(self)
        self.setWindowTitle("Информация о билете")
        self.flight_date = flight_date  # Сохраняем дату полета
        self.setup_ticket_info(ticket_info)

        # Создаем кнопку для выбора класса обслуживания
        self.service_button = self.ui.ButtonSelectService
        self.service_button.clicked.connect(self.open_service_class_dialog)

        # Поле для отображения выбранного класса обслуживания
        self.service_line_edit = self.ui.lineEdit_2
        self.service_line_edit.setReadOnly(True)

        # Создаем кнопку для выбора банка
        self.payment_button = self.ui.ButtonSelectService_2
        self.payment_button.clicked.connect(self.open_payment_dialog)

        # Поле для отображения выбранного банка
        self.payment_line_edit = self.ui.lineEdit_4
        self.payment_line_edit.setReadOnly(True)

        # Переменная для хранения количества билетов
        self.ticket_count = 0

        # Переменная для хранения выбранного класса обслуживания
        self.selected_service_class = "Эконом"

        self.total_cost_line_edit = self.ui.lineEdit_3

        # Вычисляем общую стоимость билетов
        self.calculate_total_cost()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.calculate_total_cost)
        self.timer.start(5000)

        # Создаем кнопку "Купить билет"
        self.buy_ticket_button = self.ui.Button_GoBuyTicket
        self.buy_ticket_button.clicked.connect(self.buy_ticket)

        # Создаем кнопку "Закрыть окно"
        self.exit_button = self.ui.Button_Exit
        self.exit_button.clicked.connect(self.close)

        self.ticket_count = TicketInfoDialog.ticket_count  # Количество билетов
        self.max_ticket_count = self.ticket_count  # Максимально доступное количество билетов


        self.ui.lineEdit.textChanged.connect(self.update_ticket_count)



    def setup_ticket_info(self, ticket_info):
        # Разбиваем строку на части по символу ","
        ticket_parts = ticket_info.split(",")

        # Проверяем, что количество частей равно ожидаемому (трем частям)
        if len(ticket_parts) >= 3:  # Мы ожидаем как минимум три части
            company_name = ticket_parts[1].strip()  # Название компании из второй части
            route = ",".join(ticket_parts[2:]).strip()  # Маршрут из оставшихся частей

            # Устанавливаем название компании
            self.ui.labelCompanyName.setText(company_name)

            # Попытаемся разделить маршрут на места отправления и назначения
            route_parts = route.split(" - ")
            if len(route_parts) == 2:
                from_location, to_location = route_parts
                # Устанавливаем места отправления и назначения
                self.ui.labelWhere.setText(from_location.strip())
                self.ui.labelWhere_2.setText(to_location.strip())
            else:
                print("Ошибка: Неправильный формат данных в маршруте")
        else:
            print("Ошибка: Неправильный формат данных в ticket_info")

        # Если количество билетов еще не установлено, устанавливаем его
        if TicketInfoDialog.ticket_count is None:
            # Генерация случайного количества билетов от 1 до 25
            TicketInfoDialog.ticket_count = random.randint(1, 25)

        # Устанавливаем количество билетов
        self.ui.label_7.setText(str(TicketInfoDialog.ticket_count))

        # Генерация номера рейса
        flight_number = self.generate_flight_number(ticket_parts[1].strip())
        self.ui.label.setText(flight_number)

        # Устанавливаем дату полета без времени
        self.ui.labelWhen.setText(self.flight_date.toString("yyyy-MM-dd"))

        # Генерация случайного времени для отправления
        departure_hour = random.randint(0, 23)
        departure_minute = random.randint(0, 3) * 15  # Минуты кратны 15
        departure_time = f"{departure_hour:02d}:{departure_minute:02d}"
        self.ui.label_5.setText(departure_time)

        # Генерация случайного времени для прибытия
        arrival_hour = (departure_hour + 4) % 24  # Прибытие через 4 часа
        arrival_minute = random.randint(0, 3) * 15  # Минуты кратны 15
        arrival_time = f"{arrival_hour:02d}:{arrival_minute:02d}"
        self.ui.label_6.setText(arrival_time)

    def generate_flight_number(self, company_name):
        # Получаем первые два символа названия авиакомпании и генерируем случайное трех- или четырехзначное число
        airline_code = company_name[:2].upper()
        flight_number = random.randint(100, 9999)
        return f"{airline_code}{flight_number}"

    def open_service_class_dialog(self):
        dialog = ServiceClassDialog()
        if dialog.exec() == QDialog.Accepted:
            self.service_line_edit.setText(dialog.selected_class)
            self.selected_service_class = dialog.selected_class  # Обновляем выбранный класс
            self.calculate_total_cost()

    def open_payment_dialog(self):
        dialog = PaymentDialog()
        if dialog.exec() == QDialog.Accepted:
            self.payment_line_edit.setText(dialog.selected_bank)
            self.calculate_total_cost()

    def calculate_total_cost(self):
        if self.ticket_count is not None:
            base_cost_per_ticket = 1000  # Стандартная цена билета
            service_class_cost = 0  # Стоимость класса обслуживания

            # Устанавливаем стоимость в зависимости от выбранного класса обслуживания
            if self.selected_service_class == "Эконом":
                service_class_cost = 500
            elif self.selected_service_class == "Бизнес":
                service_class_cost = 2500
            elif self.selected_service_class == "Комфорт":
                service_class_cost = 2000
            elif self.selected_service_class == "Первый класс":
                service_class_cost = 3500

            total_cost = self.ticket_count * (base_cost_per_ticket + service_class_cost)
            self.total_cost_line_edit.setText(str(total_cost))

    def set_ticket_count(self, ticket_count):
        self.ticket_count = ticket_count
        self.calculate_total_cost()

    def set_service_class(self, service_class):
        self.selected_service_class = service_class
        self.calculate_total_cost()

    def buy_ticket(self):
        if self.ticket_count == 0:
            QMessageBox.warning(self, "Ошибка", "Количество билетов не может быть равно нулю!")
            return
        if self.total_cost_line_edit.text() == '0':
            QMessageBox.warning(self, "Ошибка", "Общая стоимость не может быть равна нулю!")
            return

        ticket_count = self.ticket_count  # Получаем количество выбранных билетов
        ticket_details = f"Количество билетов: {ticket_count}\n" \
                         f"Дата полета: {self.flight_date.toString('dd-MM-yyyy')}\n" \
                         f"Класс обслуживания: {self.selected_service_class}\n" \
                         f"Общая стоимость: {self.total_cost_line_edit.text()}"

        bank_info = self.payment_line_edit.text()

        # Передаем информацию о количестве билетов в диалоговое окно оплаты билета
        buy_ticket_dialog = BuyTicketDialog(ticket_details, bank_info, ticket_count)
        buy_ticket_dialog.exec()

    def update_ticket_count(self, text):
        try:
            new_ticket_count = int(text)  # Пытаемся преобразовать текст в число
            if new_ticket_count > self.max_ticket_count:
                self.ticket_count = self.max_ticket_count  # Устанавливаем максимально доступное количество билетов
                self.ui.lineEdit.setText(str(self.max_ticket_count))  # Обновляем значение в lineEdit
            else:
                self.ticket_count = new_ticket_count  # Иначе устанавливаем новое значение
            self.calculate_total_cost()  # После обновления количества билетов пересчитываем общую стоимость
        except ValueError:
            pass  # Если не удалось преобразовать в число, игнорируем и оставляем текущее значение ticket_count
class ServiceClassDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор класса обслуживания")

        self.economy_button = QPushButton("Эконом")
        self.business_button = QPushButton("Бизнес")
        self.comfort_button = QPushButton("Комфорт")
        self.first_class_button = QPushButton("Первый класс")

        self.economy_button.clicked.connect(self.select_economy)
        self.business_button.clicked.connect(self.select_business)
        self.comfort_button.clicked.connect(self.select_comfort)
        self.first_class_button.clicked.connect(self.select_first_class)

        layout = QVBoxLayout()
        layout.addWidget(self.economy_button)
        layout.addWidget(self.business_button)
        layout.addWidget(self.comfort_button)
        layout.addWidget(self.first_class_button)

        self.setLayout(layout)

    def select_economy(self):
        self.selected_service_class = "Эконом"
        self.calculate_total_cost()
        self.accept()

    def select_business(self):
        self.selected_class = "Бизнес"
        self.accept()

    def select_comfort(self):
        self.selected_class = "Комфорт"
        self.accept()

    def select_first_class(self):
        self.selected_class = "Первый класс"
        self.accept()

class PaymentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор банка")

        self.bank1_button = QPushButton("Банк 1")
        self.bank2_button = QPushButton("Банк 2")
        self.bank3_button = QPushButton("Банк 3")
        self.bank4_button = QPushButton("Банк 4")

        self.bank1_button.clicked.connect(self.select_bank1)
        self.bank2_button.clicked.connect(self.select_bank2)
        self.bank3_button.clicked.connect(self.select_bank3)
        self.bank4_button.clicked.connect(self.select_bank4)

        layout = QVBoxLayout()
        layout.addWidget(self.bank1_button)
        layout.addWidget(self.bank2_button)
        layout.addWidget(self.bank3_button)
        layout.addWidget(self.bank4_button)

        self.setLayout(layout)

    def select_bank1(self):
        self.selected_bank = "Банк 1"
        self.accept()

    def select_bank2(self):
        self.selected_bank = "Банк 2"
        self.accept()

    def select_bank3(self):
        self.selected_bank = "Банк 3"
        self.accept()

    def select_bank4(self):
        self.selected_bank = "Банк 4"
        self.accept()

class BuyTicketDialog(QDialog):
    def __init__(self, ticket_details, bank_info, ticket_count):
        super(BuyTicketDialog, self).__init__()
        self.setWindowTitle("Оплата билета")

        layout = QVBoxLayout()

        # Добавляем метку с информацией о билете, включая количество билетов
        ticket_label = QLabel(ticket_details)
        layout.addWidget(ticket_label)

        # Добавляем метку с информацией о выбранном банке
        bank_label = QLabel(f"Оплата через банк: {bank_info}")
        layout.addWidget(bank_label)

        # Создаем кнопку для подтверждения покупки билета
        confirm_button = QPushButton("Подтвердить покупку")
        confirm_button.clicked.connect(self.confirm_purchase)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

        # Сохраняем количество билетов для использования при подтверждении покупки
        self.ticket_count = ticket_count

    def confirm_purchase(self):
        # Добавляем сообщение о подтверждении покупки
        QMessageBox.information(self, "Подтверждение покупки", "Билет успешно приобретен!")
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
