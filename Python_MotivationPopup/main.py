from plyer import notification

myTitle = "This is a test!"
myMsg = "HELLO WORLD!"

notification.notify(
        title = myTitle,
        message = myMsg,
        timeout = 10,
        toast = False,
        app_icon = None,
    )