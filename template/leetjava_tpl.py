#!/usr/bin/env python
#coding: utf-8

""" leetcode java模板

Author: hatloney(hatlonely@gmail.com)
Date: 2014-10-30
"""

import argparse

leetcode_java_tpl = """import java.lang.reflect.Method;

public class Test {{
    @SuppressWarnings("unchecked")
    static void test(Class c) throws AssertionError, Throwable {{
        Method method = c.getMethod("method", new Class[]{{}});
        assert method.invoke(c.newInstance(), {{}}).equals("result");
        // TODO add your assertion here
    }}

    public static void main(String[] args) {{
        if (args.length != 1) {{
            System.out.println("Usage: java -ea Test <package>");
            System.out.println("    eg: java -ea Test pj");
            System.out.println("    eg: java -ea Test hl");
            return;
        }}

        try {{
            Class solution = Class.forName(args[0] + ".HelloWorld");
            test(solution);
            System.out.println("test case success.");
        }} catch (AssertionError exception) {{
            System.out.println("test case failed.");
        }} catch (Throwable exception) {{
            System.out.println(args[0] + " not found");
        }}
    }}
}}
"""

default_arguments = {
}


__params = {}


command_example = """
command example:
    tplmake.py -t leetjava
"""


def parser():
    parser = argparse.ArgumentParser(usage=command_example)
    return parser


def params(options):
    global __params
    args = parser().parse_args(options)
    return __params


def tpls():
    return [leetcode_java_tpl]


def outs():
    return ['Test.java']
