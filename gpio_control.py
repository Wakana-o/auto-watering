#moisture_read.py
import spidev  # SPIデバイス用のモジュール
import time    # time.sleep用のモジュール

# SPIデバイスのインスタンスを作成
spi = spidev.SpiDev()
# MCP3008と接続されたSPIデバイスを開く
spi.open(0, 0)
spi.max_speed_hz = 100000

def read_mcp3008(ch):
    # MCP3008に対してアナログ値を取得するためのコマンドを送信
    cmd = [1, (8 + ch) << 4, 0]
    reply = spi.xfer2(cmd)

    # 取得したデータからアナログ値を計算
    value = ((reply[1] & 3) << 8) + reply[2]
    return value

def to_percent(value):
    # アナログ値からパーセント値に変換
    zero = 900
    hundred = 410
    percent = (value - zero) / (hundred - zero) * 100

    return percent

# MCP3008の0番ピン（CH0）からアナログ値を取得
channel = 0
value = read_mcp3008(channel)
moisture_percent = to_percent(value)

def print_humidity(value,moisture_percent):
    # 取得した値を表示
    print(f"Today's soil humidity is {value} {round(moisture_percent)}%")
    # 1秒間待機
    time.sleep(1)

#print_humidity(value,moisture_percent)
