import core.vtt_trans as vtt_trans

f = open(
    '../res/Al Brooks - Emini End of Day Review for Monday April 3 2023 (Transcribed on 10-Apr-2023 13-58-29).vtt',
    mode='r', encoding='utf-8')
new_f = open(
    '../res/Al Brooks - Emini End of Day Review for Monday April 3 2023 (Transcribed on 10-Apr-2023 13-58-29) - CN.vtt',
    mode='w', encoding='utf-8')

vtt_trans.trans_vtt(f, new_f)

f.close()
new_f.close()
