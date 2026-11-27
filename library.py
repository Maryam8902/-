# CPIT110 - Library Fine Calculator Project
# GROUP MEMBERS: [ حلا حافظ / مريم حميدان / ليان الزهراني]

# ———————————————————
# NOTE TO INSTRUCTOR:
# The fine rates and criteria used in this program are
# HYPOTHETICAL values created for educational purposes only.
# They do NOT represent an official library policy.
# ———————————————————

DAILY_FINE_RATE = 2.0
MINOR_MAX_DAYS = 3
MODERATE_MAX_DAYS = 7


def get_days_overdue():
    while True:
        try:
            return int(input("\nEnter the number of days the book is overdue: "))
        except ValueError:
            print("Please enter a whole number.")


def display_fine(days_overdue):
    fine_amount = days_overdue * DAILY_FINE_RATE

    if days_overdue <= MINOR_MAX_DAYS:
        level = "Minor"
        message = "Please return your books on time next time."
    elif days_overdue <= MODERATE_MAX_DAYS:
        level = "Moderate"
        message = "Warning: Your delay is getting longer. Please return the book soon."
    else:
        level = "Severe"
        message = "URGENT WARNING: Your delay is very serious! Return the book immediately and pay the fine."

    print("\n" + "=" * 45)
    print("Overdue Days :", days_overdue)
    print("Delay Level  :", level)
    print(f"Total Fine   : {fine_amount:.2f} SAR")
    print("Message      :", message)
    print("=" * 45)


print("Welcome to the Library Fine Calculator")

repeat = "yes"

while repeat in ("yes", "y"):
    days_overdue = get_days_overdue()

    if days_overdue < 0:
        print("Error: Number of days cannot be negative. Please enter a positive number.")
    elif days_overdue == 0:
        print("The book is returned on time. No fine.")
    else:
        display_fine(days_overdue)

    repeat = input("\nDo you want to calculate the fine for another book? (yes/no): ").strip().lower()

    while repeat not in ("yes", "y", "no", "n"):
        print("Please enter 'yes' or 'no'.")
        repeat = input("Do you want to calculate the fine for another book? (yes/no): ").strip().lower()

print("\nThank you for using the Library Fine Calculator. Goodbye!")