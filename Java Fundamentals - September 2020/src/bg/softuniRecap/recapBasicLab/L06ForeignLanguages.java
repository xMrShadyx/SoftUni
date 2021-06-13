package bg.softuniRecap.recapBasicLab;

import java.util.Scanner;

public class L06ForeignLanguages {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String lang = scan.nextLine();

        String result = "";
        switch (lang) {
            case "England":
            case "USA":
                result = "English";
                break;
            case "Spain":
            case "Argentina":
            case "Mexico":
                result = "Spanish";
                break;
            default:
                result = "unknown";
                break;
        }
        System.out.println(result);
    }
}
