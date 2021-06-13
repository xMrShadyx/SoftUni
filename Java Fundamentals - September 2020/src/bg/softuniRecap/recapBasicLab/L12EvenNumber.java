package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L12EvenNumber {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = Math.abs(scan.nextInt());

        boolean positive = true;

        while (positive) {
            if (num % 2 != 0) {
                System.out.println("Please write an even number.");
                num = Math.abs(scan.nextInt());
            } else {
                System.out.printf("The number is: %d", num);
                positive = false;
            }
        }
    }
}
