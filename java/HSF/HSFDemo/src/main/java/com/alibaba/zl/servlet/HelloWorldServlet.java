package com.alibaba.zl.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.support.WebApplicationContextUtils;

import com.alibaba.zl.service.HelloWorldService;

public class HelloWorldServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        WebApplicationContext context = WebApplicationContextUtils.getWebApplicationContext(getServletContext());
        HelloWorldService helloWorldService = (HelloWorldService) context.getBean("HelloWorldConsumer");
        PrintWriter out = resp.getWriter();
        out.println(helloWorldService.sayHello("zhanlan"));
        return;
    }
}
