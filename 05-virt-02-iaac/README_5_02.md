# Домашнее задание к занятию "5.2. Применение принципов IaaC в работе с виртуальными машинами"


## Задача 1
+ Опишите своими словами основные преимущества применения на практике IaaC паттернов.
```
Один раз созданный велосипед не придется каждый раз изобретать, а с помощью данного подхода создавать гомогенные среды без риска дрейфа конфигураций быстро и с помощью нескольких команд в терминале.
```
+ Какой из принципов IaaC является основополагающим?
```
Идемпоте́нтность (лат. idem — тот же самый + potens — способный) — это свойство объекта или операции, при повторном выполнении которой мы получаем результат идентичный предыдущему и всем последующим выполнениям.
```

## Задача 2
+ Чем Ansible выгодно отличается от других систем управление конфигурациями?
```
Главное его отличие от других подобных систем в том, что Ansible использует существующую SSH инфраструктуру, в то время как другие (Saltstack, Chef, Puppet, и пр.) требуют установки специального PKI-окружения (Private Key Infrastructure). Также немаловажны простота – декларативный метод описания конфигураций и расширяемость — лёгкое подключение кастомных ролей и модулей.
```

+ Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?
```
Все зависит от кол-ва необходимых хостов, если предполагается более 100 хостов то предпочтительнее использовать pull метод т.к. "ни одна отдельно стоящая железка не выдержит тысячи запросов" и не выдержит нагрузку это характерно для push метода при котором из источника конфигураций выталкивается на целевые хосты.
При pull методе неоходима установка дополнительных агентов, которые будут мониторить изменения и забирать неоходимые конфигурации, дополнительные службы накладывают дополнительные источники возможных проблем. Вообщем если в кратце как я это понял, то надежнее и проще push на примере Ansible, но если необходим массштаб то это конечно pull с установкой агентов и использование более быстрого языка нежели Python, являющимся не самым быстрым интерпретируемым языком.
```

## Задача 3
Установить на личный компьютер:

+ VirtualBox
```
bogov@MacBook-Pro-Arkadij-Bogov VagrantConfigs % vboxmanage --version
6.1.32r149290
```
+ Vagrant
```
bogov@MacBook-Pro-Arkadij-Bogov VagrantConfigs % vagrant -v
Vagrant 2.2.19
```
+ Ansible
```
bogov@MacBook-Pro-Arkadij-Bogov VagrantConfigs % ansible --version
ansible [core 2.13.2]
  config file = None
  configured module search path = ['/Users/bogov/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.9/site-packages/ansible
  ansible collection location = /Users/bogov/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.9.10 (main, Jan 15 2022, 11:48:00) [Clang 13.0.0 (clang-1300.0.29.3)]
  jinja version = 3.1.2
  libyaml = True
```
Приложить вывод команд установленных версий каждой из программ, оформленный в markdown.

## Задача 4 (*)

Воспроизвести практическую часть лекции самостоятельно.

