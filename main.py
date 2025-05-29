def показать_дату():
    from datetime import datetime
    сейчас = datetime.now()
    print(f"Дата сегодня: {сейчас.strftime('%A, %d %B %Y')}")
    print(f"Текущее время: {сейчас.strftime('%H:%M:%S')}")

показать_дату()
