# GRE3000words
A web to memory English words for GRE test. 一个基于tornado开发的再要你命3000的网站。

1. To install python and modules: tornado and MySQLdb

2. To create your mysql account:
    mysql -uroot -p
    mysql>  insert into mysql.user(Host,User,Password) values("localhost","3000word",password(""));
    mysql> flush privileges;
    mysql> create database 3000word;
    mysql> GRANT ALL PRIVILEGES ON 3000word.* TO '3000word'@'localhost' IDENTIFIED BY '' WITH GRANT OPTION;
    mysql> flush privileges;
    mysql -u3000word 3000word <GRE3000words_create.sql

3. To reencode 3000.txt. PS: 3000.txt.old is saved as unicode text file on Windows OS.
    iconv -f UCS-2 -t utf8 3000.txt.old -o 3000.txt

4. To insert data into MySQL database:
    python toMySQL.py

5. To Run your Server:
    main python main.py --port=3380  >run.log 2>&1 & 
    
