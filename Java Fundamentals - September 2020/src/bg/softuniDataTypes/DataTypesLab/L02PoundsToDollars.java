package bg.softuniDataTypes.DataTypesLab;

import java.util.Scanner;

public class L02PoundsToDollars {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double pounds = Double.parseDouble(scan.nextLine());

        System.out.printf("%.3f", pounds * 1.31);
    }
}
