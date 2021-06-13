package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class HousePainting {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double x  = Double.parseDouble(scan.nextLine());
        double y  = Double.parseDouble(scan.nextLine());
        double h  = Double.parseDouble(scan.nextLine());

        double sideWall = x * y;
        double window = 1.5 * 1.5;
        double twoSides = 2 * sideWall - 2 * window;
        double backWall = x * x;
        double entrance = 1.2 * 2;
        double backAndFront = 2 * backWall - entrance;
        double totalSpace = twoSides + backAndFront;
        double totalGPaint = totalSpace / 3.4;

        //roof
        double twoSquares = 2 * (x * y);
        double twoRectangles = 2 * (x * h) / 2;
        double totalRoof = twoSquares + twoRectangles;
        double totalRPaint = totalRoof / 4.3;

        System.out.printf("%.02f", totalGPaint);
        System.out.println();
        System.out.printf("%.02f", totalRPaint);




    }
}
