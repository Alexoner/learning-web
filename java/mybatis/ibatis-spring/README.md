Objective
=========
Integrate ibatis into Spring framework

Keys to implementation
======================
1. Configure **dependency injection** for **JavaBeans** in Spring configuration
**Ibatis client bean**
**Data Access Object bean**

2. Initialize Bean in spring way
Dao dao = applicationContext.getBean(“beanId”)

3. Play with the bean

Ibatis Usage
============
1. Write JavaBean for Data object

2. Write Data Access Object interface and implementation

3. Map SQL

4. Configure Ibatis JDBC

5. Use the DAO to manipulate database
