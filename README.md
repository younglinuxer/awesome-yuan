# awesome-yuan
```
运维常用软件合集 大部分使用docker-compose进行安装 包含一些对原有项目基础上的改动及使用说明

技术性不强 主要是方便使用 主要用于项目初期开发环境和测试环境使用 不建议生产使用  
```

#### 推荐项目

<table border="0">
    <tr>
        <td><a href="docs/setup/00-planning_and_overall_intro.md">开发环境安装(mysql,redis,禅道,gogs)</a></td>
        <td><a href="docs/setup/02-install_etcd.md">01-开箱即用的promethus监控系统</a></td>
        <td><a href="docs/setup/04-install_kube_master.md">02-数据库集群测试</a></td>
    </tr>
</table>

#### 日常使用类
~~- [jenkins](./jenkins/jenkins.md) jenkins安装及基础配置 Jenkins不建议docker安装~~
- [gogs](./gogs/gogs.md) 个人建议使用更轻量的gogs而不是使用gitlab
- [mindoc](./mindoc/mindoc.md) 小巧易用的文档库
- [sonar](./sonar/sonar.md) 代码质量检测工具
- [zentao](./zentao/zentao.md) 禅道 项目管理工具
- [svn](./svn/svn.md)
- [elk](./elk/elk.md)
#### 数据库
- [mysql](./mysql/mysql.md) 包含单机 一主一从
- [redis](./redis/redis.md) 包含单机 哨兵 及redis集群
- [mongo](./mongo/mongo.md) 包含单机 副本集 分片集群
- [psql](./psql/psql.md)
- [hive](./hive/hive.md)

#### 队列
- [rabbitmq](./rabbitmq/rabbitmq.md)
- [kafka](./kafka/kafka.md)
- [rocketmq](./rocketmq/rocketmq.md)

#### 存储类
- [minio](./minio/minio.md) 好用现代化对象存储
- [fastdfs](./fastdfs/fastdfs.md) 老牌存储 
##### 监控
- [zabbix](./zabbix/zabbix.md)
- [promethus](./promethus/promethus.md) 只需要修改下配置文件即可使用promethus监控系统
##### security安全审计类
- [juice-shop](./juice-shop/juice-shop.md) 很有意思的安全闯关游戏 玩它!
- [Nessus](./Nessus/Nessus.md)
##### 其他类
- [k8s集群](./juice-shop/juice-shop.md)
- [ocserv](./ocserv/ocserv.md)  ssl加密vpn
- [coredns](./coredns/coredns.md)  coredns+etcd存储的DNS服务器
- [jar-docker](./jar-docker/jar-docker.md)  jar包 DockerFile规范 



