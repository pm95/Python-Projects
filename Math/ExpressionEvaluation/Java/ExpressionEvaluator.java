// Author: Pietro Malky
// Purpose: Java implementation of arithmetic expression evaluator
// Date: 09/09/2019

import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.*;

class ExpressionEvaluator {

    static ArrayList<String> fixNegativeVals(ArrayList<String> expr) {
        for (int i = 0; i < expr.size(); i++) {
            if (expr.get(i).equals("-")) {
                if (i == 0 || expr.get(i - 1).matches("[*|/|+|-| ]")) {
                    double temp = -1 * Double.parseDouble(expr.get(i + 1));
                    expr.set(i + 1, String.valueOf(temp));
                    expr.remove(i);
                }
            }
        }

        return expr;
    }

    static ArrayList<String> tokenizeExpression(String expr) {
        String pattern = "(?<=[-+*/])|(?=[-+*/])";
        String[] array = expr.split(pattern);
        ArrayList<String> result = new ArrayList<>(Arrays.asList(array));

        // Fix formatting where negative values were completely tokenized
        result = fixNegativeVals(result);

        // Remove any whitespace generated by tokenization steps
        result.remove(" ");

        return result;
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
        String[] exprs = { "5+4*12-100+52/2", "5 + 2", "6 - 3", "4 * 8", "15 / 3", "19 - 27.2", "55555*99999",
                "1/10000000", "56 + 34+14+5.5", "17.23-6.46/3.23", "-1.5 + 6" };

        // for (String expr : exprs) {
        // System.out.println(evaluateExpression(expr));
        // }

        System.out.println(evaluateExpression("-4.02+-8 * 32-67/-2"));

    }
}