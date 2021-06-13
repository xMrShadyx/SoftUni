package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E01Ages {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int age = scan.nextInt();
        String result = "";
        if (age >= 0 && age <= 2) {
            result = "baby";
        } else if (age <= 13) {
            result = "child";
        } else if (age <= 19) {
            result = "teenager";
        } else if (age <= 65) {
            result = "adult";
        } else {
            result = "elder";
        }

        System.out.println(result);
    }
}
