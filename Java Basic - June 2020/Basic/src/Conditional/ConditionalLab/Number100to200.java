package Conditional.ConditionalLab;

import java.util.Scanner;

public class Number100to200 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = Integer.parseInt(scan.nextLine());
        String result = "";

        if (num < 100) {
            result = "Less than 100";
        } else if (num <= 200) {
            result = "Between 100 and 200";
        } else {
            result = "Greater than 200";
        }

        System.out.println(result);
    }
}
