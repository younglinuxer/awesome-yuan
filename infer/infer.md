### infer 
```
不同于sonar 的检查规则检查语法错误  infer可以检查代码运行中可能出现空指针的情况 及一些严重的问题

需使用高版本内核才能使用 
 
```

#### 对项目进行检查

```
使用 infer -- mvn 对java项目进行编译 编译完后则会对项目代码进行检查
infer -- mvn compile
```

![Image text](../src/img/infer-mvn01.png) 