package bg.softuniRecap.recapBasicMor;

import java.util.Scanner;

public class M02EnglishNameofLD {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String number = scan.nextLine();
        int lastDigit = number.length();
        int itsWorking = number.charAt(lastDigit - 1) - 48;
//        System.out.println(itsWorking);

        switch (itsWorking) {
            case 1:
                System.out.println("one");
                break;
            case 2:
                System.out.println("two");
                break;
            case 3:
                System.out.println("three");
                break;
            case 4:
                System.out.println("four");
                break;
            case 5:
                System.out.println("five");
                break;
            case 6:
                System.out.println("six");
                break;
            case 7:
                System.out.println("seven");
                break;
            case 8:
                System.out.println("eight");
                break;
            case 9:
                System.out.println("nine");
                break;
            case 0:
                System.out.println("zero");
                break;
        }
    }
}
