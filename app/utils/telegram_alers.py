import requests
from config import TELEGRAM_API_TOKEN, TELEGRAM_LOGGER_CHANNEL_ID


class Alerts:
    def __init__(self):
        self._headers = {
            "User-Agent": "Telegram bot, aiohttp client"
        }
        self._send_msg_base_url = "https://api.telegram.org/bot{token}/sendMessage"

    def send_message_to_telegram(self,
                                 message: str,
                                 ) -> bool:
        """Отправить сообщение пльзователю телеграм"""

        self._send_msg_base_url = self._send_msg_base_url.format(token=TELEGRAM_API_TOKEN)
        data = {
            "chat_id": TELEGRAM_LOGGER_CHANNEL_ID,
            "text": message,
            "parse_mode": "html",
        }
        try:
            response = requests.post(self._send_msg_base_url, data=data)
            if response.status_code != 200:
                return False
            return True
        except requests.RequestException as e:
            print(f'Ошибка: {e}')
            return False

        # try:
        #     async with aiohttp.ClientSession(headers=self._headers) as session:
        #         async with session.post(self._send_msg_base_url, data=data) as response:
        #             if response.status != 200:
        #                 return False
        #             return True
        # except aiohttp.ClientError as e:
        #     print(e)
        #     return False
