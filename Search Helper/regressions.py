


#  Parameters == Weight

def linear_regression(x_list, y_list):
    """
    Prints the X and Y Table
    """

    spaces = "            "

    # Get the averages
    x_avg, y_avg = sum(x_list)/len(x_list), sum(y_list)/len(y_list)
    x_sub_sum, xy = 0, 0
    y_sub_list = list()

    # Table Construction
    print("\nOLS Regression Table")
    print("\n\t____________________________________________________")
    print("\t|     |     |     ~ |     ~ |    ~ 2  |    ~    ~  |\n\t|  X  |  Y  | X - X | Y - Y | (X-X)   | (X-X)(Y-Y) |")
    print("\t|-----|-----|-------|-------|---------|------------|")
    for num in range(len(x_list)):
        x, y = x_list[num], y_list[num]
        
        x_sub, y_sub = x - x_avg, y - y_avg
        y_sub_list.append(y_sub)
        x_squared, x_y_sub = x_sub * x_sub, x_sub * y_sub
        x_sub_sum += x_squared
        xy += x_y_sub
        
        x_squared = str(x_squared) + spaces
        x_y_sub = str(x_y_sub) + spaces

        x, y, x_sub, y_sub = str(x) + spaces, str(y) + spaces, str(x_sub) + spaces, str(y_sub) + spaces
        
        print(f"\t|{x[:5]}|{y[:5]}|{x_sub[:7]}|{y_sub[:7]}|{x_squared[:9]}|{x_y_sub[:12]}|")
        print("\t|-----|-----|-------|-------|---------|------------|")
    
    w = xy / x_sub_sum
    b = y_avg - (w * x_avg)
    b_result = f"{y_avg} = b + {w} * {x_avg}\n  b = {b}"

    x_avg_str, y_avg_str = str(x_avg)+spaces, str(y_avg)+spaces
    x_sub_sum, xy = str(x_sub_sum)+spaces, str(xy)+spaces

    print(f"Average |{x_avg_str[:5]}|{y_avg_str[:5]}|     Summation |{x_sub_sum[:9]}|{xy[:12]}|")
    print("\t|_____|_____|               |_________|____________|")

    print(f"\nw = {xy} / {x_sub_sum} = {w}\n")
    print(b_result)

    print("\n\nCalculate Loss - Mean Square Error\n")

    yp_list = list()
    for x in x_list:
        yp = b + (w*x)
        yp_list.append(yp)
        print(f"    Yp = {b} + {w} * {x} = {yp}")

    y_sub_squared_list = list()
    yp_squared_list = list()

    # Table Construction
    print("\n\nCalculate R Squared")
    print("\n\t_________________________________________________________________________")
    print("\t|     |     |     ~ |    ~ 2  |     |      |       2 |     ~  |     ~ 2 |")
    print("\t|  X  |  Y  | Y - Y | (Y-Y)   |  Yp | Yp-Y | (Yp-Y)  | (Yp-Y) | (Yp-Y)  |")
    print("\t|-----|-----|-------|---------|-----|------|---------|--------|---------|")
    for num in range(len(x_list)):
        x, y, yp, y_sub = x_list[num], y_list[num], yp_list[num], y_sub_list[num]

        y_squared = y_sub * y_sub
        yp_sub_y = yp - y
        yp_sub_y_squared = yp_sub_y * yp_sub_y
        yp_sub = yp - y_avg
        yp_squared = yp_sub * yp_sub

        y_sub_squared_list.append(y_squared)
        yp_squared_list.append(yp_sub_y_squared)

        x, y, yp, y_sub = str(x) + spaces, str(y) + spaces, str(yp) + spaces, str(y_sub) + spaces
        y_squared, yp_sub, yp_squared = str(y_squared) + spaces, str(yp_sub) + spaces, str(yp_squared) + spaces
        yp_sub_y, yp_sub_y_squared = str(yp_sub_y) + spaces, str(yp_sub_y_squared) + spaces

        print(f"\t|{x[:5]}|{y[:5]}|{y_sub[:7]}|{y_squared[:9]}|{yp[:5]}|{yp_sub_y[:6]}|{yp_sub_y_squared[:9]}|{yp_sub[:8]}|{yp_squared[:9]}|")
        print("\t|-----|-----|-------|---------|-----|------|---------|--------|---------|")

    yp_sub_sum = sum(y_sub_squared_list)
    yp_squared_sum = sum(yp_squared_list)

    r2 = yp_squared_sum / yp_sub_sum
    print("\nMean Squared Error\n-------------------------")
    print(f"MSE - {yp_squared_sum/len(yp_squared_list)}")
    # yp_avg = sum(yp_list) / len(yp_list))
    # for y in y_list:
    #     mean_square = (yp_avg - y)**2 / len(yp_list)
    #     print("mean square - ", mean_square)
    print("\nR Squared Error\n-------------------------")
    print(f"\nR^2 = 1 - ({yp_squared_sum}/{yp_sub_sum}) ===> {1-r2}\n")

