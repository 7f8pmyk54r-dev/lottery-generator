import random

def generate_lottery_numbers(min_num=1, max_num=49, count=6):
    """Generate random lottery numbers without repetition"""
    return sorted(random.sample(range(min_num, max_num + 1), count))

def main():
    print("=" * 50)
    print("🎰 LOTTERY NUMBER GENERATOR 🎰")
    print("=" * 50)
    
    # Standard Lottery
    print("\n📊 Standard Lottery (6 numbers, 1-49):")
    numbers = generate_lottery_numbers(1, 49, 6)
    print(f"Your numbers: {numbers}")
    
    # Multiple draws
    print("\n📊 5 Different Draws:")
    for i in range(1, 6):
        numbers = generate_lottery_numbers(1, 49, 6)
        print(f"Draw {i}: {numbers}")
    
    # Powerball style
    print("\n📊 Powerball Style (5 numbers 1-69 + 1 bonus 1-26):")
    main_numbers = generate_lottery_numbers(1, 69, 5)
    bonus = random.randint(1, 26)
    print(f"Numbers: {main_numbers}")
    print(f"Bonus: {bonus}")
    
    # EuroMillions style
    print("\n📊 EuroMillions Style (5 numbers 1-50 + 2 stars 1-12):")
    main_numbers = generate_lottery_numbers(1, 50, 5)
    stars = sorted(random.sample(range(1, 13), 2))
    print(f"Numbers: {main_numbers}")
    print(f"Stars: {stars}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
