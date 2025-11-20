def profile_generator(age):
    """Determine life stage based on age"""
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"


def get_user_info():
    """Get basic information from user"""
    print("=== Mini-Profile Generator ===")
    print("Welcome! Let's create your personal profile.\n")

    user_name = input("Enter your name: ").strip()

    while True:
        try:
            birth_year = int(input("Enter your birth year: "))
            current_age = 2025 - birth_year

            if birth_year < 1900:
                print("Birth year cannot be before 1900! Try again.")
                continue
            elif birth_year > 2025:
                print("Birth year cannot be in the future! Try again.")
                continue
            elif current_age < 0:
                print("Invalid birth year! Try again.")
                continue

            break
        except ValueError:
            print("Please enter a valid year (numbers only)!")

    return user_name, current_age


def get_hobbies():
    """Collect hobbies from user"""
    hobbies = []
    print("\nNow let's add your hobbies. Type 'stop' when done:")

    hobby_count = 0
    while True:
        hobby = input(f"Hobby #{hobby_count + 1}: ").strip()

        if hobby.lower() == 'stop':
            break

        if hobby:
            hobbies.append(hobby)
            hobby_count += 1
        else:
            print("Hobby cannot be empty!")

    return hobbies


def display_profile(name, age, life_stage, hobbies):
    """Display user profile beautifully"""
    print("\n" + "=" * 40)
    print("🎉 YOUR PROFILE SUMMARY")
    print("=" * 40)
    print(f"👤 Name: {name}")
    print(f"🎂 Age: {age}")
    print(f"📊 Life Stage: {life_stage}")

    if hobbies:
        print(f"🎯 Favorite Hobbies ({len(hobbies)}):")
        for i, hobby in enumerate(hobbies, 1):
            print(f"   {i}. {hobby}")
    else:
        print("📝 You didn't mention any hobbies.")

    print("=" * 40)


def main():
    """Main program function"""
    name, age = get_user_info()
    life_stage = profile_generator(age)
    hobbies = get_hobbies()
    display_profile(name, age, life_stage, hobbies)


if __name__ == "__main__":
    main()