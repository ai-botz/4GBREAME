# (c) adarsh-goel
from pyrogram import Client
import pyromod.listen
from ..vars import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.25443947,
    api_hash=Var.ab4cd800dac7c9a36314ee83800adba8,
    bot_token=Var.6821223808:AAEZsS3AA3PlV3esA9VrZStEL_nSRLJs3ac,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}