package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E09SpiceMustFlow {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int cyield = Integer.parseInt(scan.nextLine());

        int days = 0;
        int newCyield = 0;

        while (cyield >= 100) {

            newCyield += (cyield - 26);
            days++;
            cyield -= 10;
        }
        if (newCyield > 0)
            newCyield -= 26;

        System.out.printf("%d%n%d", days, newCyield);
    }
}
