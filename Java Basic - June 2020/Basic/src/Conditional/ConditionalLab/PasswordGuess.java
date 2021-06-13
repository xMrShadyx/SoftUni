package Conditional.ConditionalLab;

import java.util.Scanner;

public class PasswordGuess {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String pass = scan.nextLine();
        String result = "";
        if (pass.equals("s3cr3t!P@ssw0rd")) {
            result = "Welcome";
        } else {
            result = "Wrong password!";
        }
        System.out.println(result);
    }
}
