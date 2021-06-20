package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E08BeerKegs {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = Integer.parseInt(scan.nextLine());

        String biggestKeg = "";
        double newVolume = 0;


        while (n > 0) {
            String model = scan.nextLine();
            double radius = Double.parseDouble(scan.nextLine());
            int height = Integer.parseInt(scan.nextLine());

            double volume = Math.PI * radius * radius * height;

            if (volume > newVolume) {
                newVolume = volume;
                biggestKeg = model;
            }
            n--;
        }

        System.out.println(biggestKeg);
    }
}
