package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L02Passed {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double grade = Double.parseDouble(scan.nextLine());

        if (grade >= 3) {
            System.out.println("Passed!");
        }
    }
}
