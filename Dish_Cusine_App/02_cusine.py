# Creating a list of dishes categorized by cuisine type: Indian, Italian, Chinese, and American.
cuisines = {
    "Indian": ["Butter Chicken", "Paneer Tikka", "Biryani", "Samosa", "Dal Makhani", "Chole Bhature",
               "Rogan Josh", "Masala Dosa", "Tandoori Chicken", "Palak Paneer"],
    "Italian": ["Lasagna", "Spaghetti Carbonara", "Margherita Pizza", "Risotto", "Tiramisu", 
                "Fettuccine Alfredo", "Bruschetta", "Pesto Pasta", "Caprese Salad", "Ravioli"],
    "Chinese": ["Kung Pao Chicken", "Sweet and Sour Pork", "Spring Rolls", "Fried Rice", "Dumplings", 
                "Peking Duck", "Chow Mein", "Hot and Sour Soup", "Szechuan Beef", "Wonton Soup"],
    "American": ["Hamburger", "Mac and Cheese", "Barbecue Ribs", "Buffalo Wings", "Fried Chicken", 
                 "Clam Chowder", "Apple Pie", "Cornbread", "Hot Dogs", "Philly Cheesesteak"]
}

dish = input("Enter a dish name: ")

# Loop through the cuisines to find the dish
found = False
for cuisine, dishes in cuisines.items():
    if dish in dishes:
        print(f"{dish} is available in the {cuisine} cuisine.")
        found = True
        break

if not found:
    print(f"Based on my knowledge, I can't find {dish} in any available cuisine.")
