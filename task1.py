from user_management import load_or_generate_users
from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users: list[dict]) -> None:
    birthdays_per_week = defaultdict(list)

    # Отримуємо поточну дату системи для подальшого порівняння з датами народження користувачів
    today = datetime.today().date()

    # Проходимо по користувачам
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Конвертуємо дату народження до поточного року
        birthday_this_year = datetime.strptime(birthday, "%Y-%m-%d").date().replace(year=today.year)

        # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточним днем, щоб знайти дні народження на тиждень вперед
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, щоб дата народження була в межах наступного тижня
        if 0 <= delta_days < 7:
            # Визначаємо день тижня дня народження (переносимо на понеділок, якщо вихідний)
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_weekday in {"Saturday", "Sunday"}:
                birthday_weekday = "Monday"

            # Зберігаємо ім'я користувача в відповідний день тижня
            birthdays_per_week[birthday_weekday].append(name)

    # Виводимо результат
    print("Birthday greetings for this week:")
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    loaded_users = load_or_generate_users()
    get_birthdays_per_week(loaded_users)
