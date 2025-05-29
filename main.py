def показать_дату():
    from datetime import datetime
    # Эта функция показывает текущую дату и время
    сейчас = datetime.now()
    print(f"Сегодня: {сейчас.strftime('%d.%m.%Y')}")
    print(f"Время: {сейчас.strftime('%H:%M:%S')}")

показать_дату()

