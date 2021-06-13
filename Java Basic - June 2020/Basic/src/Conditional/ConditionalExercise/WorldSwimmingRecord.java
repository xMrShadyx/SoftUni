package Conditional.ConditionalExercise;

import java.util.Scanner;

public class WorldSwimmingRecord {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double record = Double.parseDouble(scan.nextLine());
        double distance = Double.parseDouble(scan.nextLine());
        double time = Double.parseDouble(scan.nextLine());



        double bonusMeters = Math.floor(distance / 15) * 12.5;
        double needToSwim = distance * time + bonusMeters;

        if (needToSwim < record) {
            System.out.printf("Yes, he succeeded! The new world record is %.2f seconds.", needToSwim);
        } else {
            System.out.printf("No, he failed! He was %.2f seconds slower.", needToSwim - record);
        }

    }
}
