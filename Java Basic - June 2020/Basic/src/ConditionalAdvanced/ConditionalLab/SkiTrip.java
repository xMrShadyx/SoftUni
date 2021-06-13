package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class SkiTrip {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int BookingDays = Integer.parseInt(scan.nextLine()) - 1;
        String RoomType = scan.nextLine();
        String feedback = scan.nextLine();
        double result = 0.0;

        switch (RoomType) {
            case "room for one person":
                result = 18;
                break;
            case "apartment":
                if (BookingDays < 10) {
                    result = 25 * 0.7;
                } else if (BookingDays < 15) {
                    result = 25 * 0.65;
                } else if (BookingDays > 15) {
                    result = 25 * 0.5;
                }
                break;
            case "president apartment":
                if (BookingDays < 10) {
                    result = 35 * 0.9;
                } else if (BookingDays < 15) {
                    result = 35 * 0.85;
                } else if (BookingDays > 15) {
                    result = 35 * 0.8;
                }
                break;
        }

        if (feedback.equals("positive")) {
            result *= 1.25;
        } else {
            result *= 0.9;
        }

        System.out.printf("%.2f", result * BookingDays);
    }
}
