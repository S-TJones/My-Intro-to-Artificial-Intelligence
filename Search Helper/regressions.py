


#  Parameters == Weight

def linear_regression(x_list, y_list):

    """
    Prints the X and Y Table
    """
    def linear_table(x_list, y_list):
        spaces = "    "

        # Get the averages
        x_avg, y_avg = sum(x_list)/len(x_list), sum(y_list)/len(y_list)
        x_avg, y_avg = str(x_avg)+spaces, str(y_avg)+spaces

        # Table Construction
        print("\n\t__________\n\t|  X  |  Y  |\n\t|----|----|")
        for num in range(len(x_list)):
            x_value = str(x_list[num]) + spaces
            y_value = str(y_list[num]) + spaces
            print("\t|" + x_value[:5] + "|" + y_value[:5] + "|\n\t|-----|-----|")
        
        print("Average |" + x_avg[:5] + "|" + y_avg[:5] + "|")
        print("\t|_____|_____|")
    

    linear_table(x_list, y_list)

# Driver --------------------------------------------
if __name__ == "__main__":
    print("Testing:\n")

    linear_regression([1,2,3,4,5], [3,4,2,4,5])