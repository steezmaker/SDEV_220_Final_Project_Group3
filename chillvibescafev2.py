import tkinter as tk
from tkinter import messagebox, PhotoImage
class ChillVibesCafeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Chill Vibes Cafe")
        self.root.configure(bg="#4F200D")

        self.root.iconbitmap("coffee-icon.ico")

        
        self.image = PhotoImage(file = "chill-vibes-cafe.png")
        

        self.menu_frame = tk.Frame(self.root, bg="#4F200D")
        self.menu_frame.pack(pady=10)
        
        self.drink_label = tk.Label(self.menu_frame, text="Select Drink:", bg="#171010", fg="#EEEEEE")
        self.drink_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.drink_var = tk.StringVar()
        self.drink_var.set("Coffee")
        self.drink_options = ["Coffee", "Latte", "Cappuccino", "Macchiato"]
        self.drink_dropdown = tk.OptionMenu(self.menu_frame, self.drink_var, *self.drink_options)
        self.drink_dropdown.grid(row=0, column=1, padx=10, pady=5)
        
        self.size_label = tk.Label(self.menu_frame, text="Select Size:", bg="#171010", fg="#EEEEEE")
        self.size_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.size_var = tk.StringVar()
        self.size_var.set("Small")
        self.size_options = ["Small", "Medium", "Large"]
        self.size_dropdown = tk.OptionMenu(self.menu_frame, self.size_var, *self.size_options)
        self.size_dropdown.grid(row=1, column=1, padx=10, pady=5)
        
        self.ice_label = tk.Label(self.menu_frame, text="Select Ice Level:", bg="#171010", fg="#EEEEEE")
        self.ice_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.ice_var = tk.StringVar()
        self.ice_var.set("Regular")
        self.ice_options = ["No Ice", "Light Ice", "Regular Ice", "Heavy Ice"]
        self.ice_dropdown = tk.OptionMenu(self.menu_frame, self.ice_var, *self.ice_options)
        self.ice_dropdown.grid(row=2, column=1, padx=10, pady=5)
        
        self.sugar_label = tk.Label(self.menu_frame, text="Add Sugar Level:", bg="#171010", fg="#EEEEEE")
        self.sugar_label.grid(row=3, column=0, padx=10, pady=5)
        
        self.sugar_slider = tk.Scale(self.menu_frame, from_=0, to=10, orient=tk.HORIZONTAL, bg="#171010", fg="#EEEEEE")
        self.sugar_slider.grid(row=3, column=1, padx=10, pady=5)
        
        self.cream_label = tk.Label(self.menu_frame, text="Add Cream Level:", bg="#171010", fg="#EEEEEE")
        self.cream_label.grid(row=4, column=0, padx=10, pady=5)
        
        self.cream_slider = tk.Scale(self.menu_frame, from_=0, to=10, orient=tk.HORIZONTAL, bg="#171010", fg="#EEEEEE")
        self.cream_slider.grid(row=4, column=1, padx=10, pady=5)
        
        self.flavor_label = tk.Label(self.menu_frame, text="Select Flavor:", bg="#171010", fg="#EEEEEE")
        self.flavor_label.grid(row=5, column=0, padx=10, pady=5)
        
        self.flavor_var = tk.StringVar()
        self.flavor_var.set("Vanilla")
        self.flavor_options = ["Vanilla", "Hazelnut", "Maple", "Peppermint", "Cinnamon"]
        self.flavor_dropdown = tk.OptionMenu(self.menu_frame, self.flavor_var, *self.flavor_options)
        self.flavor_dropdown.grid(row=5, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self.menu_frame, text="Add to Order", command=self.add_to_order)
        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.receipt_frame = tk.Frame(self.root, bg="#4F200D")
        self.receipt_frame.pack(pady=10)
        
        self.receipt_label = tk.Label(self.receipt_frame, text="Receipt:", bg="#4F200D", fg="#EEEEEE")
        self.receipt_label.pack()
        
        self.receipt_text = tk.Text(self.receipt_frame, height=10, width=50, bg="#D1D1D1", fg="#171010")
        self.receipt_text.pack()
        
        self.total_price = 0
        
        self.finish_button = tk.Button(self.root, text="Finish Order", command=self.finish_order)
        self.finish_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset Order", command=self.reset_order)
        self.reset_button.pack()
    
    def add_to_order(self):
        drink = self.drink_var.get()
        size = self.size_var.get()
        ice = self.ice_var.get()
        sugar = self.sugar_slider.get()
        cream = self.cream_slider.get()
        flavor = self.flavor_var.get()
        
        price = self.calculate_price(drink, size)
        self.total_price += price
        
        receipt_info = f"{size} {flavor} {drink} with {ice}, Sugar level: {sugar}, Cream level: {cream}, Price: ${price:.2f}\n"
        self.receipt_text.insert(tk.END, receipt_info)
    
    def calculate_price(self, drink, size):
        prices = {
            "Coffee": {"Small": 2.55, "Medium": 2.89, "Large": 3.09},
            "Latte": {"Small": 4.19, "Medium": 4.69, "Large": 5.29},
            "Cappuccino": {"Small": 4.19, "Medium": 4.69, "Large": 5.29},
            "Macchiato": {"Small": 2.89, "Medium": 3.39, "Large": 3.89}
        }
        return prices[drink][size]
    
    def finish_order(self):
        total_with_tax = self.total_price * 1.05
        messagebox.showinfo("Here's your full order", f"{self.receipt_text.get(1.0, tk.END)}\nTotal before tax: ${self.total_price:.2f}\nTotal after 5% sales tax: ${total_with_tax:.2f}\n\nThanks for shopping at The Chill Vibes Cafe")
    def reset_order(self):
        self.receipt_text.delete(1.0, tk.END)
        self.total_price = 0
        messagebox.showinfo("Order Cleared", "Your Order is Cleared Successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChillVibesCafeApp(root)
    root.mainloop()
