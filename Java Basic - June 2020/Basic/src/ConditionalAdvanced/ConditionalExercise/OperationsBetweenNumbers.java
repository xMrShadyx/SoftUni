package ConditionalAdvanced.ConditionalExercise;

import java.util.Scanner;

public class OperationsBetweenNumbers {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		double num1 = Double.parseDouble(scan.nextLine());
		double num2 = Double.parseDouble(scan.nextLine());
		String operand = scan.nextLine();
		
		double result = 0.0;
		
		if (operand.equals("+")) {
			result = num1 + num2;
			if (result % 2 == 0) {
				System.out.printf("%.0f %s %.0f = %.0f - even", num1, operand, num2, result);
			} else {
				System.out.printf("%.0f %s %.0f = %.0f - odd", num1, operand, num2, result);
			}
		} else if (operand.equals("-")) {
			result = num1 - num2;
			if (result % 2 == 0) {
				System.out.printf("%.0f %s %.0f = %.0f - even", num1, operand, num2, result);
			} else {
				System.out.printf("%.0f %s %.0f = %.0f - odd", num1, operand, num2, result);
			}	
		} else if (operand.equals("*")) {
			result = num1 * num2;
			if (result % 2 == 0) {
				System.out.printf("%.0f %s %.0f = %.0f - even", num1, operand, num2, result);
			} else {
				System.out.printf("%.0f %s %.0f = %.0f - odd", num1, operand, num2, result);
			}
		} else if (operand.equals("%")) {
			if (num2 == 0) {
				System.out.printf("Cannot divide %.0f by zero", num1);
			} else {
				result = num1 % num2;
				System.out.printf("%.0f %s %.0f = %.0f", num1, operand, num2, result);
			}
			
		} else if (operand.equals("/")) {
			if (num2 == 0) {
				System.out.printf("Cannot divide %.0f by zero", num1);
			} else {
				result = num1 / num2;
				System.out.printf("%.0f %s %.0f = %.2f", num1, operand, num2, result);
			}
		}


	}

}
