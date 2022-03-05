import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from jproperties import Properties
from telethon import TelegramClient, events

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file, "utf-8")

substring_to_turn_alarm_on = configs.get("turn_on").data
substring_to_turn_alarm_off = configs.get("turn_off").data
api_id = 2040
api_hash = 'b18441a1ff607e10a989891a5462e627'
channel = configs.get("channel").data
client = TelegramClient('session_name', api_id, api_hash)
pygame.mixer.init()
pygame.mixer.music.load("audio.wav")


def turn_alarm_on():
    pygame.mixer.music.play(-1)
    print("Alert is turned on")


def turn_alarm_off():
    pygame.mixer.music.stop()
    print("Alert is turned off")


@client.on(events.NewMessage(chats=channel))
async def normal_handler(event):
    message = event.message.to_dict()['message']
    print(message)
    if substring_to_turn_alarm_on.casefold() in message.casefold():
        turn_alarm_on()
    if substring_to_turn_alarm_off.casefold() in message.casefold():
        turn_alarm_off()


client.start()
print("Application is started")
client.run_until_disconnected()
