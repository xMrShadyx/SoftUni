package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E06StrongNumber {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();

        int sum = 0;
        for (int i = 0; i < input.length(); i++) {
            int digit = input.charAt(i) - 48;

            int fact = 1;
            for (int j = 1; j <= digit; j++) {
                fact *= j;
            }
            sum += fact;
        }
        int inputNum = Integer.parseInt(input);
        if (sum == inputNum) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}
