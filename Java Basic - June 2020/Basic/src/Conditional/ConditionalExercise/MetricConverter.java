package Conditional.ConditionalExercise;

import java.util.Scanner;

public class MetricConverter {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double number = Double.parseDouble(scan.nextLine());
        String inp1 = scan.nextLine();
        String inp2 = scan.nextLine();


        if (inp1.equals("mm")) {
            number = number / 1000;
        } else if (inp1.equals("cm")) {
            number = number / 100;
        } else if (inp1.equals("m")) {
            number = number * 1;
        }


        if (inp2.equals("mm")) {
            number = number * 1000;
        } else if (inp2.equals("cm")) {
            number = number * 100;
        } else if (inp2.equals("m")) {
            number = number * 1;
        }

        System.out.printf("%.3f", number);
    }
}
