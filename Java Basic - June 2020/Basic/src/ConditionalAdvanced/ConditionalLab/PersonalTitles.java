package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class PersonalTitles {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double age = Double.parseDouble(scan.nextLine());;
        String type = scan.nextLine();
        String result = "";
        switch (type) {
            case "f":
                if (age < 16) {
                    result = "Miss";
                } else {
                    result = "Ms.";
                }
                break;
            case "m":
                if (age < 16) {
                    result = "Master";
                } else {
                    result = "Mr.";
                }
        }
        System.out.println(result);
    }
}
