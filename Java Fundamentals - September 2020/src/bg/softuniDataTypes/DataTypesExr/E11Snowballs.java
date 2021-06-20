package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E11Snowballs {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int number = Integer.parseInt(scan.nextLine());
        int counter = 0;

        double maxValue =  Double.MIN_VALUE;
        int endSnowball = 0;
        int endSnowballTime = 0;
        int endSnowballQuality = 0;

        while (counter < number) {
            int snowball = Integer.parseInt(scan.nextLine());
            int snowballTime = Integer.parseInt(scan.nextLine());
            int snowballQuality = Integer.parseInt(scan.nextLine());

            long formula = (long) Math.pow(snowball / snowballTime, snowballQuality);

            if (formula > maxValue){
                maxValue = formula;
                endSnowball = snowball;
                endSnowballTime = snowballTime;
                endSnowballQuality = snowballQuality;
            }
            counter++;
        }
        System.out.printf("%d : %d = %.0f (%d)",endSnowball, endSnowballTime, maxValue, endSnowballQuality );
    }
}
