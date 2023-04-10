# translator
自动翻译软件 

## 命令行
```text
usage: trans.exe [-h] [-p] [-H HOST] [-P PORT] [-V VTT_FILE] [-N NEW_FILE] [-E ENGINE] [-S SOURCE] [-T TARGET] [-M MODEL] [-C ENCODING]

翻译文本和文件

options:
  -h, --help            show this help message and exit
  -p, --proxy           是否开启代理，默认不开启
  -H HOST, --host HOST  代理服务器地址，默认 localhost
  -P PORT, --port PORT  代理服务器端口，默认 10808
  -V VTT_FILE, --vtt_file VTT_FILE
                        vtt文件路径
  -N NEW_FILE, --new_file NEW_FILE
                        翻译后的文件路径
  -E ENGINE, --engine ENGINE
                        翻译引擎，默认 google (未完成)
  -S SOURCE, --source SOURCE
                        源语言，默认 auto
  -T TARGET, --target TARGET
                        目标语言，默认 zh-CN
  -M MODEL, --model MODEL
                        翻译类型，默认 append (未完成)
  -C ENCODING, --encoding ENCODING
                        文件编码类型，默认 utf-8
```

