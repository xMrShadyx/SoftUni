package Conditional.ConditionalLab;

import java.util.Scanner;

public class EvenOrOdd {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int number = Integer.parseInt(scan.nextLine());
        String result = "";

        if (number % 2 == 0) {
            result = "even";
        } else {
            result = "odd";
        }

        System.out.println(result);
    }
}

