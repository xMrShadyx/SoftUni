package ConditionalAdvanced.ConditionalExercise;

import java.util.Scanner;

public class HotelRoom {
	@SuppressWarnings({ "resource", "unused" })
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		String month = scan.nextLine();
		int amountNights = Integer.parseInt(scan.nextLine());
		
		double apartmentPrice = 0.0;
		double studioPrice = 0.0;
		
		switch(month) {
		case "May":
		case "October":
			apartmentPrice = 65;
			studioPrice = 50;
			break;
		case "June":
		case "September":
			apartmentPrice = 68.70;
			studioPrice = 75.20;
			break;
		case "July":
		case "August":
			apartmentPrice = 77;
			studioPrice = 76;
			break;
		}
		
		if (month.equals("May") || month.equals("October")) {
			if (amountNights > 14) {
				studioPrice *= 0.70;
			} else if (amountNights > 7){
				studioPrice *= 0.95;
			}
		}
		
		if (month.equals("June") || month.equals("September")) { 
			if (amountNights > 14) {
				studioPrice *= 0.80;
			}
		}
		
		if (amountNights > 14) {
			apartmentPrice *= 0.9;
		}
		
		System.out.printf("Apartment: %.2f lv.%n", apartmentPrice * amountNights);
		System.out.printf("Studio: %.2f lv.", studioPrice * amountNights);
		
	}

}
