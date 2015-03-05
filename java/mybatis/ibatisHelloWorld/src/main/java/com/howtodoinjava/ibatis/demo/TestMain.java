package com.howtodoinjava.ibatis.demo;

import java.io.Reader;

import com.howtodoinjava.ibatis.demo.dao.UserDao;
import com.howtodoinjava.ibatis.demo.dao.UserDaoImpl;
import com.howtodoinjava.ibatis.demo.dto.UserTEO;
import com.ibatis.common.resources.Resources;
import com.ibatis.sqlmap.client.SqlMapClient;
import com.ibatis.sqlmap.client.SqlMapClientBuilder;

public class TestMain {

    public static void main(String[] args) throws Exception {
        // Initialize dao
        UserDao manager = new UserDaoImpl();

        // Create the SQLMapClient
        Reader reader = Resources.getResourceAsReader("sqlmap-config.xml");
        SqlMapClient sqlmapClient = SqlMapClientBuilder.buildSqlMapClient(reader);

        // Create a new user to persistence
        UserTEO user = new UserTEO();
        user.setId(Integer.valueOf(1));
        user.setName("Demo User");
        user.setPassword("password");
        user.setEmail("demo-user@howtodoinjava.com");
        user.setStatus(1);

        // Add the user
        manager.addUser(user, sqlmapClient);

        // Fetch the user detail
        UserTEO createdUser = manager.getUserById(Integer.valueOf(1), sqlmapClient);
        System.out.println(createdUser.getEmail());

        // Lets delete the user
        manager.deleteUserById(Integer.valueOf(1), sqlmapClient);

        // insert another
        user.setId(Integer.valueOf(1));
        user.setName("John");
        user.setPassword("passwd");
        user.setEmail("demo@howtodoinjava.com");
        user.setStatus(2);

        manager.addUser(user, sqlmapClient);
    }
}
