from deep_translator import GoogleTranslator
from core.trans_type import Engine


def trans(text, source='auto', target='zh-CN', engine=Engine.deep_google):
    if engine == Engine.deep_google:
        return GoogleTranslator(source=source, target=target).translate(text)
    else:
        raise Exception('not support')
