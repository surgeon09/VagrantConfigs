
# Домашнее задание к занятию "5.3. Введение. Экосистема. Архитектура. Жизненный цикл Docker контейнера"

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Любые вопросы по решению задач задавайте в чате учебной группы.

---


## Важно!

Перед отправкой работы на проверку удаляйте неиспользуемые ресурсы.
Это важно для того, чтоб предупредить неконтролируемый расход средств, полученных в результате использования промокода.

Подробные рекомендации [здесь](https://github.com/netology-code/virt-homeworks/blob/virt-11/r/README.md)

---

## Задача 1

Сценарий выполения задачи:

- создайте свой репозиторий на https://hub.docker.com;
- выберете любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность:
запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```
Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

#### https://hub.docker.com/repository/docker/aabogov/nginx

#### Смотрим IP VM
```
bogov@MacBook-Pro-Arkadij-Bogov vagrant % vagrant ssh
==> vagrant: A new version of Vagrant is available: 2.3.0 (installed version: 2.2.19)!
==> vagrant: To upgrade visit: https://www.vagrantup.com/downloads.html

Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 18 Aug 2022 11:00:34 AM UTC

  System load:  0.0                Users logged in:          0
  Usage of /:   14.9% of 30.88GB   IPv4 address for docker0: 172.17.0.1
  Memory usage: 25%                IPv4 address for eth0:    10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1:    **192.168.192.11**
  Processes:    115


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
Last login: Wed Aug 17 18:32:37 2022 from 10.0.2.2
```
#### 192.168.192.11 

### Создание кастомного index.html
```
vagrant@server1:~$ mkdir custom-index
vagrant@server1:~$ vim custom-index/index.html
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```

### Доступные образы nginx
```
vagrant@server1:~$ docker images
REPOSITORY   TAG             IMAGE ID       CREATED       SIZE
nginx        stable-alpine   075b447b534f   8 days ago    23.5MB
nginx        latest          b692a91e4e15   2 weeks ago   142MB
```

### Запуск контейнера на основе тега stable-alpine и использование кастомного index.html
```
docker run --name nginx_home -P -d -v ~/custom-index/:/usr/share/nginx/html nginx:stable-alpine
0a8f3d2b81753ec74ac7609147570f0449f6f2bca1c9c5388e6e64bcb029bedd
vagrant@server1:~/custom-index$ docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                                     NAMES
0a8f3d2b8175   nginx:stable-alpine   "/docker-entrypoint.…"   12 seconds ago   Up 11 seconds   0.0.0.0:49156->80/tcp, :::49156->80/tcp   nginx_home
```

#### Скриншот:
____
![1](https://github.com/surgeon09/VagrantConfigs/blob/master/Screenshots/05-03-01.png?raw=true)

## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
"Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- Высоконагруженное монолитное java веб-приложение;
- Nodejs веб-приложение;
- Мобильное приложение c версиями для Android и iOS;
- Шина данных на базе Apache Kafka;
- Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
- Мониторинг-стек на базе Prometheus и Grafana;
- MongoDB, как основное хранилище данных для java-приложения;
- Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

#### - Высоконагруженное монолитное java веб-приложение:
```
Не подходит.
Т.к. архитектура предполагается монолитной, т.е. один сервер, поэтому  дополнительная прослойка в виде docker-контейнера только дополняет рисков в отказе, в данном случае предпочтительнее stand alone подход когда все раскатывается на физическом сервере или как вариант паравиртуализация при котором Гипервизор модифицирует ядро гостевой ВМ для разделения доступа к аппаратным средствам физического сервера.
```

#### - Nodejs веб-приложение:
```
Подходит. 
Node.js - по сути окружение для javascript для построения логики работы веб-приложения, является его частью, модулем, хорошо укладывается в микро сервисную архитектуру.
```

#### - Мобильное приложение c версиями для Android и iOS:
```
Зависит от способа разработки мобильного приложения, если применяется подход при котором используется эмуляция браузера для унифицированного отображения фронта приложения на обоих типах устройства, то в таком случае и фронт и бэк будут одинаковым при отображении что на Android что на IOS, т.е. то здесь подойдет подход с виртуальной машиной и iaac для быстрого развертывания и тестирования в виду быстро меняющихся версий android и ios.

Если предполагается разработка нативных мобильных приложений какждая из которых содержит в себе разный стек как для фронта так и для бэка, здесь может подойти подход с контейнеризацией при котором можно будет изолировать разные подходы в разработки в виде отдельных контейнеров.
```

#### - Шина данных на базе Apache Kafka:
```
Подходит.
Здесь точно подойдет контейнеризация т.к. необходимо достигнуть отказоустойчивового состояния за счет кластеризации, для удобного массштабирования воркеров для разребания большого кол-ва пакетов в очередях.
```

#### - Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana:
```
Подходит.
Для простоты управления и сборки контейнеров, необходимо собрать кластер, для гибкого и прозрачного управления, а также логировоания сервисов, можно подключить создать кластер логирования и нам не придется хранить логи nginx в контейнере на том же Docker-хосте -> мы можем по сети либо в json формате либо в каком-то другом удобном формате отправлять на сервер легирования.
```

#### - Мониторинг-стек на базе Prometheus и Grafana:
```
Подходит.
По аналогии с вышеперечисленным примером, также создание кластера с использованием подхода IaaC, для возможности гибкого программирования сред под динамично добавляющиеся потребности от бизнеса по метрикам и удобства анализа логов.
```

#### - MongoDB, как основное хранилище данных для java-приложения:
```
Т.к. MongoDB это NoSQl технология архитектуры баз данных, и с легкостью интегрируется под любую операционную систему, то дополнительную ВМ создавать не понадобится, и соответственно контейнеризация подходит для легкости и массштабирования отдельных приложений на сервере.
```


#### - Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry:
```
Не подходит.
Речь идет о 2-х отдельных серверах один для сборки другой для приватного Docker Registry, что может быть удобно при закрытых с точки зрения ИБ организациях, когда подрядчикам доступно только на push обновленных образов в Docker Registry, с последущим выкатыванием на прод полученных образов.
```

## Задача 3

- Запустите первый контейнер из образа ***centos*** c любым тэгом в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```;
- Добавьте еще один файл в папку ```/data``` на хостовой машине;
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера.

#### Контейнер из образа ***centos***
```
vagrant@server1:/$ docker run -t -d -v /data:/data centos
ac28bb7272d6649ced1462c067ddd942d20dd8f4736d03ae31c4913f68653614
```

#### Контейнер из образа ***debian***
```
vagrant@server1:/$ docker run -t -v /data:/data -d debian
5283420cc786e87cecc61eb8aa4359249411c23f67f7aca86d0b17941b794c45
```

#### Смотрим ID контейнеров чтобы провалиться
```
vagrant@server1:/$ docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS              PORTS     NAMES
5283420cc786   debian    "bash"        4 seconds ago        Up 3 seconds                  jolly_kapitsa
ac28bb7272d6   centos    "/bin/bash"   About a minute ago   Up About a minute             eloquent_ellis
```

#### Внутри контейнера с centos создаем фокусную папку и файл
```
vagrant@server1:/$ docker exec -it ac28bb7272d6 bash
[root@ac28bb7272d6 /]# ls -lah /
total 60K
drwxr-xr-x   1 root root 4.0K Aug 18 18:08 .
drwxr-xr-x   1 root root 4.0K Aug 18 18:08 ..
-rwxr-xr-x   1 root root    0 Aug 18 18:08 .dockerenv
lrwxrwxrwx   1 root root    7 Nov  3  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K Aug 18 17:53 data
drwxr-xr-x   5 root root  360 Aug 18 18:08 dev
drwxr-xr-x   1 root root 4.0K Aug 18 18:08 etc
drwxr-xr-x   2 root root 4.0K Nov  3  2020 home
lrwxrwxrwx   1 root root    7 Nov  3  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Nov  3  2020 lib64 -> usr/lib64
drwx------   2 root root 4.0K Sep 15  2021 lost+found
drwxr-xr-x   2 root root 4.0K Nov  3  2020 media
drwxr-xr-x   2 root root 4.0K Nov  3  2020 mnt
drwxr-xr-x   2 root root 4.0K Nov  3  2020 opt
dr-xr-xr-x 168 root root    0 Aug 18 18:08 proc
dr-xr-x---   2 root root 4.0K Sep 15  2021 root
drwxr-xr-x  11 root root 4.0K Sep 15  2021 run
lrwxrwxrwx   1 root root    8 Nov  3  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K Nov  3  2020 srv
dr-xr-xr-x  13 root root    0 Aug 18 18:08 sys
drwxrwxrwt   7 root root 4.0K Sep 15  2021 tmp
drwxr-xr-x  12 root root 4.0K Sep 15  2021 usr
drwxr-xr-x  20 root root 4.0K Sep 15  2021 var
[root@ac28bb7272d6 /]# echo '' > /data/centos-file-1
[root@ac28bb7272d6 /]# ls /data
centos-file-1
[root@ac28bb7272d6 /]# exit
exit
```

#### На хостовой машине создаем фокусную папку и файл
```
vagrant@server1:/$ sudo su
root@server1:/# echo '' > /data/host-file-2
root@server1:/# ls /data
centos-file-1  host-file-2
root@server1:/# exit
exit
```

#### Листинг файлов в директории из контейнера debian
```
vagrant@server1:/$ docker exec -it 5283420cc786 bash
root@5283420cc786:/# ls -lah /data
total 16K
drwxr-xr-x 2 root root 4.0K Aug 18 17:53 .
drwxr-xr-x 1 root root 4.0K Aug 18 18:10 ..
-rw-r--r-- 1 root root    1 Aug 18 18:11 centos-file-1
-rw-r--r-- 1 root root    1 Aug 18 18:12 host-file-2
root@5283420cc786:/# exit
exit
```

## Задача 4 (*)

Воспроизвести практическую часть лекции самостоятельно.

Соберите Docker образ с Ansible, загрузите на Docker Hub и пришлите ссылку вместе с остальными ответами к задачам.


---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---