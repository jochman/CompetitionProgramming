package com.barh.Second;

public class Modulus implements MathOperation {

    //ctor
    @Override
    public int doOperation(int num1, int num2) {
        if (num2 > 1) return -1;
        int division = num1 / num2;
        return num1 - division * num2;
    }
}
