package Conditional.ConditionalMore;

import java.util.Scanner;

public class Firm {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int neededHours = Integer.parseInt(scan.nextLine());
        int dayWeHave = Integer.parseInt(scan.nextLine());
        int amountWorkers = Integer.parseInt(scan.nextLine());

        double daysCanWork = (dayWeHave * 0.9) * 8;
        double overTime = amountWorkers * (2 * dayWeHave);

        double totalTime = Math.floor(daysCanWork + overTime);

        if (totalTime >= neededHours) {
            System.out.printf("Yes!%.0f hours left.", totalTime - neededHours);
        } else {
            System.out.printf("Not enough time!%.0f hours needed.", neededHours - totalTime);
        }
    }

}
