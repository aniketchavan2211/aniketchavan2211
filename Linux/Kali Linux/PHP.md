## PHP8

### First Update and Upgrade System.

```bash
sudo apt update -y && sudo apt full-upgrade -y
```

### Install PHP Package from repo

```bash
sudo apt -y install wget php php-cgi php-mysqli php-pear php-mbstring libapache2-mod-php php-common php-phpseclib php-mysql
```

Check PHP version by:

```bash
php --version
```

### Install Mariadb (Database Server)

 1. Update and Upgrade
 
 ```bash
 sudo apt update -y && sudo apt upgrade -y 
 ```

 2. Install Mariadb package from repo

 ```bash
 sudo apt install mariadb-server
 # if not working then
 # apt search mariadb
 # it will list all package with name mariadb
 ```

 3. starting database server (Mariadb)

 Starting MariaDB Database Server using:

 ```bash
 sudo service start mariadb
 ```

 For Permanently changes

 ```bash
 # this will automatically start when ever system reboot.
 sudo systemctl enable --now mariadb
 ```

 4. create a user and database for first time

 ```bash
 sudo mysql_secure_installation
 
 # Answers the below questions
 ```

 then login with shell

 ```bash
 mysql -u root -p
 # accessing mysql shell loging as root user with password prompt
 ```

 execute Query.

 ```mysql
 ? 
 # for help with mysql commands
 ```

### Installation of PHPMyAdmin


Installing using `phpmyadmin` package from repo:
```bash
sudo apt install phpmyadmin -y
```

give nessessary permissions:

```
sudo chown -R www-data:www-data /var/lib/phpmyadmin
```

copy config template:

```bash
sudo cp /usr/share/phpmyadmin/config.sample.inc.php  /usr/share/phpmyadmin/config.inc.php
```

edit `/usr/share/phpmyadmin/config.inc.php` this file:

```bash
sudo nano /usr/share/phpmyadmin/config.inc.php
```

Change this token:

```bash
$cfg['blowfish_secret'] = 'H2TxcGXxflSd8JwrXVlh6KW4s2rER63i';
```

Check your token:

```bash
sudo cat /var/lib/phpmyadmin/blowfish_secret.inc.php
```

Add this line to config:

```bash
$cfg['TempDir'] = '/var/lib/phpmyadmin/tmp';
```

### Configure Apache2 Web Server

Quickstart

```
sudo apt update -y && sudo apt upgrade -y
sudo apt install apache2
```

Configure

```bash
sudo nano /etc/apache2/conf-enabled/phpmyadmin.conf
```

```conf
# phpMyAdmin default Apache configuration

Alias /phpmyadmin /usr/share/phpmyadmin

<Directory /usr/share/phpmyadmin>
    Options SymLinksIfOwnerMatch
    DirectoryIndex index.php

    # limit libapache2-mod-php to files and directories necessary by >
    <IfModule mod_php7.c>
        php_admin_value upload_tmp_dir /var/lib/phpmyadmin/tmp
        php_admin_value open_basedir /usr/share/phpmyadmin/:/usr/shar>
    </IfModule>

    # PHP 8+
    <IfModule mod_php.c>
        php_admin_value upload_tmp_dir /var/lib/phpmyadmin/tmp
        php_admin_value open_basedir /usr/share/phpmyadmin/:/usr/shar>
    </IfModule>

</Directory>

# Disallow web access to directories that don't need it
<Directory /usr/share/phpmyadmin/templates>
    Require all denied
</Directory>
<Directory /usr/share/phpmyadmin/libraries>
    Require all denied
</Directory>

```

then restart the apache2 web server:

```bash
sudo service apache2 restart
```

Check PHPMyAdminpage
go to `localhost:80/phpmyadmin` page or `127.0.0.1:80/phpmyadmin`
both are same.
`[IP:PORT/HOSTNAME/phpmyadmin]
