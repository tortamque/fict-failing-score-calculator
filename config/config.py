from pyrogram import Client
app = Client("*place_your_session_name_here*")

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "18",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "vstup.edbo.gov.ua",
    "Origin": "https://vstup.edbo.gov.ua",
    "Referer": "https://vstup.edbo.gov.ua/offer/986240/",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

positions_count = {
    "121": {
        "default": 165,
        "kvota1": 8,
        "kvota2": 16,
    },
    "123": {
        "default": 165,
        "kvota1": 8,
        "kvota2": 16,
    },
    "126": {
        "default": 245,
        "kvota1": 12,
        "kvota2": 24,
    },
    "121_zaochka": {
        "default": 10,
        "kvota1": 1,
        "kvota2": 1,
    },
}

speciality_ids = {
    "121": "986240",
    "123": "985216",
    "126": "988213",
    "121_zaochka": "986243"
}
