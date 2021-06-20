package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E02SumDigits {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String number = scan.nextLine();

        int result = 0;
        for (int i = 0; i < number.length(); i++) {
//            System.out.println(number.charAt(i));
            result += (char) number.charAt(i) - 48;
        }
        System.out.println(result);
    }
}
