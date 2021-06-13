package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class CircleAreaAndPerimeter {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double r = Double.parseDouble(scan.nextLine());

        double calculatedArea = (r * Math.PI) * 2;
        double calculateParameter = r * r * Math.PI;


        System.out.printf("%.02f", calculateParameter);
        System.out.println();
        System.out.printf("%.02f", calculatedArea);


    }
}
