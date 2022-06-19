# Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

<!-- 1.Какой системный вызов делает команда cd? В прошлом ДЗ мы выяснили, что cd не является самостоятельной программой, это shell builtin, поэтому запустить strace непосредственно на cd не получится. Тем не менее, вы можете запустить strace на /bin/bash -c 'cd /tmp'. В этом случае вы увидите полный список системных вызовов, которые делает сам bash при старте. Вам нужно найти тот единственный, который относится именно к cd. Обратите внимание, что strace выдаёт результат своей работы в поток stderr, а не в stdout. -->
#stat("/tmp", {st_mode=S_IFDIR|S_ISVTX|0777, st_size=4096, ...}) = 0
#chdir("/tmp") - непосредственная смена директории

<!-- 2.Попробуйте использовать команду file на объекты разных типов на файловой системе. Например:
vagrant@netology1:~$ file /dev/tty
/dev/tty: character special (5/0)
vagrant@netology1:~$ file /dev/sda
/dev/sda: block special (8/0)
vagrant@netology1:~$ file /bin/bash
/bin/bash: ELF 64-bit LSB shared object, x86-64
Используя strace выясните, где находится база данных file на основании которой она делает свои догадки. -->
#openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3

<!-- 3.Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удален (deleted в lsof), однако возможности сигналом сказать приложению переоткрыть файлы или просто перезапустить приложение – нет. Так как приложение продолжает писать в удаленный файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе). -->
#echo '' >/proc/1448/fd/4

<!-- 4.Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)? -->
#Процесс при завершении (как нормальном, так и в результате не обрабатываемого сигнала) освобождает все 
#свои ресурсы и становится «зомби» — пустой записью в таблице процессов, хранящей статус завершения, 
#предназначенный для чтения родительским процессом.
#Зомби-процесс существует до тех пор, пока родительский процесс не прочитает его статус с помощью 
#системного вызова wait(), в результате чего запись в таблице процессов будет освобождена.

<!-- 5.В iovisor BCC есть утилита opensnoop:
root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop
/usr/sbin/opensnoop-bpfcc
На какие файлы вы увидели вызовы группы open за первую секунду работы утилиты? Воспользуйтесь пакетом bpfcc-tools для Ubuntu 20.04. Дополнительные сведения по установке. -->

#root@vagrant:~# /usr/sbin/opensnoop-bpfcc
#PID    COMM               FD ERR PATH
#887    vminfo              4   0 /var/run/utmp
#676    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
#676    dbus-daemon        20   0 /usr/share/dbus-1/system-services
#676    dbus-daemon        -1   2 /lib/dbus-1/system-services
#676    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/


<!-- 6.Какой системный вызов использует uname -a? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в /proc, где можно узнать версию ядра и релиз ОС. -->
#uname()
#Part of the utsname information is also accessible  via  /proc/sys/kernel/{ostype, hostname, 
#osrelease, version, domainname}.

<!-- 7.Чем отличается последовательность команд через ; и через && в bash? Например:
root@netology1:~# test -d /tmp/some_dir; echo Hi
Hi
root@netology1:~# test -d /tmp/some_dir && echo Hi
root@netology1:~#
Есть ли смысл использовать в bash &&, если применить set -e? -->
#&& -  условный оператор "и" - echo Hi выполнит если test -d /tmp/some_dir успешно
#; 	- разделитель - echo Hi - выполнится после test -d /tmp/some_dir
#set -e - Exit immediately if a command exits with a non-zero status. (прерывает при ненулевом статусе)
#если будет ошибка то смысла в set -e не будет

<!-- 8.Из каких опций состоит режим bash set -euxo pipefail и почему его хорошо было бы использовать в сценариях? -->
#-e прерывает выполнение исполнения при ошибке любой команды кроме последней в последовательности 
#-x вывод трейса простых команд 
#-u неустановленные/не заданные параметры и переменные считаются как ошибки, с выводом в stderr текста 
#ошибки и выполнит завершение неинтерактивного вызова
#-o pipefail возвращает код возврата набора/последовательности команд, ненулевой при последней команды 
#или 0 для успешного выполнения команд.
? - повышает детализацию логов и прервется при обнаружении ошибки.

<!-- 9.Используя -o stat для ps, определите, какой наиболее часто встречающийся статус у процессов в системе. В man ps ознакомьтесь (/PROCESS STATE CODES) что значат дополнительные к основной заглавной буквы статуса процессов. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными). -->
#Процессы ожидания S* и фоновые процессы I*