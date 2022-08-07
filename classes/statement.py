class Statement:
    def __init__(self, fio: str, priority: str, kb: str, kvota: int):
        self.__fio = fio
        self.__priority = int(priority)
        self.__kb = float(kb)
        self.__kvota = kvota

    def get_priority(self):
        return self.__priority

    def get_kb(self):
        return self.__kb

    def get_kvota(self):
        return self.__kvota

    def __str__(self):
        return f"{self.__kb} ({self.__fio}, пріоритет: {self.__priority}, квота: {self.__kvota})"



