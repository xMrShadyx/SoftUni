package bg.softuniDataTypes.DataTypesExr;

import java.util.Scanner;

public class E04SumOfChars {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int inputNums = Integer.parseInt(scan.nextLine());

        int result = 0;
        for (int i = 0; i < inputNums; i++) {
            String enteringChar = scan.nextLine();
            char letter = enteringChar.charAt(0);
            result += (int) letter;

        }
        System.out.printf("The sum equals: %d",result);



    }
}
