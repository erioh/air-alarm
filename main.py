from jproperties import Properties
import pygame
from telethon import TelegramClient, events

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file, "utf-8")

TURN_ON = "усім пройти в укриття"
TURN_OFF = "ВІДБІЙ ТРИВОГИ"
api_id = configs.get("api_id").data
api_hash = configs.get("api_hash").data
channel = configs.get("channel").data

client = TelegramClient('session_name', api_id, api_hash)
pygame.mixer.init()
pygame.mixer.music.load("audio.wav")


def turn_on():
    pygame.mixer.music.play(-1)
    print("Alert is turned on")


def turn_off():
    pygame.mixer.music.stop()
    print("Alert is turned off")


@client.on(events.NewMessage(chats=(channel)))
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    if user_mess.find(TURN_ON) != -1:
        turn_on()
    if user_mess.find(TURN_OFF) != -1:
        turn_off()


client.start()
client.run_until_disconnected()