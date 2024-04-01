import deep_translator


def trans(text, source='auto', target='zh-CN', engine='GoogleTranslator'):
    return getattr(deep_translator, engine)(source=source, target=target).translate(text)
