CPIT110 - Library Fine Calculator Project
GROUP MEMBERS: [ حلا حافظ / مريم حميدان / ليان الزهراني]
---------------------------------------------------------
NOTE TO INSTRUCTOR:
The fine rates and criteria used in this program are
HYPOTHETICAL values created for educational purposes only.
They do NOT represent an official library policy.
---------------------------------------------------------
DAILY_FINE_RATE = 2.0
def main():
print("Welcome to the Library Fine Calculator")
repeat = "yes"
while repeat == "yes" or repeat == "y" or repeat == "YES" or repeat == "Y":
    days_overdue = int(input("\nEnter the number of days the book is overdue: "))

    if days_overdue < 0:
        print("Error: Number of days cannot be negative. Please enter a positive number.")
    elif days_overdue == 0:
        print("The book is returned on time. No fine.")
    else:
        calculate_and_display_fine(days_overdue)

    repeat = input("\nDo you want to calculate the fine for another book? (yes/no): ")
    while (repeat != "yes" and repeat != "y" and repeat != "YES" and repeat != "Y" and
           repeat != "no" and repeat != "n" and repeat != "NO" and repeat != "N"):
        print("Please enter 'yes' or 'no'.")
        repeat = input("Do you want to calculate the fine for another book? (yes/no): ")

print("\nThank you for using the Library Fine Calculator. Goodbye!")
def calculate_and_display_fine(days):
fine_amount = days * DAILY_FINE_RATE
if days <= 3:
    level = "Minor"
    message = "Please return your books on time next time."
elif days <= 7:
    level = "Moderate"
    message = "Warning: Your delay is getting longer. Please return the book soon."
else:
    level = "Severe"
    message = "URGENT WARNING: Your delay is very serious! Return the book immediately and pay the fine."

print("\n=============================================")
print("Overdue Days :", days)
print("Delay Level  :", level)
print("Total Fine   :", format(fine_amount, ".2f"), "SAR")
print("Message      :", message)
print("=============================================")
main()
