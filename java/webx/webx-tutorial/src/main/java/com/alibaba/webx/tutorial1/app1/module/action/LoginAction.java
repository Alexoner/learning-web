package com.alibaba.webx.tutorial1.app1.module.action;

import com.alibaba.citrus.turbine.Navigator;
import com.alibaba.citrus.turbine.dataresolver.FormGroup;
import com.alibaba.webx.tutorial1.app1.Visitor;

public class LoginAction {

    /*
     * @FormGroup:annotation.Validate form and inject data from group
     * into visitor
     */
    public void doCheck(@FormGroup("login")Visitor visitor,Navigator nav) {
        String name = visitor.getName();
        String passwd = visitor.getPasswd();
        if("admin".equals(name)&&"admin".equals(passwd)) {
            nav.redirectTo("app1Link").withTarget("form/welcome").withParameter("name",name);
        }else {

        }
    }
}
