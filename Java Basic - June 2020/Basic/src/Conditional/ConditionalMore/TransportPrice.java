package Conditional.ConditionalMore;

import java.util.Scanner;

public class TransportPrice {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int Kms = Integer.parseInt(scan.nextLine());
        String Cycle = scan.nextLine();

        double result = 0.0;

        if (Kms < 20) {
            if (Cycle.equals("day")) {
                result = (0.79 * Kms) + 0.70;
            } else if (Cycle.equals("night")) {
                result = (0.90 * Kms) + 0.70;
            }
        } else if (Kms < 100) {
            result = 0.09 * Kms;
        } else {
            result = 0.06 * Kms;
        }

        System.out.printf("%.2f", result);
    }
}
