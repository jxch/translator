import core.deep_google as dg
import util.proxy_util as pu


pu.enable()

res = dg.trans("Hello", source='auto', target='zh-CN')

print(res)