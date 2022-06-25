### Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

---



## 1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.

#### Скриншот:
____
![1](https://github.com/surgeon09/VagrantConfigs/blob/master/Screenshots/1.png?raw=true)


## 2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

#### Скриншот:
____
![2](https://github.com/surgeon09/VagrantConfigs/blob/master/Screenshots/2.png?raw=true)

## 3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS (использовал Nginx)

**Установка Nginx в Ubuntu 20.04**
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04-ru

+ Шаг 1 — Установка Nginx
```
sudo apt update
sudo apt install nginx

```

+ Шаг 2 — Настройка брандмауэра
```
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
```

+ Шаг 3 — Проверка веб-сервера
```
systemctl status nginx
vagrant@vagrant:/etc/nginx/sites-enabled$ systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-06-12 10:18:38 UTC; 46min ago
       Docs: man:nginx(8)
    Process: 39496 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 39500 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 39517 ExecReload=/usr/sbin/nginx -g daemon on; master_process on; -s reload (code=exited, status=0/SUCCESS)
   Main PID: 39507 (nginx)
      Tasks: 5 (limit: 2278)
     Memory: 5.7M
     CGroup: /system.slice/nginx.service
             ├─39507 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             ├─39518 nginx: worker process
             ├─39519 nginx: worker process
             ├─39520 nginx: worker process
             └─39521 nginx: worker process

```

+ Шаг 4 - Смотрим IP
```
bogov@MacBook-Pro-Arkadij-Bogov VagrantConfigs % vagrant ssh
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)


 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


  System information as of Sun 12 Jun 2022 09:14:44 AM UTC


  System load:  0.0                Users logged in:         0
  Usage of /:   13.0% of 30.88GB   IPv4 address for dummy0: 10.2.2.2
  Memory usage: 15%                IPv4 address for eth0:   10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1:   ***192.168.1.67***

```
    + http://192.168.1.67
    + Получил начальную страницу Nginx по умолчанию

























