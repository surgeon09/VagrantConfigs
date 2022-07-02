#!/usr/bin/env python3
import os, sys

param = sys.argv[1]
bash_command = [f'cd {param}', "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:   ', '')
        print(f'{param}/{prepare_result}')