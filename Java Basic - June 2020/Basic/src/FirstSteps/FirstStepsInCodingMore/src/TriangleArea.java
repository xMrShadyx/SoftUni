package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double side1 = Double.parseDouble(scan.nextLine());
        double side2 = Double.parseDouble(scan.nextLine());

        double result = side1 * side2 / 2;
        System.out.printf("%.02f", result);
    }
}
