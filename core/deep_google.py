from deep_translator import GoogleTranslator
import socket
import socks
from core.trans_type import Engine

socks.setdefaultproxy(socks.SOCKS5, "localhost", 10808)
socket.socket = socks.socksocket


def trans(text, source='auto', target='zh-CN', engine=Engine.deep_google):
    if engine == Engine.deep_google:
        return GoogleTranslator(source=source, target=target).translate(text)
    else:
        raise Exception('not support')
