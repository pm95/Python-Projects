// Author: Pietro Malky
// Purpose: Java implementation of arithmetic expression evaluator
// Date: 09/09/2019

import java.util.ArrayList;
import java.util.regex.*;

class EvaluateExpression {
    String expr = "";

    EvaluateExpression(String expression) {
        this.expr = expression;
    }

    void sayHello() {
        System.out.println(this.expr);
    }

}

class ExpressionEvaluator {

    public static void main(String[] args) {
        String expr = "5+4*12-100+52/2";
        String[] nums = expr.split("(?<=[-+*/])|(?=[-+*/])");
        for (String c : nums) {
            System.out.println(c);
        }
    }
}