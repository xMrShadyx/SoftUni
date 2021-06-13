package Conditional.ConditionalExercise;

import java.util.Scanner;

public class BonusScore {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int number = Integer.parseInt(scan.nextLine());
        double bonusPoints = 0;

        if (number <= 100) {
            bonusPoints = 5;
        } else if (number > 1000) {
            bonusPoints = number * 0.10;
        } else {
            bonusPoints = number * 0.20;
        }

        if (number % 2 == 0) {
            bonusPoints += 1;
        } else if (number % 10 == 5) {
            bonusPoints += 2;
        }



        System.out.printf("%.1f %n", bonusPoints);
        System.out.printf("%.1f", number + bonusPoints);
    }
}
