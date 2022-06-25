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
  Swap usage:   0%                 IPv4 address for eth1:   192.168.1.67

```
**Получили начальную страницу Nginx по умолчанию** http://192.168.1.67

+ Шаг 5 — Настройка блоков сервера
```
sudo mkdir -p /var/www/devops/html
sudo chown -R $USER:$USER /var/www/devops/html
sudo chmod -R 755 /var/www/devops
nano /var/www/devops/html/index.htm
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps</title>
</head>
<body>
        DevOps - ИБ
</body>
</html>
```

```
sudo nano /etc/nginx/sites-available/devops
server {
        listen 80;
        listen [::]:80;
        listen 192.168.1.67;


        root /var/www/devops/html;
        index index.html index.htm index.nginx-debian.html;


        server_name devops www.devops;


        location / {
                try_files $uri $uri/ =404;
        }
}
```
```
sudo ln -s /etc/nginx/sites-available/devops /etc/nginx/sites-enabled/
sudo nano /etc/nginx/nginx.conf
server_names_hash_bucket_size 64;// удалал #
vagrant@vagrant:/etc/nginx/sites-enabled$ sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
sudo systemctl restart nginx
```
#### Скриншот:
____
![3](https://github.com/surgeon09/VagrantConfigs/blob/master/Screenshots/3.png?raw=true)



***Создание самоподписного SSL сертификата***
https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1
```
vagrant@vagrant:/var/www$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt

Generating a RSA private key
.......................................+++++
................................................................+++++
writing new private key to '/etc/ssl/private/nginx-selfsigned.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:RU
State or Province Name (full name) [Some-State]:Moscow
Locality Name (eg, city) []:Moscow
Organization Name (eg, company) [Internet Widgits Pty Ltd]:NoName
Organizational Unit Name (eg, section) []:NoName
Common Name (e.g. server FQDN or YOUR name) []:192.168.1.67
Email Address []:admin@devops.local

vagrant@vagrant:/var/www$ sudo openssl dhparam -out /etc/nginx/dhparam.pem 4096

```

```
Generating DH parameters, 4096 bit long safe prime, generator 2
This is going to take a long time
....................................................................................................................................................................................................................................................................................................+.......................................................................................................................................+..........+................................................................................................................................................................................................................................................................+....................................................................................................................................................................................+......................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................+.................................................................................................................................................................................................................................................................................................................................+....................................................................................................................................................................................................................................................................................................+.............................................................................................................................................................................................................................................+.......................................................+.........................................................................................................................................................................................................................................................................................+...............................................................................................................

```

```
vagrant@vagrant:/var/www$ cd /etc/ssl
vagrant@vagrant:/etc/ssl$ ls
certs  openssl.cnf  private
```
***vagrant@vagrant:/etc/ssl$ sudo nano /etc/nginx/snippets/self-signed.conf***
```
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
```
***vagrant@vagrant:/etc/ssl$ sudo nano /etc/nginx/snippets/ssl-params.conf***
```
ssl_protocols TLSv1.3;
ssl_prefer_server_ciphers on;
ssl_dhparam /etc/nginx/dhparam.pem; 
ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
ssl_ecdh_curve secp384r1;
ssl_session_timeout  10m;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
# Disable strict transport security for now. You can uncomment the following
# line if you understand the implications.
#add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
add_header X-XSS-Protection "1; mode=block";
```
***vagrant@vagrant:/etc/ssl$ sudo cp /etc/nginx/sites-available/devops.local /etc/nginx/sites-available/devops.local.bak***

```
vagrant@vagrant:/etc/ssl$ sudo nano /etc/nginx/sites-available/devops.local

server {
        listen 443 ssl;
        listen [::]:443 ssl;
        listen 192.168.1.67 ssl;
        include snippets/self-signed.conf;
        include snippets/ssl-params.conf;


        root /var/www/devops.local/html;
        index index.html index.htm index.nginx-debian.html;


        server_name devops.local www.devops.local;


        location / {
                try_files $uri $uri/ =404;
        }
}


server {
    listen 80;
    listen [::]:80;


    server_name devops.local www.devops.local;


    return 301 https://$server_name$request_uri;
}

```
***vagrant@vagrant:/etc/ssl$ sudo ufw status***
```
Status: active


To                         Action      From
--                         ------      ----
Nginx HTTPS                ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
Nginx Full                 ALLOW       Anywhere
Nginx HTTPS (v6)           ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
Nginx Full (v6)            ALLOW       Anywhere (v6)
vagrant@vagrant:/etc/ssl$ sudo nginx -t
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found for certificate "/etc/ssl/certs/nginx-selfsigned.crt"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successfu
sudo systemctl restart nginx
```
#### Скриншот:
____
![4](https://github.com/surgeon09/VagrantConfigs/blob/master/Screenshots/4.png?raw=true)


























