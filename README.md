# GRE3000words
A web to memory English words for GRE test. 一个基于tornado开发的再要你命3000的网站。

![Alt text](demo.png)


* To install python and modules: tornado and MySQLdb

* To create your mysql account:
```shell
    mysql -uroot -p
```
```mysql
    mysql> insert into mysql.user(Host,User,Password) values("localhost","3000word",password(""));
    mysql> flush privileges;
    mysql> create database 3000word;
    mysql> GRANT ALL PRIVILEGES ON 3000word.* TO '3000word'@'localhost' IDENTIFIED BY '' WITH GRANT OPTION;
    mysql> flush privileges;
    mysql -u3000word 3000word <GRE3000words_create.sql
```
* To reencode 3000.txt. PS: 3000.txt.old is saved as unicode text file on Windows OS.
```shell    
    iconv -f UCS-2 -t utf8 3000.txt.old -o 3000.txt
```
* To insert data into MySQL database:
```python    
    python toMySQL.py
```
* To Run your Server:
```shell    
    python main.py --port=3380  >run.log 2>&1 & 
``` 
* To make it run at startup
```
    nohup python /home/conda/GRE3000words/main.py >/home/conda/GRE3000words/run.log 2>&1 &
    add the sentence above into /etc/rc.d/rc.local 
    confirm your permission and add execute privileges for /etc/rc.d/rc.local

```