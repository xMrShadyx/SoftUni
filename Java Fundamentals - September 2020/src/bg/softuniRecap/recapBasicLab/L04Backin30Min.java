package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;
public class L04Backin30Min {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int hours = Integer.parseInt(scan.nextLine());
        int mins = Integer.parseInt(scan.nextLine()) + 30;

        if (mins > 60) {
            hours++;
            mins -= 60;
        }

        if (hours > 23) {
            hours -= 24;
        }

        System.out.printf("%d:%02d", hours, mins);

    }
}
