package com.howtodoinjava.ibatis.demo.dao;

import com.howtodoinjava.ibatis.demo.dto.UserTEO;
import com.ibatis.sqlmap.client.SqlMapClient;

/*
 * Data Access Object Interface
 */
public interface UserDao {

    public UserTEO addUser(UserTEO user, SqlMapClient sqlmapClient);

    public Integer getUserMaxId(SqlMapClient sqlmapClient);

    public UserTEO getUserById(Integer id, SqlMapClient sqlmapClient);

    public UserTEO deleteUserById(Integer id, SqlMapClient sqlmapClient);

    public UserTEO getAUser(SqlMapClient sqlmapClient);
}
