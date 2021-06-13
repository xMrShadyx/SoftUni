package FirstSteps.FirstStepsInCodingMore.src;

import java.util.Scanner;

public class TrainingLab {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double w = Double.parseDouble(scan.nextLine());
        double h = Double.parseDouble(scan.nextLine());

        double wToCm = w * 100;
        double hToCm = h * 100;

        int rows = (int) (wToCm / 120);
//        System.out.println(rows);

        hToCm -= 100;
        int burosInRow = (int) (hToCm / 70);
//        System.out.println(burosInRow);

        double totalBuros = rows * burosInRow - 3;
        System.out.printf("%.0f", totalBuros);
    }
}
