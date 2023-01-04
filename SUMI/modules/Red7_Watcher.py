""" Team Red7 """

from .. import telethn as Red7
from telethon import events 

try:
  from extra import Red7_Watch_telethon
except:
  import os
  os.system("pip3 install pyRiZoeLX==1.0.5")
  from extra import Red7_Watch_telethon


@Red7.on(events.NewMessage(incoming=True))
async def Red7_Scanner(message):
    await Red7_Watch_telethon(Red7, message)
