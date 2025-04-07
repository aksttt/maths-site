def get_terms_for_table():
    """Чтение карточек из файла (формат: слово;перевод)"""
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        next(f)  # Пропуск заголовка
        for line in f:
            line = line.strip()
            if line:
                term, translation = line.split(";")
                terms.append([term, translation])
    return terms


def write_term(new_term, new_translation):
    """Добавление новой карточки в файл"""
    new_line = f"{new_term};{new_translation}"
    with open("./data/terms.csv", "a", encoding="utf-8") as f:
        # Проверяем, не пустой ли файл
        if f.tell() == 0:  # Если файл пуст, записываем без переноса
            f.write(new_line)
        else:
            f.write(f"\n{new_line}")  # Добавляем перенос только если файл не пуст


def search_terms(query):
    """Поиск карточек по запросу"""
    results = []
    try:
        with open("./data/terms.csv", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:  # Пропускаем пустые строки
                    continue
                if ";" not in line:  # Пропускаем некорректные строки
                    continue
                term, translation = line.split(";", 1)
                if query.lower() in term.lower() or query.lower() in translation.lower():
                    results.append([term, translation])
    except FileNotFoundError:
        pass  # Файл не существует — возвращаем пустой список
    return results