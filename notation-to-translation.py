#!/usr/bin/python3
from googletrans import Translator
import re, fileinput
## setup engine
translator = Translator(service_urls=['translate.google.cn'])
## setup RegularEx
pattern = re.compile(r'^([\s*]+//[\s*].*)|(//[\s*].*).*$')
## file input
for line in fileinput.input(['/Users/5swind/Downloads/python-notation-detecting/example/bgmchain/accounts/accounts.go'], inplace=1):
    if pattern.search(line):
        source = str(pattern.findall(line.strip()))
        text = source[source.find('//'):source.rfind('\'')]
        print(pattern.sub(text, translator.translate(text, dest='zh-CN').text))
    else:
        print(line)

