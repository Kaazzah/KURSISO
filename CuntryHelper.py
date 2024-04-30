import sqlite3

def populate_countries_database(data_file):
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                        id INTEGER PRIMARY KEY,
                        state TEXT,
                        capital TEXT
                    )''')

    with open(data_file, 'r', encoding='utf-8') as file:
        for line in file:
            country_info = line.strip().split('\t')
            if len(country_info) != 2:
                print(f"Ошибка в строке: {line}")
                continue

            state = country_info[0]
            capital = country_info[1]

            cursor.execute(
                "INSERT INTO countries (state, capital) VALUES (?, ?)",
                (state, capital))

    conn.commit()
    conn.close()

    print("База данных успешно заполнена!")

if __name__ == "__main__":
    populate_countries_database("countries1.txt")
