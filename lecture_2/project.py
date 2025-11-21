def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

def main():
    print("Welcome! Let's create your mini-profile.")

    user_name = input("Please enter your full name: ")

    birth_year_str = input("Please enter your birth year:")
    birth_year = int(birth_year_str)

    current_age = 2025 - birth_year

    hobbies = []
    print("Now let's add your favorite hobbies.")
    print("Type 'stop' when you're finished.")

    while True:
        hobby = input("Enter a favourite hobby or type 'stop to finish'")

        if hobby.lower() == "stop":
            break
        elif hobby.strip():
            hobbies.append(hobby)

    life_stage = generate_profile(current_age)

    user_profile = {
        "name": user_name,
        "birth_year": birth_year,
        "current_age": current_age,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

    print('---')
    print("Profile Summary: ")
    print(f"Name: {user_profile['name']}")
    print(f"Birth Year: {user_profile['birth_year']}")
    print(f"Current Age: {user_profile['current_age']}")
    print(f"Life Stage: {user_profile['life_stage']}")

    if not user_profile['hobbies']:
        print("Hobbies: You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies: ({len(user_profile['hobbies'])})")
        for hobby in user_profile['hobbies']:
            print(f" - {hobby}")

        print('---')

if __name__ == "__main__":
    main()