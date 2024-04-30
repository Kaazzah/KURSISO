import random
class Flight:
    def __init__(self, flight_number, from_location, to_location, departure_date, return_date, adults, children,
                 babies):
        self.flight_number = flight_number
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.return_date = return_date
        self.adults = adults
        self.children = children
        self.babies = babies
        self.aircraft_type = random.choice(["A-320ceo", "Б-737NG", "Суперджет", "Ан-24/Ан-26", "A-320neo",
                                            "A-320нео", "A-321нео", "Б-777", "Л-410", "A-330", "CRJ-100/200",
                                            "Б-737Classic", "Б-767", "ATR-72", "Е-170", "Dash 8 Q-200/300/400",
                                            "Б-757", "Як-42", "Як-40", "Б-747", "А-350", "Ан-28/Ан-38",
                                            "Dash 6 Twin Otter", "Е-190", "ATR-42", "Ан-74"])
        self.distance = self.calculate_distance()
        self.price = 0  # Цена будет рассчитана позже
        self.flight_name = f"{self.from_location}-{self.to_location}"
        self.ticket_name = f"{self.from_location}-{self.to_location}_{self.departure_date}"

    def calculate_distance(self):
        # Примерный расчет расстояния
        return random.randint(1100, 46000)


def calculate_ticket_price(flight, seat_type):
    # Примерный расчет цены билета
    base_prices = {
        "Business": 750,
        "Comfort": 1100,
        "Economy": 400,
        "First Class": 2000
    }

    # Примерные факторы
    aircraft_factors = {
        "A-320ceo": 1.1,
        "Б-737NG": 1.2,
        "Суперджет": 1.3,
        "Ан-24/Ан-26": 1.5,
        "А-320neo": 1.6,
        "Б-777": 1.7,
        "Л-410": 1.8,
        "А-330": 1.9,
        "CRJ-100/200": 2,
        "Б-737Classic": 2,
        "Б-767": 2.1,
        "ATR-72": 2.2,
        "Е-170": 2.2,
        "Dash 8 Q-200/300/400": 2.4,
        "Б-757": 2.5,
        "Як-42": 2.5,
        "Як-40": 2.7,
        "Б-747": 2.8,
        "А-350": 2.9,
        "Ан-28/Ан-38": 3.1,
        "Dash 6 Twin Otter": 3.1,
        "Е-190": 3.2,
        "ATR-42": 3.8,
        "Ан-74": 4
    }

    base_price = base_prices.get(seat_type, 300)  # Если тип места не найден, используем базовую цену 300
    aircraft_factor = aircraft_factors.get(flight.aircraft_type,
                                           1)  # Если тип самолета не найден, используем коэффициент 1

    # Примерный расчет цены с учетом коэффициентов
    price = base_price * aircraft_factor

    # Добавим случайное изменение цены в пределах 10%
    price *= random.uniform(0.90, 1)

    return round(price, 2)
