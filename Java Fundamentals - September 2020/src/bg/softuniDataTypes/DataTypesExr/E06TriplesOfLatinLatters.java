package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E06TriplesOfLatinLatters {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = Integer.parseInt(scan.nextLine());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    int firstNum = i + 97;
                    int secondNum = j + 97;
                    int thirdNum = k + 97;

                    System.out.printf("%c%c%c%n", firstNum, secondNum, thirdNum);
                }
            }
        }
    }
}
