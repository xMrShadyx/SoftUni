package ConditionalAdvanced.ConditionalExercise;

import java.util.Scanner;

public class Journey {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		double budget = Double.parseDouble(scan.nextLine());
		String season = scan.nextLine();
		
		String resultTxt = "";
		String location = "";
		double resultPrice = 0.0;
		
		
		if (budget <= 100) {
			if (season.equals("summer")) {
				resultTxt = "Somewhere in Bulgaria";
				location = "Camp -";
				resultPrice = budget * 0.3;
				
			} else {
				resultTxt = "Somewhere in Bulgaria";
				location = "Hotel -";
				resultPrice = budget * 0.7;
			}
		} else if (budget <= 1000) {
			if (season.equals("summer")) {
				resultTxt = "Somewhere in Balkans";
				location = "Camp -";
				resultPrice = budget * 0.4;
				
			} else {
				resultTxt = "Somewhere in Balkans";
				location = "Hotel -";
				resultPrice = budget * 0.8;
			}
		} else {
			resultTxt = "Somewhere in Europe";
			location = "Hotel -";
			resultPrice = budget * 0.9;
		}
		
		System.out.println(resultTxt);
		System.out.printf("%s %.2f",location, resultPrice);
		
		
	}
}