import random

def coin_toss():
    result = random.choice(["Heads", "Tails"])
    return result

if __name__ == "__main__":
    print("Welcome to the Heads or Tails game!")
    while True:
        toss = input("Type 'toss' to flip the coin or 'quit' to exit: ").strip().lower()
        if toss == 'toss':
            print(f"The result is: {coin_toss()}")
        elif toss == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please type 'toss' or 'quit'.")