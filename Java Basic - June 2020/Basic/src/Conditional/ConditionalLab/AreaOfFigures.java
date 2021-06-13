package Conditional.ConditionalLab;

import java.util.Scanner;

public class AreaOfFigures {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String type = scan.nextLine();

        double result = 0.0;

        if (type.equals("square")) {
            double num = Double.parseDouble(scan.nextLine());
            result = num * num;
        } else if (type.equals("rectangle")) {
            double num1 = Double.parseDouble(scan.nextLine());
            double num2 = Double.parseDouble(scan.nextLine());
            result = num1 * num2;
        } else if (type.equals("circle")) {
            double num = Double.parseDouble(scan.nextLine());
            result = num * num * Math.PI;
        } else if (type.equals("triangle")) {
            double num1 = Double.parseDouble(scan.nextLine());
            double num2 = Double.parseDouble(scan.nextLine());
            result = (num1 * num2) / 2;
        }
        System.out.printf("%.3f", result);
    }
}
