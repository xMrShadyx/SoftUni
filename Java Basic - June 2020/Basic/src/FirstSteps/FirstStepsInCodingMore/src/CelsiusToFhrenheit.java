package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class CelsiusToFhrenheit {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // °F = °C × 1,8 + 32

        double fahrenheit = Double.parseDouble(scan.nextLine());

        double result = fahrenheit * 1.8 + 32;
        System.out.printf("%.02f",result);
    }
}
