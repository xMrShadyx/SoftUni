package bg.softuniDataTypes.DataTypesLab;

import java.util.Scanner;

public class L01ConvertMetersToKilometers {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double meters = Integer.parseInt(scan.nextLine());

        System.out.printf("%.2f", meters / 1000);
    }
}
