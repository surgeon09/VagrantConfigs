# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"
# Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.

#vagrant@vagrant:~$ type cd
#cd is a shell builtin - встроенная функция в оболочку
#может работать по разному в зависимости от оболочки (Bourne shell, csh, tcsh, bash и в DOS)
#если бы она была внешняя, то необходимо было бы дополнительно подключать свою оболочку для получения желаемого еффекта поведения (например: в сессии DOS (общепринятый «домашний каталог» отсутствует и зависит от конкретной реализации)), также cd даёт различный эффект в разных операционных системах, поэтому для удобства cd является встроенной функицей в каждую оболочку.

# Какая альтернатива без pipe команде grep <some_string> <some_file> | wc -l? man grep поможет в ответе на этот вопрос. Ознакомьтесь с документом о других подобных некорректных вариантах использования pipe.
#vagrant@vagrant:~$ cat  /var/log/syslog | grep error - чтение и поиск в нем ключевого слова error
#vagrant@vagrant:~$ cat  /var/log/syslog | grep -i error - чтение и поиск в нем ключевого слова error невзирая на регистр
#Можно файл передать утилите grep в качестве аргумента:
#vagrant@vagrant:~$ grep -i error /var/log/syslog

#Можно выполнять поиск по маске, по набору файлов:
#vagrant@vagrant:~$ sudo grep -i error /var/log/*
#grep: /var/log/journal: Is a directory - может выдавать ошибку что grep не может прочитать директорию 
#vagrant@vagrant:~$ sudo grep -ir error /var/log/* - ключ -ir дает возможность заглянуть в каждую директорию и найти там, при этом ошибок что он не может прочитать директорию не будет
#vagrant@vagrant:~$ sudo grep -ir error /var/log/* | grep RAS: - выведет все строки с ключевым словом RAS:
#vagrant@vagrant:~$ sudo grep -ir error /var/log/* | grep RAS: | wc -l - выведет все строки с ключевым словом RAS: и подсчитает кол-во таких строк
#vagrant@vagrant:~$ cat /var/log/syslog | grep -A 2 error - выведет 2 строки после найденного вхождения
#vagrant@vagrant:~$ cat /var/log/syslog | grep -B 2 error - выведет 2 строки до найденного вхождения
#vagrant@vagrant:~$ cat /var/log/syslog | grep -С 2 error - выведет 2 строки до и после найденного вхождения


# Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?
#systemd(1)─┬─VBoxService(893)─┬─{VBoxService}(895)
           │                  ├─{VBoxService}(896)
           │                  ├─{VBoxService}(897)
           │                  ├─{VBoxService}(898)
           │                  ├─{VBoxService}(899)
           │                  ├─{VBoxService}(900)
           │                  ├─{VBoxService}(901)
           │                  └─{VBoxService}(902)


# Как будет выглядеть команда, которая перенаправит вывод stderr ls на другую сессию терминала?

#vagrant@vagrant:~$ tty
#/dev/pts/0
#vagrant@vagrant:~$ ls -l 14.file 2>/dev/pts/1

#vagrant@vagrant:~$ tty
#/dev/pts/1
#vagrant@vagrant:~$ ls: cannot access '14.file': No such file or directory


# Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.

#vagrant@vagrant:~$ cat 11.file
#insert to 14.file
#vagrant@vagrant:~$ cat 14.file
#cat: 14.file: No such file or directory
#vagrant@vagrant:~$ less <11.file >14.file
#vagrant@vagrant:~$ cat 14.file
#insert to 14.file

# Получится ли находясь в графическом режиме, вывести данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?

#vagrant@vagrant:~$ tty
#/dev/pts/0
#vagrant@vagrant:~$ echo "Hello!" > /dev/tty1-7 (By default Ubuntu has 7 tty's.)

#vagrant@vagrant:~$ ls -l /dev/std*
#lrwxrwxrwx 1 root root 15 Mar 27 11:41 /dev/stderr -> /proc/self/fd/2
#lrwxrwxrwx 1 root root 15 Mar 27 11:41 /dev/stdin -> /proc/self/fd/0
#lrwxrwxrwx 1 root root 15 Mar 27 11:41 /dev/stdout -> /proc/self/fd/1
#bash 5>&1 - созданный файловый дескриптор 5 получит поток stdout
#echo netology > /proc/$$/fd/5 - выведет "netology" т.к. поток stout был перенаправлен на предыдущем шаге
