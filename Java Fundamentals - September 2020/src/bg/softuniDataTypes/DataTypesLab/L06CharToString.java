package bg.softuniDataTypes.DataTypesLab;

import java.util.Scanner;

public class L06CharToString {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String char1 = scan.nextLine();
        String char2 = scan.nextLine();
        String char3 = scan.nextLine();

        System.out.printf("%s%s%s", char1, char2, char3);
    }
}
