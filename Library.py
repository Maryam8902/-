#CPIT110 - Library Fine Calculator Project
#GROUP MEMBERS: [ حلا حافظ / مريم حميدان / ليان الزهراني]
#---------------------------------------------------------
#NOTE TO INSTRUCTOR:
#The fine rates and criteria used in this program are
#HYPOTHETICAL values created for educational purposes only.
#They do NOT represent an official library policy.
#---------------------------------------------------------

DAILY_FINE_RATE = 2.0


def calculate_and_display_fine(days):
    fine_amount = days * DAILY_FINE_RATE

    if days <= 3:
        level = "Minor"
    elif days <= 7:
        level = "Moderate"
    else:
        level = "Severe"

    print("\n=============================================")
    print("Overdue Days :", days)
    print("Delay Level  :", level)
    print("Total Fine   :", format(fine_amount, ".2f"), "SAR")
    print("=============================================")


def main():
    print("Welcome to the Library Fine Calculator")

    repeat = "yes"
    while repeat in ("yes", "y"):
        try:
            days_overdue = int(
                input("\nEnter the number of days the book is overdue: ")
            )
        except ValueError:
            print("Error: Please enter a whole number of days.")
        else:
            if days_overdue < 0:
                print("Error: Number of days cannot be negative.")
            elif days_overdue == 0:
                print("The book is on time. No fine.")
            else:
                calculate_and_display_fine(days_overdue)

        repeat = input(
            "\nDo you want to calculate the fine for another book? (yes/no): "
        ).strip().lower()
        while repeat not in ("yes", "y", "no", "n"):
            print("Please enter 'yes' or 'no'.")
            repeat = input(
                "Do you want to calculate the fine for another book? (yes/no): "
            ).strip().lower()

    print("\nThank you for using the Library Fine Calculator. Goodbye!")


if __name__ == "__main__":
    main()
