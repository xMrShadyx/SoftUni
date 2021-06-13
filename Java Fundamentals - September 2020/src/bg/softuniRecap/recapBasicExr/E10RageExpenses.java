package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E10RageExpenses {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int lostGamesCount = Integer.parseInt(scan.nextLine());

        double headSetPrice = Double.parseDouble(scan.nextLine());
        double mousePrice = Double.parseDouble(scan.nextLine());
        double keyboardPrice = Double.parseDouble(scan.nextLine());
        double displayPrice = Double.parseDouble(scan.nextLine());

        int trashedHeadset = 0;
        int trashedMouse = 0;
        int trashedKeyboard = 0;
        int trashedDisplay = 0;

        for (int i = 1; i <= lostGamesCount ; i++) {
            if (i % 2 == 0 && i % 3 == 0) {
                trashedKeyboard++;
            }
            if (i % 2 == 0) {
                trashedHeadset++;
            }
            if (i % 3 == 0) {
                trashedMouse++;
            }
        }

        for (int i = 1; i <= trashedKeyboard; i++) {
            if (i % 2 == 0) {
                trashedDisplay++;
            }
        }

        double result = (trashedHeadset * headSetPrice) + (trashedMouse * mousePrice) + (trashedKeyboard * keyboardPrice) + (trashedDisplay * displayPrice);
        System.out.printf("Rage expenses: %.2f lv.",result);
    }
}
