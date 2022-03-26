# Какие ресурсы выделены по-умолчанию?
#- Оперативная память: 1024мб
#- Процессоры: 2
#- Порядок загрузки: Жесткий диск, Оптический диск
#- Ускорение: VT-x/AMD-V,Nested Paging, PAE/NX, Паравиртуализация KM
#- Видеопамять: 4мб
#- Графический контроллер: VBoxVGA
#- Порт сервера удаленного дисплея: 5902
#- Запись: Выключена
#- Контроллер: IDE Controller
#- Контроллер: SATA Controller
#- SATA порт 0: ubuntu-20.04-amd64-disk001.vmdk (Обычный, 64,00ГБ)

# Как добавить оперативной памяти или ресурсов процессора виртуальной машине?
#config.vm.provider "virtualbox" do |v|
	#v.memory = 4096
	#v.cpus = 4
#end
#vagrant reload

# Какой переменной можно задать длину журнала history?
#HISTSIZE=1000

# На какой строчке manual это описывается?
#line 3234

# Что делает директива ignoreboth в bash?
#Значение ignoreboth является сокращением для ignorespace и ignoredups, т.е. если список значений 
#включает в себя ignorespace, строки, начинающиеся с символа пробела, не сохраняются в списке истории и 
#значение ignoredups приводит к тому, что строки, соответствующие предыдущей записи истории, не 
#сохраняются.

# В каких сценариях использования применимы скобки {} и на какой строчке man bash это описано?
#{ и } являются зарезервированными словами и должны встречаться там, где разрешено распознавание 
#зарезервированного слова
#lines 186 (RESERVED WORDS) and 280 (Compound Commands - { list; })

# С учётом ответа на предыдущий вопрос, как создать однократным вызовом touch 100000 файлов? Получится 
# ли аналогичным образом создать 300000? Если нет, то почему?
#vagrant@vagrant:~/test$ touch {1..100000}.txt
#vagrant@vagrant:~/test$ rm {1..100000}.txt
#vagrant@vagrant:~/test$ touch {1..200000}.txt
#-bash: /usr/bin/touch: Argument list too long
#vagrant@vagrant:~/test$ touch {1..300000}.txt
#-bash: /usr/bin/touch: Argument list too long
#vagrant@vagrant:~/test$
#100000 создать дал, а 300000 нет - argument list too long: touch
<!--  -->

# В man bash поищите по /\[\[. Что делает конструкция [[ -d /tmp ]]?
#При использовании с [[ операторы < и > сортируются лексикографически с использованием текущей локали, 
#т.е. конструкция означает, что в текущей локали -d - Истинно, если файл существует и является каталогом /tmp

# Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:
#vagrant@vagrant:~$ mkdir /tmp/new_path_dir/
#vagrant@vagrant:~$ cp /bin/bash /tmp/new_path_dir/
#vagrant@vagrant:~$ PATH=/tmp/new_path_dir/:$PATH
#vagrant@vagrant:~$ type -a bash
#bash is /tmp/new_path_dir/bash
#bash is /usr/bin/bash
#bash is /bin/bash
