import core.trans_type as trans_type
from core.deep_google import trans
from map.trans_map import trans_map


def trans_vtt(file, new_file, model=trans_type.TransModel.append, engine=trans_type.Engine.deep_google, dict_map=None):
    for index, line in enumerate(file.readlines()):
        new_file.write(line)
        if 'WEBVTT' not in line and '-->' not in line and not line.isspace():
            t_text = trans(line)
            if dict_map:
                for k, v in trans_map[dict_map].items():
                    t_text = t_text.replace(k, v)
            new_file.write(' ' + t_text + '\n')
        print('\r', index + 1, end='', flush=True)
    print('\nend.')
