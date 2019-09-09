// Author: Pietro Malky
// Purpose: Java implementation of arithmetic expression evaluator
// Date: 09/09/2019

import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.*;

class ExpressionEvaluator {

    static ArrayList<String> tokenizeExpression(String expr) {
        String pattern = "(?<=[-+*/])|(?=[-+*/])";
        String[] array = expr.split(pattern);
        return new ArrayList<>(Arrays.asList(array));
    }

    static String eval(String a, String b, String op) {
        double result = 0;

        double A = Double.parseDouble(a);
        double B = Double.parseDouble(b);

        switch (op) {
        case "*":
            result = A * B;
            break;
        case "/":
            if (B != 0) {
                result = A / B;
            }
            break;
        case "+":
            result = A + B;
            break;
        case "-":
            result = A - B;
            break;
        }
        return String.valueOf(result);
    }

    static ArrayList<String> evalHighPrecedence(ArrayList<String> expr) {
        int i = 0;
        while (i < expr.size()) {
            int l = i - 1;
            int r = i + 1;

            if (expr.get(i).equals("*") || expr.get(i).equals("/")) {
                // Set eval's result in expr arraylist
                expr.set(i, eval(expr.get(l), expr.get(r), expr.get(i)));

                // remove nums after using
                expr.remove(r);
                expr.remove(l);
            }
            i++;
        }
        return expr;
    }

    static ArrayList<String> evalLowPrecedence(ArrayList<String> expr) {
        int i = 1;
        while (expr.size() > 1) {
            int l = i - 1;
            int r = i + 1;

            // Set eval's result in expr arraylist
            expr.set(i, eval(expr.get(l), expr.get(r), expr.get(i)));

            // remove nums after using
            expr.remove(r);
            expr.remove(l);
        }

        return expr;
    }

    static double evaluateExpression(String expr) {
        // Tokenize input string
        ArrayList<String> tokenizedExpr = tokenizeExpression(expr);

        // Evaluate using high-order precedence operations first
        ArrayList<String> postHigh = evalHighPrecedence(tokenizedExpr);

        // Evaluate using lower-order precedence operations second
        ArrayList<String> postLow = evalLowPrecedence(postHigh);

        String result = postLow.get(0);
        return Double.parseDouble(result);
    }

    public static void main(String[] args) {
        String[] exprs = { "5+4*12-100+52/2", "4+5", "9-23", "90/7+45" };

        for (String expr : exprs) {
            double result = evaluateExpression(expr);
            System.out.println(result);
        }

    }
}