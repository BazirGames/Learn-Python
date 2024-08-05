# Type you code here.
def print_roster(roster):
    print("ROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print(f"Jersey number: {jersey_number}, Rating: {rating}")

def add_player(roster):
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    roster[jersey_number] = rating

def remove_player(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        del roster[jersey_number]
        print("Player removed.")
    else:
        print("Player not found.")

def update_player_rating(roster):
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player:\n"))
        roster[jersey_number] = new_rating
        print("Player rating updated.")
    else:
        print("Player not found.")

def output_players_above_rating(roster):
    rating_threshold = int(input("Enter a rating:\n"))
    print(f"\nABOVE {rating_threshold}")
    for jersey_number, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print(f"Jersey number: {jersey_number}, Rating: {rating}")
            
def output_rosters(roster):
    print("ROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print(f"Jersey number: {jersey_number}, Rating: {rating}")
    
    
def print_menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

def main():
    roster = {}

    for i in range(1, 6):
        print(f"Enter player {i}'s jersey number:")
        jersey_number = int(input())
        print(f"Enter player {i}'s rating:\n")
        rating = int(input())
        roster[jersey_number] = rating
        
    output_rosters(roster)
        
    while True:
        
        print_menu()

        choice = input("Choose an option:\n")

        if choice == 'a':
            add_player(roster)
        elif choice == 'd':
            remove_player(roster)
        elif choice == 'u':
            update_player_rating(roster)
        elif choice == 'r':
            output_players_above_rating(roster)
        elif choice == 'o':
            print_roster(roster)
        elif choice == 'q':
                break
            
if __name__ == "__main__":
    main()