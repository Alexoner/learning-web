package com.howtodoinjava.ibatis.demo.dto;

public class UserTEO {
    private Integer id;
    private String name;
    private String email;
    private String password;
    private int status;

    public String getEmail(){
        return email;
    }

    public void setEmail(String email) {
        this.email=email;
    }

    public void setId(Integer id) {
        this.id=id;
    }

    public String getName() {
        return name;
    }

    public void setName() {
        this.name=name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password){
        this.password=password;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus() {
        this.status = status;
    }
}
