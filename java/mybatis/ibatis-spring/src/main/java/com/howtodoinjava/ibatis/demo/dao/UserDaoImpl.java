package com.howtodoinjava.ibatis.demo.dao;

import com.howtodoinjava.ibatis.demo.dto.UserTEO;
import com.ibatis.sqlmap.client.SqlMapClient;

/*
 * Data Access Object implementation
 */
public class UserDaoImpl implements UserDao {

    // @Override
    public UserTEO addUser(UserTEO user, SqlMapClient sqlmapClient) {
        try {
            /*
             * sqlmap-config.xml:<sqlMap namespace="user">
             */
            Integer id = (Integer) sqlmapClient.queryForObject("user.getMaxId");
            // Integer id = (Integer)getSqlMapClientTemplate().queryForObject("user.getMaxId");
            id = id == null ? Integer.valueOf(1) : Integer.valueOf(id.intValue() + 1);
            user.setId(id);
            user.setStatus(1);
            sqlmapClient.insert("user.addUser", user);
            user = getUserById(id, sqlmapClient);

            return user;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public UserTEO getUserById(Integer id, SqlMapClient sqlmapClient) {
        // TODO Auto-generated method stub
        try {
            UserTEO user = (UserTEO) sqlmapClient.queryForObject("user.getUserById", id);
            return user;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public UserTEO deleteUserById(Integer id, SqlMapClient sqlmapClient) {
        // TODO Auto-generated method stub
        try {
            sqlmapClient.delete("user.deleteUserById", id);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
