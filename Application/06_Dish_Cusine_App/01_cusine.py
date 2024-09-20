### This is a Dish-Cusine Application

# Creating a list of dishes categorized by cuisine type: Indian, Italian, Chinese, and American.
Indian = ["Butter Chicken", "Paneer Tikka", "Biryani", "Samosa", "Dal Makhani", "Chole Bhature",
        "Rogan Josh", "Masala Dosa", "Tandoori Chicken", "Palak Paneer"]

Italian = ["Lasagna", "Spaghetti Carbonara", "Margherita Pizza", "Risotto", "Tiramisu", 
        "Fettuccine Alfredo", "Bruschetta", "Pesto Pasta", "Caprese Salad", "Ravioli"]

Chinese = ["Kung Pao Chicken", "Sweet and Sour Pork", "Spring Rolls", "Fried Rice", "Dumplings", 
        "Peking Duck", "Chow Mein", "Hot and Sour Soup", "Szechuan Beef", "Wonton Soup"]
    
American = ["Hamburger", "Mac and Cheese", "Barbecue Ribs", "Buffalo Wings", "Fried Chicken", 
        "Clam Chowder", "Apple Pie", "Cornbread", "Hot Dogs", "Philly Cheesesteak"]


dish = input("Enter a dish name  ")

if dish in Indian:
    print(f"{dish} is available in the Indian Cusine")
elif dish in Italian:
    print(f"{dish} is available in the Italian Cusine")
elif dish in Chinese:
    print(f"{dish} is available in the Chinese Cusine")
elif dish in American:
    print(f"{dish} is available in the American Cusine")
else:
    print(f"Based on my knowledge, I can't find {dish} in any available Cusine")