package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L07TheatrePromotion {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String Day = scan.nextLine();
        int age = Integer.parseInt(scan.nextLine());

        int result = 0;
        switch (Day) {
            case "Weekday":
                if (0 <= age && age <= 18) {
                    result = 12;
                } else if (age > 18 && age <= 64) {
                    result = 18;
                } else if (age > 64 && age <= 122) {
                    result = 12;
                } else {
                    result = -1;
                }
                break;
            case "Weekend":
                if (0 <= age && age <= 18) {
                    result = 15;
                } else if (age > 18 && age <= 64) {
                    result = 20;
                } else if (age > 64 && age <= 122) {
                    result = 15;
                } else {
                    result = -1;
                }
                break;
            case "Holiday":
                if (age >= 0 && age <= 18) {
                    result = 5;
                } else if (age > 18 && age <= 64) {
                    result = 12;
                } else if (age > 64 &&age <= 122) {
                    result = 10;
                } else {
                    result = -1;
                }
                break;
            default:
                result = -1;
                break;
        }

        if (result == -1) {
            System.out.println("Error!");
        } else {
            System.out.printf("%d$", result);
        }
    }
}
