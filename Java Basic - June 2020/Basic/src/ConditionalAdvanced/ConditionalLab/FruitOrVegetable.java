package ConditionalAdvanced.ConditionalLab;

import java.util.Scanner;

public class FruitOrVegetable {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String type = scan.nextLine();

        String result = "";
        switch (type) {
            case "banana":
            case "apple":
            case "kiwi":
            case "cherry":
            case "lemon":
            case "grapes":
                result = "fruit";
                break;
            case "tomato":
            case "cucumber":
            case "pepper":
            case "carrot":
                result = "vegetable";
                break;
            default:
                result = "unknown";
                break;
        }
        System.out.println(result);
    }
}
