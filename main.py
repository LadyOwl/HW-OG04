def показать_дату():
    from datetime import datetime
    сейчас = datetime.now()

    print(f"Сегодня: {сейчас.strftime('%A, %d %B %Y')}")
    print(f"Время: {сейчас.strftime('%H:%M:%S')}")
# Вызов второй функции
(показать_дату())

