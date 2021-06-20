
import os, sys

def main_menu():
    print("************************************")
    print("*Enter [ 0 ] - Exit")
    print("*Enter [ 1 ] - Exit")
    print("*Enter [ 2 ] - Exit")
    print("*Enter [ 3 ] - Exit")
    print("*Enter [ 4 ] - Exit")
    print("************************************")

# Driver for the program
if __name__ == "__main__":
    print("** WELCOME **")
    print()

    # Simple error catch
    try:
        while True:
            main_menu()
            search_option = input("* Enter an option from above - ").strip()

            # Check for option
            if search_option.lower() not in []:
                print(f"| You entered \'{search_option}\'.")
                print("| That\'s not a valid option. Please try again.")
                continue
            
            # Switch
            if search_option == "1":
                pass
            elif search_option == "2":
                pass
            elif search_option == "3":
                pass
            else:
                print("** GOODBYE **")
                break

    except KeyboardInterrupt:
        print("| We see that you abruptly ended our program :(")
        print("| Did something go wrong?")
        print("| If yes, please make an\'ISSUE\' at this repo \'https://github.com/S-TJones/My-Intro-to-Artificial-Intelligence\'")

        # exits the program
        sys.exit("\n| GOODBYE!!")
    except:
        print("| ERROR: Something went wrong!! :(\n| Please try again.\n| Or make an\'ISSUE\' at this repo \'https://github.com/S-TJones/My-Intro-to-Artificial-Intelligence\'")

        # exits the program
        sys.exit("\n| We apologize for the inconvenience.")