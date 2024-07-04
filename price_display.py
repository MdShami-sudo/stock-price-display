import tkinter as tk
from tkinter import ttk
import random

def generate_stock_price():
    return round(random.uniform(100, 500), 2)

def update_prices():
    apple_price.set(f"Apple: ${generate_stock_price()}")
    google_price.set(f"Google: ${generate_stock_price()}")
    amazon_price.set(f"Amazon: ${generate_stock_price()}")
    facebook_price.set(f"Facebook: ${generate_stock_price()}")
    root.after(1000, update_prices)

root = tk.Tk()
root.title("Stock Price Display")
root.geometry("400x300")
root.configure(bg='#1c1c1c')  

style = ttk.Style()
style.configure("TLabel", background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 16, "bold"))

apple_price = tk.StringVar()
google_price = tk.StringVar()
amazon_price = tk.StringVar()
facebook_price = tk.StringVar()

apple_label = ttk.Label(root, textvariable=apple_price, style="TLabel")
apple_label.pack(pady=10)

google_label = ttk.Label(root, textvariable=google_price, style="TLabel")
google_label.pack(pady=10)

amazon_label = ttk.Label(root, textvariable=amazon_price, style="TLabel")
amazon_label.pack(pady=10)

facebook_label = ttk.Label(root, textvariable=facebook_price, style="TLabel")
facebook_label.pack(pady=10)

update_prices()

root.mainloop()
