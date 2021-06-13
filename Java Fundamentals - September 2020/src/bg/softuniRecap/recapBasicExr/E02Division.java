package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E02Division {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();

        String result = "";
        if (num % 10 == 0) {
            result = "The number is divisible by 10";
        } else if (num % 7 == 0) {
            result = "The number is divisible by 7";
        } else if (num % 6 == 0) {
            result = "The number is divisible by 6";
        } else if (num % 3 == 0) {
            result = "The number is divisible by 3";
        } else if (num % 2 == 0) {
            result = "The number is divisible by 2";
        } else {
            result = "Not divisible";
        }

        System.out.println(result);
    }
}
