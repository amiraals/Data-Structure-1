from enum import Enum
import random

# Defining an Enum for different Chocolate types
class ChocolateType(Enum):
    ALMOND = "Almond chocolate"
    PEANUT_BUTTER = "Peanut butter chocolate"
    MILK = "Milk chocolate"
    DARK = "Dark chocolate"
    WHITE = "White chocolate"
    CARAMEL = "Caramel Chocolate"

class Chocolate:
    """Class representing a chocolate"""
    def __init__(self, weight, price, chocolate_type, id_number):
        # The chocolates atributes
        self.weight = weight
        self.price = price
        self.type = chocolate_type
        self.id = id_number

# Defining a function to generate chocolates
def generate_chocolates(num_chocolates):
    chocolates = []  # Creating empty list to store the generated chocolates
    for i in range(1, num_chocolates + 1):
        weight = random.randint(2, 12)  # Assuming weight range between 2gm to 12gm
        price = random.randint(5, 45)    # Assuming price range between 5 to 45 AED
        chocolate_type = random.choice(list(ChocolateType))  # Choses a random chocolate from the ENUM of ChocolateType
        chocolates.append(Chocolate(weight, price, chocolate_type, i))  #Appending the chocolate object to the chocolate list
    return chocolates

# Defining a function to generate student names
def generate_student_names(num_students):
    return [f"Student {i+1}" for i in range(num_students)]

# Defining an iterative function to distribute chocolates to students
def distribute_chocolates_iteratively(chocolates, students):
    distribution = {}   # Creating an empty dictionary to store the distribution of chocolates to students
    # Iterating over the range of the number of students
    for i in range(len(chocolates)):
            distribution[students[i]] = chocolates[i]    # Assigning the chocolate at index i to the student at index i
    return distribution

# Defining a recursive function to distribute chocolates to  students
def distribute_chocolates_recursively(chocolates, students, index=0, distribution=None):
    if distribution is None:
        distribution = {}    # Creating an empty dictionary to store the distribution of chocolates to students
    if index >= len(students) or index >= len(chocolates):  #Base Case
        return distribution
    distribution[students[index]] = chocolates[index]  # Assigning the chocolate at the current index to the student at the current index in the distribution dictionary
    return distribute_chocolates_recursively(chocolates, students, index + 1, distribution)   # Recursive call: Increase the index and call the function again with the updated index and distribution

# Generating chocolates
chocolates = generate_chocolates(25)

# Generating list of student names based on the number of chocolates
students = generate_student_names(len(chocolates))

if len(chocolates) == 0:
    print("Error: There is no Chocolates/Students to distribute the chocolate to")  # Displaying an error message if there were no chocolates/students available
else:
    # Distributing chocolates iteratively using the iterative function
    distribution_iterative_simple = distribute_chocolates_iteratively(chocolates, students)
    print("Iterative Distribution:")
    for name, chocolate in distribution_iterative_simple.items():
        print(name, "received", chocolate.type.value, "with ID", chocolate.id, "and weight of", chocolate.weight, "gm", "and a price of", chocolate.price, "AED")

    # Distributing chocolates recursively using the recurssive function
    distribution_recursive_simple = distribute_chocolates_recursively(chocolates, students)
    print()
    print("Recursive Distribution:")
    for name, chocolate in distribution_recursive_simple.items():
        print(name, "received", chocolate.type.value, "with ID", chocolate.id, "and weight of", chocolate.weight, "gm", "and a price of", chocolate.price, "AED")

    # Defining a function to sort chocolates based on a given key using the merge sort algorithm
    def merge_sort(chocolates, key):
        if len(chocolates) <= 1:  # Base Case
            return chocolates
        mid = len(chocolates) // 2  # Finding the middle index of the chocolates list

        # Splitting the chocolates list into two halves (left half and right half)
        left_half = chocolates[:mid]
        right_half = chocolates[mid:]

        # Recursive calls, sorting the left_half and right_half using the merge_sort function
        left = merge_sort(left_half, key)
        right = merge_sort(right_half, key)

        # Merging the sorted left and right halves using the merge function and then returning the merged result
        return merge(left, right, key)


    # Defining a function to merge two sorted lists into a single sorted list based on a given key
    def merge(left, right, key):
        merged = []    # Creating an empty list to store the merged result
        i = j = 0    # Initializing two pointers, i and j, for the left and right lists
        while i < len(left) and j < len(right):
            # Comparing the elements from the left and right lists, and merging them in sorted order
            if getattr(left[i], key) <= getattr(right[j], key):
                # If the value in the left element is smaller or equal, we append it to the merged list
                merged.append(left[i])
                i += 1
            else:
                # If the value in the right element is smaller, we append it to the merged list
                merged.append(right[j])
                j += 1

        # Extending the merged list with any remaining elements from the left and right lists
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


    # Sorting the chocolates by weight and price
    chocolates_sorted_by_weight = merge_sort(chocolates, 'weight')
    chocolates_sorted_by_price = merge_sort(chocolates, 'price')

    print()
    print("Chocolates sorted by weight:")
    for chocolate in chocolates_sorted_by_weight:
        print("Type:", chocolate.type.value, ", ID:", chocolate.id, ", Weight:", chocolate.weight, ", Price:",
              chocolate.price)

    print()
    print("Chocolates sorted by price:")
    for chocolate in chocolates_sorted_by_price:
        print("Type:", chocolate.type.value, ", ID:", chocolate.id, ", Weight:", chocolate.weight, ", Price:",
              chocolate.price)


    # Adjusting the binary search to finding chocolate, then find which student has it
    def binary_search_chocolates(chocolates, target, key):
        low = 0
        high = len(chocolates) - 1

        while low <= high:
            mid = (low + high) // 2  # Calculating the middle index
            if key == "weight":
                mid_val = chocolates[mid].weight  # Getting the weight value of the chocolate at the middle index
            elif key == "price":
                mid_val = chocolates[mid].price  # Getting the price value of the chocolate at the middle index
            else:
                return "invalid key"

            if mid_val < target:
                low = mid + 1  # If the middle value is less than the target, we narrow the search range to the upper half
            elif mid_val > target:
                high = mid - 1  # If the middle value is greater than the target, we narrow the search range to the lower half
            else:
                    chocolate = chocolates[mid]
                    student_name = students[chocolate.id - 1]
                    return f"The chocolate with {key} {target} was found with {student_name} (ID {chocolate.id})."
        return f"No chocolate with {key} {target} found."


    # Calling the function
    print()
    print(binary_search_chocolates(chocolates_sorted_by_weight, 5, "weight"))
    print(binary_search_chocolates(chocolates_sorted_by_price, 9, "price"))