def get_updates(e, n, b, type="MB"):
    """
        e: epochs
        n: number of records / dataset size
        b: batch size
        type: type of Gradient Decent
            - Mini-Batch(MB)
            - Stochastic(S)
            - Batch(B)
    """

    # Updates per epoch
    if type == "MB":
        batches = n / b
        print(batches, "BTCH")
        updates = batches * e
    elif type == "S":
        updates = n * e
    elif type == "B":
        updates = (n/n) * e

    print(f"Total Updates for {type} = ", updates)

def calc_loss(learning_rate, weight, bias, x_list, y_list):
    import random

    pairs = list(zip(x_list, y_list))
    length = len(y_list)

    random_num = random.randint(0, length)
    x, y = pairs[random_num]
    print(f"Row number {random_num+1}: X-{x} | Y-{y}\n")

    y_pred = (weight * x) + bias
    y_sub = y_pred - y
    mse = (y_sub*y_sub) / 2
    print(f"MSE: {mse}")
    
    dL_dW = 2 * (y_pred - y) * x
    dL_db = 2 * (y_pred - y)
    print(f"Derivative of loss with respect to w: {dL_dW}")
    print(f"Derivative of loss with respect to b: {dL_db}")

    w_new = weight - (learning_rate * dL_dW)
    b_new = bias - (learning_rate * dL_db)
    print(f"W new = {w_new}\nb new = {b_new}")
    

# Driver --------------------------------------------
if __name__ == "__main__":

    # linear_regression([1,2,3,4,5], [3,4,2,4,5])
    x_list = [95, 85, 80, 70, 60]
    y_list = [85, 95, 70, 65, 70]
    # x_list = [1.47, 1.5, 1.52, 1.55, 1.57, 1.6, 1.63, 1.65, 1.68, 1.7, 1.73, 1.75, 1.78, 1.8, 1.83]
    # y_list = [52.21, 53.12, 54.48, 55.84, 57.2, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.1, 69.92, 72.19, 74.46]
    linear_regression(x_list, y_list)

    print("--------------------------------------\n")
    # get_updates(2, 2000, 100, type="S")

    # get_updates(20, 2000, 1, type="B")
    # get_updates(10, 2000, 1, type="S")
    # get_updates(10, 2000, 100, type="MB")

    # get_updates(10, 500, 1, type="B")
    # get_updates(20, 500, 1, type="S")
    # get_updates(5, 500, 50, type="MB")

    get_updates(200, 7, 1, type="S")
    get_updates(300, 7, 2, type="MB")
    print("\n--------------------------------------")

    calc_loss(0.5, 0.2, 0.1, [0.22, 0.24, 0.33, 0.37, 0.44, 0.44], [0.22, 0.58, 0.2, 0.55, 0.39, 0.54])