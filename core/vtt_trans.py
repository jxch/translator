import core.trans_type as trans_type
from core.deep_google import trans
from util.file_util import iter_count


def trans_vtt(file, new_file, model=trans_type.TransModel.append, engine=trans_type.Engine.deep_google):
    for index, line in enumerate(file.readlines()):
        new_file.write(line)
        if 'WEBVTT' not in line and '-->' not in line and not line.isspace():
            t_text = trans(line).replace('酒吧', 'K线')
            new_file.write(' ' + t_text + '\n')
        print('\r', index + 1, end='', flush=True)
