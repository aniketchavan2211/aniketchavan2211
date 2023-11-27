## PostgreSQL Database

1. To `Start` Database Server:

Please check superuser permission is need or not, If needed then use `sudo` and if not then skip it.

You need to start the server first, by

using `systemctl`

```
sudo systemctl start postgresql 
```

or 


```bash
sudo service postgresql start
```

2. To check state of Database Server:

```bash
sudo systemclt status postgresql
```


```bash
sudo service posgresql status
```


3. Create `USER`:

```bash
# login using root user / superuser
sudo -i -u postgres
```

```bash
# access postgresql prompt
psql
```

```bash
# change username
CREATE DATABASE username;

# here we created kali as user name
CREATE DATABASE kali;
# quit
\q 
```

4. Query


```bash
# login kali as user in database
psql -d kali

# Enter Query then
# username=> query
kali=> SELECT * FROM Table;
```

5. To `STOP` Database Server:


```bash
sudo systemctl stop postgresql
```

or 

```bash
sudo service postgresql stop
```
