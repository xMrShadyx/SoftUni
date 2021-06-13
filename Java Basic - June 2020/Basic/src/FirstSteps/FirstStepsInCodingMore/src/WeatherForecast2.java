package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class WeatherForecast2 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double InputNum = Double.parseDouble(scan.nextLine());

        if (InputNum >= 26 && InputNum <= 35) {
            System.out.println("Hot");
        } else if (InputNum >= 20.1 && InputNum <= 25.9) {
            System.out.println("Warm");
        } else if (InputNum >= 15 && InputNum <= 20) {
            System.out.println("Mild");
        } else if (InputNum >= 12 && InputNum <= 14.9) {
            System.out.println("Cool");
        } else if (InputNum >= 5 && InputNum <= 11.9) {
            System.out.println("Cold");
        } else {
            System.out.println("unknown");
        }

    }
}