+ Создать виртуальную машину.
```
bogov@MacBook-Pro-Arkadij-Bogov vagrant % vagrant up
Bringing machine 'server1.netology' up with 'virtualbox' provider...
==> server1.netology: Checking if box 'bento/ubuntu-20.04' version '202112.19.0' is up to date...
==> server1.netology: Clearing any previously set network interfaces...
==> server1.netology: Preparing network interfaces based on configuration...
    server1.netology: Adapter 1: nat
    server1.netology: Adapter 2: hostonly
==> server1.netology: Forwarding ports...
    server1.netology: 22 (guest) => 20011 (host) (adapter 1)
    server1.netology: 22 (guest) => 2222 (host) (adapter 1)
==> server1.netology: Running 'pre-boot' VM customizations...
==> server1.netology: Booting VM...
==> server1.netology: Waiting for machine to boot. This may take a few minutes...
    server1.netology: SSH address: 127.0.0.1:2222
    server1.netology: SSH username: vagrant
    server1.netology: SSH auth method: private key
    server1.netology: 
    server1.netology: Vagrant insecure key detected. Vagrant will automatically replace
    server1.netology: this with a newly generated keypair for better security.
    server1.netology: 
    server1.netology: Inserting generated public key within guest...
    server1.netology: Removing insecure key from the guest if it's present...
    server1.netology: Key inserted! Disconnecting and reconnecting using new SSH key...
==> server1.netology: Machine booted and ready!
==> server1.netology: Checking for guest additions in VM...
==> server1.netology: Setting hostname...
==> server1.netology: Configuring and enabling network interfaces...
==> server1.netology: Mounting shared folders...
    server1.netology: /vagrant => /Users/bogov/Documents/DevOps/VagrantConfigs/05-virt-02-iaac/src/vagrant
==> server1.netology: Running provisioner: ansible...
    server1.netology: Running ansible-playbook...

PLAY [nodes] *******************************************************************

TASK [Gathering Facts] *********************************************************
ok: [server1.netology]

TASK [Create directory for ssh-keys] *******************************************
ok: [server1.netology]

TASK [Adding rsa-key in /root/.ssh/authorized_keys] ****************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: If you are using a module and expect the file to exist on the remote, see the remote_src option
fatal: [server1.netology]: FAILED! => {"changed": false, "msg": "Could not find or access '~/.ssh/id_rsa.pub' on the Ansible Controller.\nIf you are using a module and expect the file to exist on the remote, see the remote_src option"}
...ignoring

TASK [Checking DNS] ************************************************************
changed: [server1.netology]

TASK [Installing tools] ********************************************************
ok: [server1.netology] => (item=git)
ok: [server1.netology] => (item=curl)

TASK [Installing docker] *******************************************************
changed: [server1.netology]

TASK [Add the current user to docker group] ************************************
changed: [server1.netology]

PLAY RECAP *********************************************************************
server1.netology           : ok=7    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=1 
```
+ Зайти внутрь ВМ, убедиться, что Docker установлен с помощью команды
```
docker ps
```

```
bogov@MacBook-Pro-Arkadij-Bogov vagrant % vagrant ssh
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon 18 Jul 2022 04:57:36 PM UTC

  System load:  0.0                Users logged in:          0
  Usage of /:   13.6% of 30.88GB   IPv4 address for docker0: 172.17.0.1
  Memory usage: 24%                IPv4 address for eth0:    10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1:    192.168.192.11
  Processes:    109


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
Last login: Mon Jul 18 16:50:05 2022 from 10.0.2.2

vagrant@server1:~$ uptime
 16:58:31 up 10 min,  1 user,  load average: 0.00, 0.14, 0.16
```

```
vagrant@server1:~$ service docker status
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-07-18 16:49:56 UTC; 9min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 21002 (dockerd)
      Tasks: 7
     Memory: 40.0M
     CGroup: /system.slice/docker.service
             └─21002 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.705987040Z" level=warning msg="Your kernel does not support CPU realtime scheduler"
Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.706093849Z" level=warning msg="Your kernel does not support cgroup blkio weight"
Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.706195947Z" level=warning msg="Your kernel does not support cgroup blkio weight_device"
Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.706456677Z" level=info msg="Loading containers: start."
Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.860352493Z" level=info msg="Default bridge (docker0) is assigned with an IP address 172.17.0.0/16. Daemon>
Jul 18 16:49:55 server1 dockerd[21002]: time="2022-07-18T16:49:55.948673801Z" level=info msg="Loading containers: done."
Jul 18 16:49:56 server1 dockerd[21002]: time="2022-07-18T16:49:56.020593295Z" level=info msg="Docker daemon" commit=a89b842 graphdriver(s)=overlay2 version=20.10.17
Jul 18 16:49:56 server1 dockerd[21002]: time="2022-07-18T16:49:56.021131873Z" level=info msg="Daemon has completed initialization"
Jul 18 16:49:56 server1 systemd[1]: Started Docker Application Container Engine.
Jul 18 16:49:56 server1 dockerd[21002]: time="2022-07-18T16:49:56.070597529Z" level=info msg="API listen on /run/docker.sock"
lines 1-21/21 (END)
```

```
vagrant@server1:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```