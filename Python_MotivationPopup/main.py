import random
from plyer import notification

My_Title = "Motivational quote of the day"

file = open(r"C:\Users\Eier\OneDrive\Koding\PrøveProsjekt\Python_MotivationPopup\quotes.txt", "r", encoding="mbcs" )
lines = file.readlines()

rndNum = random.randint(0, len(lines) - 1)
myMsg = lines[rndNum]

notification.notify(
        title = My_Title,
        message = myMsg,
        timeout = 10,
        toast = False,
        app_icon = None,
    )