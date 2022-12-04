## PHP

Install Php, Apache2 Webserver, MySQL.
```bash
apt install apache2 php php-apache mariadb phpmyadmin
```

## Apache Web Server

server serves `index.html` on `localhost:8080`

To start Web server
```bash
apachectl start
```

To stop
```
apachectl stop
```

Change index.html file
```bash
cd $PREFIX/share/apache2/default-site/htdocs
```
Remove or edit using text editor
```bash
rm index.html

nano index.php
```

Make changes to `httpd.conf` at `/etc/apache2`

1. Add 
```
LoadModule php_module libexec/apache2/libphp.so
```
Before `LoadModule mpm_prefork_module libexec/apache2/mod_mpm_prefork.so`

2. Uncomment `LoadModule mpm_prefork_module libexec/apache2/mod_mpm_prefork.so`
On line 66.

3. Comment `LoadModule mpm_worker_module libexec/apache2/mod_mpm_worker.so`

4. Add Line 553 before SSL ...

```
<FilesMatch \.php$>
         SetHandler application/x-httpd-php
 </FilesMatch>
```

5. Add Line at last
```
Include etc/apache2/extra/php_module.conf
```

6. Create file php_module.conf
```
touch etc/apache2/extra/php_module.conf
```

No need to add something in conf

Add text to `$PREFIX/share/apache2/default-site/htdocs/index.php`
```php
<?php
 echo "Hello, php"; 
?>
```
