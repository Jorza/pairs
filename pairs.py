def get_pair_list():
    while True:
        try:
            # Get input as a string, turn into a list
            pairs = input("Enter a list of integers, separated by spaces: ")
            pairs = pairs.strip().split()
            # Convert individual numbers from strings into integers
            for i in range(len(pairs)):
                pairs[i] = int(pairs[i])
            return pairs
        except ValueError:
            # Go back to the start if the input wasn't entered correctly
            print("Invalid input")


def find_pairs(the_list):
    # Sum odd => one value even, one value odd
    # Product even => one value even
    # The condition for the odd sum guarantees an even product.
    # Therefore, only need to check the sum.

    # Split list into even and odd values
    even_list = []
    odd_list = []
    for item in the_list:
        new_list = even_list if item % 2 == 0 else odd_list
        new_list.append(item)

    # Find all pairs with one item from the even list and one item from the odd list
    pairs = []
    for odd_item in odd_list:
        for even_item in even_list:
            pairs.append([odd_item, even_item])
    return pairs


def print_pairs(pairs):
    for pair in pairs:
        print(pair)


if __name__ == "__main__":
    print_pairs(find_pairs(get_pair_list()))
