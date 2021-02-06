# Dad Joke Notification code

from plyer import notification
import time


def notifyMe(title, message):
    notification.notify(
        title = title,          # the header, maybe it will say "Joke Time!"
        message = message,      # the joke
        app_icon = "C:\\Users\\oluch\\PycharmProjects\\NotFunnyDadHackProject\\laugh.ico",      # the little image that will pop up with the notification
        timeout = 15,           # how long the notification shows up for, here it is for 10 seconds
    )


if __name__ == '__main__':
    while  True:
        notifyMe("Joke time!", "How does a penguin build a house? \n Igloos it together")
        time.sleep(14400)        # to make the program run every 4 hours
