import argparse
import socket
import socks
import core.trans_type as trans_type
import core.vtt_trans as vtt_trans
import sys

parser = argparse.ArgumentParser(description='翻译文本和文件')
parser.add_argument('-p', '--proxy', action='store_true', help="是否开启代理，默认不开启")
parser.add_argument('-H', '--host', help='代理服务器地址，默认 localhost', default="localhost")
parser.add_argument('-P', '--port', help='代理服务器端口，默认 10808', default=10808)

parser.add_argument('-V', '--vtt_file', help='vtt文件路径')
parser.add_argument('-N', '--new_file', help='翻译后的文件路径')
parser.add_argument('-E', '--engine', help='翻译引擎，默认 google (未完成)', default=trans_type.Engine.deep_google)
parser.add_argument('-S', '--source', help='源语言，默认 auto', default='auto')
parser.add_argument('-T', '--target', help='目标语言，默认 zh-CN', default='zh-CN')
parser.add_argument('-M', '--model', help='翻译类型，默认 append (未完成)', default=trans_type.TransModel.append)
parser.add_argument('-C', '--encoding', help='文件编码类型，默认 utf-8', default='utf-8')
args = parser.parse_args()

if args.proxy:
    socks.setdefaultproxy(socks.SOCKS5, args.host, args.port)
    socket.socket = socks.socksocket

if args.vtt_file:
    with open(args.vtt_file, mode='r', encoding=args.encoding) as of:
        with open(args.new_file, mode='a', encoding=args.encoding) as nf:
            vtt_trans.trans_vtt(of, nf, args.model, args.engine)

if len(sys.argv) == 1:
    print(str(parser.print_usage()).replace('None', ''))
