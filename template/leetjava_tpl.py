#!/usr/bin/env python
#coding: utf-8

""" leetcode java模板

Author: hatloney(hatlonely@gmail.com)
Date: 2014-10-30
"""

import argparse

leetcode_java_tpl = """import java.lang.reflect.Method;

public class Test {{
    private static Method method_;
    private static Class class_;

    private static void test_cases() throws Throwable {{
        // test_case(new Object[]{{new int[]{{1, 2, 3, 4}}, 8}}, new int[]{{0, 0}});
        // TODO add your case here
    }};

    private static void test_case(Object[] args, Object ret) throws Throwable {{
        // int[] result = (int[]) method_.invoke(class_.newInstance(), args);
        // int[] expect = (int[]) ret;
        try {{
            // TODO add assertions
            // assert result[0] == expect[0];
            // assert result[1] == expect[1];
        }} catch (AssertionError e) {{
            System.out.println("test case failed: ");
            // TODO print error infomation
        }}
    }}

    @SuppressWarnings("unchecked")
    public static void test(Class c) throws Throwable {{
        class_ = c;
        // TODO set method_
        // method_ = c.getMethod("twoSum", new Class[]{{int[].class, int.class}});
        test_cases();
    }}

    public static void main(String[] args) throws Throwable {{
        if (args.length != 1) {{
            System.out.println("Usage: java -ea Test <package>");
            System.out.println("    eg: java -ea Test pj");
            System.out.println("    eg: java -ea Test hl");
            return;
        }}

        test(Class.forName(args[0] + ".Solution"));
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
