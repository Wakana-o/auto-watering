import time
import RPi.GPIO as GPIO

from gpio_control import GPIO_HL
from moisture_read import read_mcp3008, to_percent,print_humidity

moisture_check = True
while moisture_check == True:
    # MCP3008の0番ピン（CH0）からアナログ値を取得
    channel = 0
    value = read_mcp3008(channel)
    moisture_percent = to_percent(value)

    # 取得した値を表示
    #print(f"Today's soil humidity is {value} {round(moisture_percent)}%")
    print_humidity(value,moisture_percent)

    # もし湿度が20%以下ならGPIO_HLを実行
    if moisture_percent <= 20:
        GPIO_HL()
    else:
        moisture_check = False


    # 1秒間待機
    time.sleep(1)
