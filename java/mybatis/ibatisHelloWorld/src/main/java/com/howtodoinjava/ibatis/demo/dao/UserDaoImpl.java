package com.howtodoinjava.ibatis.demo.dao;

import com.howtodoinjava.ibatis.demo.dto.UserTEO;
import com.ibatis.sqlmap.client.SqlMapClient;

public class UserDaoImpl implements UserDAO {

    // @Override
    public UserTEO addUser(UserTEO user, SqlMapClient sqlmapClient) {
        try {
            Integer id = (Integer) sqlmapClient.queryForObject("user.getMaxId");
            id = id == null ? (Integer) 1 : (Integer) id + (Integer) 1;
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

    public UserTEO deleteUserByid(Integer id, SqlMapClient sqlmapClient) {
        // TODO Auto-generated method stub
        try {
            sqlmapClient.delete("user.deleteUserById", id);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
