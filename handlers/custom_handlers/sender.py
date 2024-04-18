import time
from pybit.unified_trading import HTTP
from database.info import cryptocurencys, users
from loader import bot

def get_ratio(curency):
    session = HTTP(testnet=True)
    info = session.get_mark_price_kline(
        category="linear",
        symbol=curency,
        interval=60,
        limit=1,
    )
    return float(info['result'].get('list')[0][4]) / float(info['result'].get('list')[0][1]) * 100 - 100
def com():
    while True:
        for cur in cryptocurencys:
            ratio = get_ratio(cur)
            if abs(ratio) >= 5:
                for user in users:
                    bot.send_message(user, f'Криптовалюта {cur[:-4]} изменилась на {ratio}')
        time.sleep(60)