
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

```
vagrant@server1:~$ mkdir -p 05-virt-03-docker/src/build/ansible
vagrant@server1:~/05-virt-03-docker/src/build/ansible$ vim Dockerfile

FROM alpine:3.14

RUN CARGO_NET_GIT_FETCH_WITH_CLI=1 && \
    apk --no-cache add \
        sudo \
        python3\
        py3-pip \
        openssl \
        ca-certificates \
        sshpass \
        openssh-client \
        rsync \
        git && \
    apk --no-cache add --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        musl-dev \
        gcc \
        cargo \
        openssl-dev \
        libressl-dev \
        build-base && \
    pip install --upgrade pip wheel && \
    pip install --upgrade cryptography cffi && \
    pip install ansible==2.9.24 && \
    pip install mitogen ansible-lint jmespath && \
    pip install --upgrade pywinrm && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache/pip && \
    rm -rf /root/.cargo

RUN mkdir /ansible && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible

CMD [ "ansible-playbook", "--version"



vagrant@server1:~/05-virt-03-docker/src/build/ansible$ ls -la
total 12
drwxrwxr-x 2 vagrant vagrant 4096 Aug 18 18:29 .
drwxrwxr-x 3 vagrant vagrant 4096 Aug 18 18:28 ..
-rw-rw-r-- 1 vagrant vagrant  968 Aug 18 18:29 Dockerfile




vagrant@server1:~/05-virt-03-docker/src/build/ansible$ docker build -t aabogov/ansible:2.10.0 .
Sending build context to Docker daemon   2.56kB
Step 1/5 : FROM alpine:3.14
3.14: Pulling from library/alpine
c7ed990a2339: Pull complete
Digest: sha256:1ab24b3b99320975cca71716a7475a65d263d0b6b604d9d14ce08f7a3f67595c
Status: Downloaded newer image for alpine:3.14
 ---> dd53f409bf0b
Step 2/5 : RUN CARGO_NET_GIT_FETCH_WITH_CLI=1 &&     apk --no-cache add         sudo         python3        py3-pip         openssl         ca-certificates         sshpass         openssh-client         rsync         git &&     apk --no-cache add --virtual build-dependencies         python3-dev         libffi-dev         musl-dev         gcc         cargo         openssl-dev         libressl-dev         build-base &&     pip install --upgrade pip wheel &&     pip install --upgrade cryptography cffi &&     pip install ansible==2.9.24 &&     pip install mitogen ansible-lint jmespath &&     pip install --upgrade pywinrm &&     apk del build-dependencies &&     rm -rf /var/cache/apk/* &&     rm -rf /root/.cache/pip &&     rm -rf /root/.cargo
 ---> Running in cb21b22de08c
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz
(1/55) Installing ca-certificates (20220614-r0)
(2/55) Installing brotli-libs (1.0.9-r5)
(3/55) Installing nghttp2-libs (1.43.0-r0)
(4/55) Installing libcurl (7.79.1-r2)
(5/55) Installing expat (2.4.7-r0)
(6/55) Installing pcre2 (10.36-r1)
(7/55) Installing git (2.32.3-r0)
(8/55) Installing openssh-keygen (8.6_p1-r3)
(9/55) Installing ncurses-terminfo-base (6.2_p20210612-r1)
(10/55) Installing ncurses-libs (6.2_p20210612-r1)
(11/55) Installing libedit (20210216.3.1-r0)
(12/55) Installing openssh-client-common (8.6_p1-r3)
(13/55) Installing openssh-client-default (8.6_p1-r3)
(14/55) Installing openssl (1.1.1q-r0)
(15/55) Installing libbz2 (1.0.8-r1)
(16/55) Installing libffi (3.3-r2)
(17/55) Installing gdbm (1.19-r0)
(18/55) Installing xz-libs (5.2.5-r1)
(19/55) Installing libgcc (10.3.1_git20210424-r2)
(20/55) Installing libstdc++ (10.3.1_git20210424-r2)
(21/55) Installing mpdecimal (2.5.1-r1)
(22/55) Installing readline (8.1.0-r0)
(23/55) Installing sqlite-libs (3.35.5-r0)
(24/55) Installing python3 (3.9.5-r2)
(25/55) Installing py3-appdirs (1.4.4-r2)
(26/55) Installing py3-chardet (4.0.0-r2)
(27/55) Installing py3-idna (3.2-r0)
(28/55) Installing py3-urllib3 (1.26.5-r0)
(29/55) Installing py3-certifi (2020.12.5-r1)
(30/55) Installing py3-requests (2.25.1-r4)
(31/55) Installing py3-msgpack (1.0.2-r1)
(32/55) Installing py3-lockfile (0.12.2-r4)
(33/55) Installing py3-cachecontrol (0.12.6-r1)
(34/55) Installing py3-colorama (0.4.4-r1)
(35/55) Installing py3-contextlib2 (0.6.0-r1)
(36/55) Installing py3-distlib (0.3.1-r3)
(37/55) Installing py3-distro (1.5.0-r3)
(38/55) Installing py3-six (1.15.0-r1)
(39/55) Installing py3-webencodings (0.5.1-r4)
(40/55) Installing py3-html5lib (1.1-r1)
(41/55) Installing py3-parsing (2.4.7-r2)
(42/55) Installing py3-packaging (20.9-r1)
(43/55) Installing py3-toml (0.10.2-r2)
(44/55) Installing py3-pep517 (0.10.0-r2)
(45/55) Installing py3-progress (1.5-r2)
(46/55) Installing py3-retrying (1.3.3-r1)
(47/55) Installing py3-ordered-set (4.0.2-r1)
(48/55) Installing py3-setuptools (52.0.0-r3)
(49/55) Installing py3-pip (20.3.4-r1)
(50/55) Installing libacl (2.2.53-r0)
(51/55) Installing popt (1.18-r0)
(52/55) Installing zstd-libs (1.4.9-r1)
(53/55) Installing rsync (3.2.4-r0)
(54/55) Installing sshpass (1.09-r0)
(55/55) Installing sudo (1.9.7_p1-r1)
Executing busybox-1.33.1-r8.trigger
Executing ca-certificates-20220614-r0.trigger
OK: 98 MiB in 69 packages
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz
(1/37) Installing pkgconf (1.7.4-r0)
(2/37) Installing python3-dev (3.9.5-r2)
(3/37) Installing linux-headers (5.10.41-r0)
(4/37) Installing libffi-dev (3.3-r2)
(5/37) Installing musl-dev (1.2.2-r3)
(6/37) Installing binutils (2.35.2-r2)
(7/37) Installing libgomp (10.3.1_git20210424-r2)
(8/37) Installing libatomic (10.3.1_git20210424-r2)
(9/37) Installing libgphobos (10.3.1_git20210424-r2)
(10/37) Installing gmp (6.2.1-r1)
(11/37) Installing isl22 (0.22-r0)
(12/37) Installing mpfr4 (4.1.0-r0)
(13/37) Installing mpc1 (1.2.1-r0)
(14/37) Installing gcc (10.3.1_git20210424-r2)
(15/37) Installing rust-stdlib (1.52.1-r1)
(16/37) Installing libxml2 (2.9.14-r1)
(17/37) Installing llvm11-libs (11.1.0-r2)
(18/37) Installing http-parser (2.9.4-r0)
(19/37) Installing pcre (8.44-r0)
(20/37) Installing libssh2 (1.9.0-r1)
(21/37) Installing libgit2 (1.1.0-r2)
(22/37) Installing rust (1.52.1-r1)
(23/37) Installing cargo (1.52.1-r1)
(24/37) Installing openssl-dev (1.1.1q-r0)
(25/37) Installing libressl3.3-libcrypto (3.3.6-r0)
(26/37) Installing libressl3.3-libssl (3.3.6-r0)
(27/37) Installing libressl3.3-libtls (3.3.6-r0)
(28/37) Installing libressl-dev (3.3.6-r0)
(29/37) Installing libmagic (5.40-r1)
(30/37) Installing file (5.40-r1)
(31/37) Installing libc-dev (0.7.2-r3)
(32/37) Installing g++ (10.3.1_git20210424-r2)
(33/37) Installing make (4.3-r0)
(34/37) Installing fortify-headers (1.1-r1)
(35/37) Installing patch (2.7.6-r7)
(36/37) Installing build-base (0.5-r3)
(37/37) Installing build-dependencies (20220818.183237)
Executing busybox-1.33.1-r8.trigger
OK: 1110 MiB in 106 packages
Requirement already satisfied: pip in /usr/lib/python3.9/site-packages (20.3.4)
Collecting pip
  Downloading pip-22.2.2-py3-none-any.whl (2.0 MB)
Collecting wheel
  Downloading wheel-0.37.1-py2.py3-none-any.whl (35 kB)
Installing collected packages: wheel, pip
  Attempting uninstall: pip
    Found existing installation: pip 20.3.4
    Uninstalling pip-20.3.4:
      Successfully uninstalled pip-20.3.4
Successfully installed pip-22.2.2 wheel-0.37.1
Collecting cryptography
  Downloading cryptography-37.0.4-cp36-abi3-musllinux_1_1_x86_64.whl (4.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 9.5 MB/s eta 0:00:00
Collecting cffi
  Downloading cffi-1.15.1-cp39-cp39-musllinux_1_1_x86_64.whl (463 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 463.1/463.1 kB 10.5 MB/s eta 0:00:00
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 10.5 MB/s eta 0:00:00
Installing collected packages: pycparser, cffi, cryptography
Successfully installed cffi-1.15.1 cryptography-37.0.4 pycparser-2.21
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
Collecting ansible==2.9.24
  Downloading ansible-2.9.24.tar.gz (14.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.3/14.3 MB 4.1 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting jinja2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 4.7 MB/s eta 0:00:00
Collecting PyYAML
  Downloading PyYAML-6.0.tar.gz (124 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.0/125.0 kB 8.1 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Requirement already satisfied: cryptography in /usr/lib/python3.9/site-packages (from ansible==2.9.24) (37.0.4)
Requirement already satisfied: cffi>=1.12 in /usr/lib/python3.9/site-packages (from cryptography->ansible==2.9.24) (1.15.1)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp39-cp39-musllinux_1_1_x86_64.whl (29 kB)
Requirement already satisfied: pycparser in /usr/lib/python3.9/site-packages (from cffi>=1.12->cryptography->ansible==2.9.24) (2.21)
Building wheels for collected packages: ansible, PyYAML
  Building wheel for ansible (setup.py): started
  Building wheel for ansible (setup.py): finished with status 'done'
  Created wheel for ansible: filename=ansible-2.9.24-py3-none-any.whl size=16205052 sha256=caefabb26dd88aa17ed6c811c7844a9eb0e209fe14653610ccfa38da3e5f1a77
  Stored in directory: /root/.cache/pip/wheels/ba/89/f3/df35238037ec8303702ddd8569ce11a807935f96ecb3ff6d52
  Building wheel for PyYAML (pyproject.toml): started
  Building wheel for PyYAML (pyproject.toml): finished with status 'done'
  Created wheel for PyYAML: filename=PyYAML-6.0-cp39-cp39-linux_x86_64.whl size=45331 sha256=1e357565ef1fee668b2268334bb0b9aaf49808e20ac7d9be4396607b6c67a3f8
  Stored in directory: /root/.cache/pip/wheels/b4/0f/9a/d6af48581dda678920fccfb734f5d9f827c6ed5b4074c7eda8
Successfully built ansible PyYAML
Installing collected packages: PyYAML, MarkupSafe, jinja2, ansible
Successfully installed MarkupSafe-2.1.1 PyYAML-6.0 ansible-2.9.24 jinja2-3.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
Collecting mitogen
  Downloading mitogen-0.3.3-py2.py3-none-any.whl (292 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 292.2/292.2 kB 956.7 kB/s eta 0:00:00
Collecting ansible-lint
  Downloading ansible_lint-6.4.0-py3-none-any.whl (181 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 181.2/181.2 kB 950.5 kB/s eta 0:00:00
Collecting jmespath
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting wcmatch>=7.0
  Downloading wcmatch-8.4-py3-none-any.whl (40 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.0/40.0 kB 1.3 MB/s eta 0:00:00
Collecting jsonschema>=4.8.0
  Downloading jsonschema-4.12.1-py3-none-any.whl (81 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 81.2/81.2 kB 1.3 MB/s eta 0:00:00
Collecting yamllint>=1.25.0
  Downloading yamllint-1.27.1.tar.gz (129 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 129.1/129.1 kB 2.4 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting ansible-core>=2.12.0
  Downloading ansible_core-2.13.3-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 2.8 MB/s eta 0:00:00
Collecting ruamel.yaml<0.18,>=0.15.34
  Downloading ruamel.yaml-0.17.21-py3-none-any.whl (109 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.5/109.5 kB 3.3 MB/s eta 0:00:00
Collecting pytest
  Downloading pytest-7.1.2-py3-none-any.whl (297 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 297.0/297.0 kB 3.5 MB/s eta 0:00:00
Collecting ansible-compat>=2.2.0
  Downloading ansible_compat-2.2.0-py3-none-any.whl (18 kB)
Collecting rich>=9.5.1
  Downloading rich-12.5.1-py3-none-any.whl (235 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 235.6/235.6 kB 3.2 MB/s eta 0:00:00
Requirement already satisfied: packaging in /usr/lib/python3.9/site-packages (from ansible-lint) (20.9)
Collecting enrich>=1.2.6
  Downloading enrich-1.2.7-py3-none-any.whl (8.7 kB)
Requirement already satisfied: pyyaml in /usr/lib/python3.9/site-packages (from ansible-lint) (6.0)
Collecting subprocess-tee>=0.3.5
  Downloading subprocess_tee-0.3.5-py3-none-any.whl (8.0 kB)
Requirement already satisfied: cryptography in /usr/lib/python3.9/site-packages (from ansible-core>=2.12.0->ansible-lint) (37.0.4)
Collecting resolvelib<0.9.0,>=0.5.3
  Downloading resolvelib-0.8.1-py2.py3-none-any.whl (16 kB)
Requirement already satisfied: jinja2>=3.0.0 in /usr/lib/python3.9/site-packages (from ansible-core>=2.12.0->ansible-lint) (3.1.2)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Downloading pyrsistent-0.18.1.tar.gz (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.5/100.5 kB 4.0 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting attrs>=17.4.0
  Downloading attrs-22.1.0-py2.py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.8/58.8 kB 1.0 MB/s eta 0:00:00
Collecting pygments<3.0.0,>=2.6.0
  Downloading Pygments-2.13.0-py3-none-any.whl (1.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 1.1 MB/s eta 0:00:00
Collecting commonmark<0.10.0,>=0.9.0
  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.1/51.1 kB 1.3 MB/s eta 0:00:00
Collecting ruamel.yaml.clib>=0.2.6
  Downloading ruamel.yaml.clib-0.2.6.tar.gz (180 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 180.7/180.7 kB 2.4 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting bracex>=2.1.1
  Downloading bracex-2.3.post1-py3-none-any.whl (12 kB)
Collecting pathspec>=0.5.3
  Downloading pathspec-0.9.0-py2.py3-none-any.whl (31 kB)
Requirement already satisfied: setuptools in /usr/lib/python3.9/site-packages (from yamllint>=1.25.0->ansible-lint) (52.0.0)
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
Collecting py>=1.8.2
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.7/98.7 kB 4.4 MB/s eta 0:00:00
Collecting tomli>=1.0.0
  Downloading tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting iniconfig
  Downloading iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/lib/python3.9/site-packages (from jinja2>=3.0.0->ansible-core>=2.12.0->ansible-lint) (2.1.1)
Requirement already satisfied: cffi>=1.12 in /usr/lib/python3.9/site-packages (from cryptography->ansible-core>=2.12.0->ansible-lint) (1.15.1)
Requirement already satisfied: pycparser in /usr/lib/python3.9/site-packages (from cffi>=1.12->cryptography->ansible-core>=2.12.0->ansible-lint) (2.21)
Building wheels for collected packages: yamllint, pyrsistent, ruamel.yaml.clib
  Building wheel for yamllint (setup.py): started
  Building wheel for yamllint (setup.py): finished with status 'done'
  Created wheel for yamllint: filename=yamllint-1.27.1-py2.py3-none-any.whl size=62023 sha256=1c5ba2ac4fb9c0560b8383b653812b1860162f3251b9b55882c14dd16fd62bb1
  Stored in directory: /root/.cache/pip/wheels/96/6b/41/cdc6102faa47924bd11794a9b3d5e6d7107daf6548c46f79ee
  Building wheel for pyrsistent (pyproject.toml): started
  Building wheel for pyrsistent (pyproject.toml): finished with status 'done'
  Created wheel for pyrsistent: filename=pyrsistent-0.18.1-cp39-cp39-linux_x86_64.whl size=119789 sha256=c3facdc36a448c433f88606354a9875ae7e8210a787ad1552c46227a8cebd90d
  Stored in directory: /root/.cache/pip/wheels/87/fe/e6/fc8deeb581a41e462eafaf19fee96f51cdc8391e0be1c8088a
  Building wheel for ruamel.yaml.clib (setup.py): started
  Building wheel for ruamel.yaml.clib (setup.py): finished with status 'done'
  Created wheel for ruamel.yaml.clib: filename=ruamel.yaml.clib-0.2.6-cp39-cp39-linux_x86_64.whl size=746355 sha256=72f4973ce3d2600e41784adb9473f5ed0703ef4f58c61e79f2e92552b938004b
  Stored in directory: /root/.cache/pip/wheels/b1/c4/5d/d96e5c09189f4d6d2a9ffb0d7af04ee06d11a20f613f5f3496
Successfully built yamllint pyrsistent ruamel.yaml.clib
Installing collected packages: resolvelib, iniconfig, commonmark, tomli, subprocess-tee, ruamel.yaml.clib, pyrsistent, pygments, py, pluggy, pathspec, mitogen, jmespath, bracex, attrs, yamllint, wcmatch, ruamel.yaml, rich, pytest, jsonschema, enrich, ansible-core, ansible-compat, ansible-lint
Successfully installed ansible-compat-2.2.0 ansible-core-2.13.3 ansible-lint-6.4.0 attrs-22.1.0 bracex-2.3.post1 commonmark-0.9.1 enrich-1.2.7 iniconfig-1.1.1 jmespath-1.0.1 jsonschema-4.12.1 mitogen-0.3.3 pathspec-0.9.0 pluggy-1.0.0 py-1.11.0 pygments-2.13.0 pyrsistent-0.18.1 pytest-7.1.2 resolvelib-0.8.1 rich-12.5.1 ruamel.yaml-0.17.21 ruamel.yaml.clib-0.2.6 subprocess-tee-0.3.5 tomli-2.0.1 wcmatch-8.4 yamllint-1.27.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
Collecting pywinrm
  Downloading pywinrm-0.4.3-py2.py3-none-any.whl (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.1/44.1 kB 1.4 MB/s eta 0:00:00
Collecting requests-ntlm>=1.1.0
  Downloading requests_ntlm-1.1.0-py2.py3-none-any.whl (5.7 kB)
Collecting xmltodict
  Downloading xmltodict-0.13.0-py2.py3-none-any.whl (10.0 kB)
Requirement already satisfied: requests>=2.9.1 in /usr/lib/python3.9/site-packages (from pywinrm) (2.25.1)
Requirement already satisfied: six in /usr/lib/python3.9/site-packages (from pywinrm) (1.15.0)
Requirement already satisfied: chardet<5,>=3.0.2 in /usr/lib/python3.9/site-packages (from requests>=2.9.1->pywinrm) (4.0.0)
Requirement already satisfied: idna<3.3,>=2.5 in /usr/lib/python3.9/site-packages (from requests>=2.9.1->pywinrm) (3.2)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3.9/site-packages (from requests>=2.9.1->pywinrm) (1.26.5)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3.9/site-packages (from requests>=2.9.1->pywinrm) (2020.12.5)
Requirement already satisfied: cryptography>=1.3 in /usr/lib/python3.9/site-packages (from requests-ntlm>=1.1.0->pywinrm) (37.0.4)
Collecting ntlm-auth>=1.0.2
  Downloading ntlm_auth-1.5.0-py2.py3-none-any.whl (29 kB)
Requirement already satisfied: cffi>=1.12 in /usr/lib/python3.9/site-packages (from cryptography>=1.3->requests-ntlm>=1.1.0->pywinrm) (1.15.1)
Requirement already satisfied: pycparser in /usr/lib/python3.9/site-packages (from cffi>=1.12->cryptography>=1.3->requests-ntlm>=1.1.0->pywinrm) (2.21)
Installing collected packages: xmltodict, ntlm-auth, requests-ntlm, pywinrm
Successfully installed ntlm-auth-1.5.0 pywinrm-0.4.3 requests-ntlm-1.1.0 xmltodict-0.13.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: Ignoring https://dl-cdn.alpinelinux.org/alpine/v3.14/main: No such file or directory
WARNING: Ignoring https://dl-cdn.alpinelinux.org/alpine/v3.14/community: No such file or directory
(1/37) Purging build-dependencies (20220818.183237)
(2/37) Purging python3-dev (3.9.5-r2)
(3/37) Purging libffi-dev (3.3-r2)
(4/37) Purging linux-headers (5.10.41-r0)
(5/37) Purging cargo (1.52.1-r1)
(6/37) Purging rust (1.52.1-r1)
(7/37) Purging rust-stdlib (1.52.1-r1)
(8/37) Purging openssl-dev (1.1.1q-r0)
(9/37) Purging libressl-dev (3.3.6-r0)
(10/37) Purging libressl3.3-libssl (3.3.6-r0)
(11/37) Purging libressl3.3-libtls (3.3.6-r0)
(12/37) Purging build-base (0.5-r3)
FROM alpine:3.14

RUN CARGO_NET_GIT_FETCH_WITH_CLI=1 && \
    apk --no-cache add \
        sudo \
        python3\
        py3-pip \
        openssl \
        ca-certificates \
        sshpass \
        openssh-client \
        rsync \
        git && \
    apk --no-cache add --virtual build-dependencies \
        python3-dev \
        libffi-dev \
        musl-dev \
        gcc \
        cargo \
        openssl-dev \
        libressl-dev \
        build-base && \
    pip install --upgrade pip wheel && \
    pip install --upgrade cryptography cffi && \
    pip install ansible==2.9.24 && \
    pip install mitogen ansible-lint jmespath && \
    pip install --upgrade pywinrm && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.cache/pip && \
    rm -rf /root/.cargo

RUN mkdir /ansible && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible

CMD [ "ansible-playbook", "--version" ]
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"Dockerfile" 39L, 968C                                                                                     39,39         All
(13/37) Purging file (5.40-r1)
(14/37) Purging g++ (10.3.1_git20210424-r2)
(15/37) Purging gcc (10.3.1_git20210424-r2)
(16/37) Purging binutils (2.35.2-r2)
(17/37) Purging libatomic (10.3.1_git20210424-r2)
(18/37) Purging libgomp (10.3.1_git20210424-r2)
(19/37) Purging libgphobos (10.3.1_git20210424-r2)
(20/37) Purging make (4.3-r0)
(21/37) Purging libc-dev (0.7.2-r3)
(22/37) Purging musl-dev (1.2.2-r3)
(23/37) Purging fortify-headers (1.1-r1)
(24/37) Purging patch (2.7.6-r7)
(25/37) Purging pkgconf (1.7.4-r0)
(26/37) Purging mpc1 (1.2.1-r0)
(27/37) Purging mpfr4 (4.1.0-r0)
(28/37) Purging isl22 (0.22-r0)
(29/37) Purging gmp (6.2.1-r1)
(30/37) Purging llvm11-libs (11.1.0-r2)
(31/37) Purging libxml2 (2.9.14-r1)
(32/37) Purging libgit2 (1.1.0-r2)
(33/37) Purging http-parser (2.9.4-r0)
(34/37) Purging pcre (8.44-r0)
(35/37) Purging libssh2 (1.9.0-r1)
(36/37) Purging libressl3.3-libcrypto (3.3.6-r0)
(37/37) Purging libmagic (5.40-r1)
Executing busybox-1.33.1-r8.trigger
OK: 98 MiB in 69 packages
Removing intermediate container cb21b22de08c
 ---> ec5646ea8779
Step 3/5 : RUN mkdir /ansible &&     mkdir -p /etc/ansible &&     echo 'localhost' > /etc/ansible/hosts
 ---> Running in 80d0736504e6
Removing intermediate container 80d0736504e6
 ---> 0a7142deaae7
Step 4/5 : WORKDIR /ansible
 ---> Running in 71f45deb65f9
Removing intermediate container 71f45deb65f9
 ---> 6e8cc4c4865a
Step 5/5 : CMD [ "ansible-playbook", "--version" ]
 ---> Running in 722958aadcc7
Removing intermediate container 722958aadcc7
 ---> c64d02ecd044
Successfully built c64d02ecd044
Successfully tagged aabogov/ansible:2.10.0







vagrant@server1:~/05-virt-03-docker/src/build/ansible$ docker login -u aabogov
Password:
WARNING! Your password will be stored unencrypted in /home/vagrant/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded








vagrant@server1:~/05-virt-03-docker/src/build/ansible$ docker push aabogov/ansible:2.10.0
The push refers to repository [docker.io/aabogov/ansible]
cc37b466431d: Pushed
1713957929f4: Pushed
63493a9ab2d4: Mounted from library/alpine
2.10.0: digest: sha256:0ac7d04c1d0a56add8ac4ba13c211b4073f2536897e4475a9b29185780ed081c size: 947





vagrant@server1:~/05-virt-03-docker/src/build/ansible$ docker images
REPOSITORY        TAG             IMAGE ID       CREATED         SIZE
aabogov/ansible   2.10.0          c64d02ecd044   7 minutes ago   242MB
aabogov/nginx     1808            075b447b534f   8 days ago      23.5MB
nginx             stable-alpine   075b447b534f   8 days ago      23.5MB
alpine            3.14            dd53f409bf0b   9 days ago      5.61MB
nginx             latest          b692a91e4e15   2 weeks ago     142MB
debian            latest          07d9246c53a6   2 weeks ago     124MB
centos            latest          5d0da3dc9764   11 months ago   231MB

```

#### https://hub.docker.com/repository/docker/aabogov/ansible

---

### Как cдавать задание

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---