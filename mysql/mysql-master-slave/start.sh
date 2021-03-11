#!/usr/bin/env bash
#设置主从使用脚本

Repl_passwd="aA123$%^"
M_USER_PASSWD="bGludXIK"
S_USER_PASSWD="eW91bmcK"

add_user_sql="grant replication slave, replication client on *.* to 'repl'@'%' identified by  '$Repl_passwd';"
File=`echo "SHOW MASTER STATUS" | MYSQL_PWD=$M_USER_PASSWD  mysql -uroot -h mysql-master -N|awk '{print $1}'`
Position=`echo "SHOW MASTER STATUS" | MYSQL_PWD=$M_USER_PASSWD  mysql -uroot -h mysql-master -N|awk '{print $2}'`
slave_sql="change master to master_host='mysql-master',master_user='repl',master_password='$Repl_passwd',master_port=3306,master_log_file='$File',master_log_pos=$Position,master_connect_retry=30;"


master_sql(){
  echo "$add_user_sql"
  echo "$add_user_sql" | MYSQL_PWD=$M_USER_PASSWD  mysql -uroot -h mysql-master -N
  sleep 6
}

slave_sql(){
  echo "$slave_sql "
  echo "$slave_sql" | MYSQL_PWD=$S_USER_PASSWD  mysql -uroot -h mysql-slave -N
  sleep 6
  echo "start slave;" | MYSQL_PWD=$S_USER_PASSWD  mysql -uroot -h mysql-slave -N
  echo "show slave status \G;" | MYSQL_PWD=$S_USER_PASSWD  mysql -uroot -h mysql-slave -N

}

#echo "$add_user_sql"
master_sql
slave_sql
