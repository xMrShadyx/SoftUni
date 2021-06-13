package Conditional.ConditionalExercise;

import java.util.Scanner;

public class SumSeconds {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int time1 = Integer.parseInt(scan.nextLine());
        int time2 = Integer.parseInt(scan.nextLine());
        int time3 = Integer.parseInt(scan.nextLine());

        int minutes = (time1 + time2 + time3) / 60;
        int seconds = (time1 + time2 + time3) % 60;

        if (seconds < 10) {
            System.out.printf("%d:0%d", minutes, seconds);
        } else {
            System.out.printf("%d:%d", minutes, seconds);
        }
    }
}
