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


## 4. Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное)
***vagrant@vagrant:/etc/ssl/testssl.sh$ ./testssl.sh -U --sneaky https://192.168.1.67***

```
###########################################################
    testssl.sh       3.1dev from https://testssl.sh/dev/
    (13298ff 2022-06-01 09:47:12)


      This program is free software. Distribution and
             modification under GPLv2 permitted.
      USAGE w/o ANY WARRANTY. USE IT AT YOUR OWN RISK!


       Please file bugs @ https://testssl.sh/bugs/


###########################################################


 Using "OpenSSL 1.0.2-chacha (1.0.2k-dev)" [~183 ciphers]
 on vagrant:./bin/openssl.Linux.x86_64
 (built: "Jan 18 17:12:17 2019", platform: "linux-x86_64")




 Start 2022-06-13 04:49:23        -->> 192.168.1.67:443 (192.168.1.67) <<--


 rDNS (192.168.1.67):    devops.local. www.devops.local.
 192.168.1.67:443 appears to support TLS 1.3 ONLY. You better use --openssl=<path_to_openssl_supporting_TLS_1.3>
 Type "yes" to proceed and accept all scan problems --> yes
 Service detected:       HTTP




 Testing vulnerabilities


 Heartbleed (CVE-2014-0160)                not vulnerable (OK), no heartbeat extension
 CCS (CVE-2014-0224)                       not vulnerable (OK)
 Ticketbleed (CVE-2016-9244), experiment.  not vulnerable (OK), no session ticket extension
 ROBOT                                     Server does not support any cipher suites that use RSA key transport
 Secure Renegotiation (RFC 5746)           not vulnerable (OK)
 Secure Client-Initiated Renegotiation     not vulnerable (OK)
 CRIME, TLS (CVE-2012-4929)                not vulnerable (OK)
 BREACH (CVE-2013-3587)                    First request failed (HTTP header request stalled and was terminated) POODLE, SSL (CVE-2014-3566)               not vulnerable (OK), no SSLv3 support
 TLS_FALLBACK_SCSV (RFC 7507)              No fallback possible (OK), no protocol below TLS 1.2 offered
 SWEET32 (CVE-2016-2183, CVE-2016-6329)    not vulnerable (OK)
 FREAK (CVE-2015-0204)                     not vulnerable (OK)
 DROWN (CVE-2016-0800, CVE-2016-0703)      not vulnerable on this host and port (OK)
                                           no RSA certificate, thus certificate can't be used with SSLv2 elsewhere
 LOGJAM (CVE-2015-4000), experimental      not vulnerable (OK): no DH EXPORT ciphers, no DH key detected with <= TLS 1.2
 BEAST (CVE-2011-3389)                     not vulnerable (OK), no SSL3 or TLS1
 LUCKY13 (CVE-2013-0169), experimental     not vulnerable (OK)
 Winshock (CVE-2014-6321), experimental    not vulnerable (OK)
 RC4 (CVE-2013-2566, CVE-2015-2808)        not vulnerable (OK)




 Done 2022-06-13 04:49:44 [  23s] -->> 192.168.1.67:443 (192.168.1.67) <<--

```























