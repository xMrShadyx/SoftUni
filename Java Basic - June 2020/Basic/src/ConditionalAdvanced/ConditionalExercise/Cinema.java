package ConditionalAdvanced.ConditionalExercise;

import java.util.Scanner;

public class Cinema {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String typeOfMovie = scan.nextLine();
        int rows = Integer.parseInt(scan.nextLine());
        int columns = Integer.parseInt(scan.nextLine());

        double outcome = 0.0;

        switch (typeOfMovie) {
            case "Premiere":
                outcome = (rows * columns) * 12;
                break;
            case "Normal":
                outcome = (rows * columns) * 7.5;
                break;
            case "Discount":
                outcome = (rows * columns) * 5;
                break;
        }

        System.out.printf("%.2f leva", outcome);
    }

}
