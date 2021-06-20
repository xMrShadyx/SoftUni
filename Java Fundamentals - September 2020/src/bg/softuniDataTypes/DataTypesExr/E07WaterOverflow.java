package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E07WaterOverflow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());

        int currentWater = 0;

        while (n > 0) {
            int water = Integer.parseInt(scan.nextLine());

            if (currentWater <= 255) {
                currentWater += water;
                if (currentWater > 255) {
                    currentWater -= water;
                    System.out.println("Insufficient capacity!");
                }
            } else {
                System.out.println("Insufficient capacity!");
            }

            n--;
        }
        System.out.println(currentWater);
    }
}
