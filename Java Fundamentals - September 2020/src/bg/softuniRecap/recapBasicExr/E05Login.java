package bg.softuniRecap.recapBasicExr;

import java.util.Scanner;

public class E05Login {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String currentPassword = scan.nextLine();
        String newPassword = new StringBuilder(currentPassword).reverse().toString();
//        System.out.println(newPassword);


        boolean isTrue = true;
        int counter = 1;

        while (isTrue) {
            String whatsPassword = scan.nextLine();
            if (!whatsPassword.equals(newPassword)) {
                System.out.println("Incorrect password. Try again.");
                counter++;
                if (counter == 4) {
                    System.out.printf("User %s blocked!", currentPassword);
                    isTrue = false;
                }
            } else {
                System.out.printf("User %s logged in.", currentPassword);
                isTrue = false;
            }
        }
    }
}
