package com.barh;

import java.util.HashSet;

public class ArrayQuestions {
    private final static int ASCII_SIZE = 128;
    public static void main(String[] args) {
        String arg = args[0];
        Boolean b = CheckRepeating(arg);
        String ans = b ? "" : " not";
        System.out.printf("There are%s repeating characters in \"%s\".\n", ans, arg);
    }

    private static Boolean CheckRepeating(String arg) {
        HashSet<Character> hashSet = new HashSet<>();
        if (arg.length() > ASCII_SIZE) return true;
        for(Character ch: arg.toCharArray()) {
            if (hashSet.contains(ch)) {
                return true;
            }
            hashSet.add(ch);
        }
        return false;
    }
}
