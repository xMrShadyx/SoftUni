package Conditional.ConditionalMore;

import java.util.Scanner;

public class SleepyTomCat {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int amountOfHolidays = Integer.parseInt(scan.nextLine());

        double OffDays = amountOfHolidays * 127;
        double WorkingDays = (365 - amountOfHolidays) * 63;

        double totalPlayingTime = OffDays + WorkingDays;

        double time = Math.abs(30000 - totalPlayingTime);
        double hours = time / 60;
        double minutes = time % 60;

        if (totalPlayingTime <= 30000) {
            System.out.printf("Tom sleeps well %n%.0f hours and %.0f minutes less for play", Math.floor(hours), minutes);
        } else {
            System.out.printf("Tom will run away%n%.0f hours and %.0f minutes more for play", Math.floor(hours), minutes);

        }
    }
}
