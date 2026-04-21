import tkinter as tk
from tkinter import messagebox, filedialog
import datetime, os, json

# PDF LIBRARY
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ---------------- MENU ----------------
menu = {
    "Maharaja Thali": 550,
    "Deluxe Thali": 450,
    "Paneer Butter Masala": 300,
    "Dal Tadka": 180,
    "Jeera Rice": 150,
    "Butter Naan": 40,
    "Lassi": 80
}

# ---------------- COLORS ----------------
BG = "#f5f1ee"
PRIMARY = "#7b1113"
HOVER = "#a52a2a"
CARD = "#ffffff"

# ---------------- APP ----------------
class RajdhaniPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Rajdhani Restaurant POS")
        self.root.geometry("1100x700")
        self.root.configure(bg=BG)

        self.cart = []

        self.layout()

    # ---------------- LAYOUT ----------------
    def layout(self):
        sidebar = tk.Frame(self.root, bg=PRIMARY, width=180)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="RAJDHANI",
                 bg=PRIMARY, fg="white",
                 font=("Georgia", 18, "bold")).pack(pady=20)

        self.nav(sidebar, "Home", self.home)
        self.nav(sidebar, "Booking", self.booking)
        self.nav(sidebar, "Billing", self.billing)

        self.main = tk.Frame(self.root, bg=BG)
        self.main.pack(fill="both", expand=True)

        self.home()

    def nav(self, parent, text, cmd):
        b = tk.Label(parent, text=text,
                     bg=PRIMARY, fg="white",
                     font=("Arial", 12, "bold"),
                     pady=10)
        b.pack(fill="x", padx=10, pady=5)

        b.bind("<Button-1>", lambda e: cmd())
        b.bind("<Enter>", lambda e: b.config(bg=HOVER))
        b.bind("<Leave>", lambda e: b.config(bg=PRIMARY))

    def clear(self):
        for w in self.main.winfo_children():
            w.destroy()

    # ---------------- HOME ----------------
    def home(self):
        self.clear()

        hero = tk.Frame(self.main, bg=PRIMARY, height=160)
        hero.pack(fill="x", padx=20, pady=20)

        tk.Label(hero, text="A Royal Feast Awaits",
                 fg="white", bg=PRIMARY,
                 font=("Georgia", 26, "bold")).pack(pady=40)

        cards = tk.Frame(self.main, bg=BG)
        cards.pack()

        self.card(cards, "🍽️ Special", "Maharaja Thali Experience")
        self.card(cards, "🎁 Rewards", "Earn loyalty points")

    def card(self, parent, title, desc):
        f = tk.Frame(parent, bg=CARD, width=300, height=150)
        f.pack(side="left", padx=15)
        f.pack_propagate(False)

        tk.Label(f, text=title, bg=CARD,
                 fg=PRIMARY, font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(f, text=desc, bg=CARD,
                 wraplength=250).pack()

        f.bind("<Enter>", lambda e: f.config(bg="#f9f3e8"))
        f.bind("<Leave>", lambda e: f.config(bg=CARD))

    # ---------------- BOOKING ----------------
    def booking(self):
        self.clear()

        box = tk.Frame(self.main, bg=CARD, padx=20, pady=20)
        box.pack(pady=40)

        tk.Label(box, text="Book Table",
                 font=("Georgia", 20, "bold"),
                 bg=CARD, fg=PRIMARY).pack(pady=10)

        self.name = self.entry(box, "Customer Name")
        self.guests = self.entry(box, "Guests")
        self.table = self.entry(box, "Table No")

        tk.Button(box, text="Confirm Booking",
                  bg=PRIMARY, fg="white",
                  command=self.save_booking).pack(pady=10)

    def entry(self, p, label):
        tk.Label(p, text=label, bg=CARD).pack()
        e = tk.Entry(p, font=("Arial", 12))
        e.pack(pady=5)
        return e

    def save_booking(self):
        messagebox.showinfo("Success", "Table Booked!")

    # ---------------- BILLING ----------------
    def billing(self):
        self.clear()
        self.cart = []

        frame = tk.Frame(self.main, bg=BG)
        frame.pack(fill="both", expand=True)

        # LEFT
        left = tk.Frame(frame, bg=CARD, padx=10, pady=10)
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        tk.Label(left, text="Menu",
                 font=("Arial", 16, "bold"),
                 bg=CARD).pack()

        self.menu_box = tk.Listbox(left, font=("Arial", 12))
        self.menu_box.pack(fill="both", expand=True)

        for i, p in menu.items():
            self.menu_box.insert(tk.END, f"{i} - ₹{p}")

        tk.Button(left, text="Add Item",
                  bg=PRIMARY, fg="white",
                  command=self.add_item).pack(pady=5)

        tk.Label(left, text="Cart",
                 font=("Arial", 12, "bold"),
                 bg=CARD).pack()

        self.cart_box = tk.Listbox(left)
        self.cart_box.pack(fill="both", expand=True)

        # RIGHT
        right = tk.Frame(frame, bg=CARD, padx=10, pady=10)
        right.pack(side="left", fill="both", expand=True)

        tk.Label(right, text="Bill",
                 font=("Arial", 16, "bold"),
                 bg=CARD).pack()

        self.bill = tk.Text(right, height=20)
        self.bill.pack(fill="both", expand=True)

        tk.Button(right, text="Generate Bill",
                  bg=PRIMARY, fg="white",
                  command=self.generate_bill).pack(pady=5)

        tk.Button(right, text="Save PDF",
                  bg="green", fg="white",
                  command=self.print_pdf).pack(pady=5)

        tk.Button(right, text="Load Bill",
                  bg="#444", fg="white",
                  command=self.load_bill).pack(pady=5)

    # ---------------- LOGIC ----------------
    def add_item(self):
        sel = self.menu_box.curselection()
        if not sel:
            return

        item = self.menu_box.get(sel[0])
        self.cart.append(item)
        self.cart_box.insert(tk.END, item)

    def generate_bill(self):
        self.bill.delete("1.0", tk.END)

        total = 0
        text = "RAJDHANI RESTAURANT\n\n"

        for i in self.cart:
            n, p = i.split(" - ₹")
            total += int(p)
            text += f"{n} - ₹{p}\n"

        text += f"\nTOTAL: ₹{total}"
        self.bill.insert(tk.END, text)

    # ---------------- PDF ----------------
    def print_pdf(self):
        file = filedialog.asksaveasfilename(defaultextension=".pdf")
        if not file:
            return

        c = canvas.Canvas(file, pagesize=letter)
        w, h = letter
        y = h - 50

        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(w/2, y, "RAJDHANI RESTAURANT")

        y -= 40
        c.setFont("Helvetica", 11)

        total = 0

        for i in self.cart:
            n, p = i.split(" - ₹")
            p = int(p)
            total += p

            c.drawString(50, y, n)
            c.drawRightString(w-50, y, f"₹{p}")
            y -= 20

        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawRightString(w-50, y, f"TOTAL: ₹{total}")

        c.save()
        os.startfile(file)

    # ---------------- LOAD ----------------
    def load_bill(self):
        file = filedialog.askopenfilename(filetypes=[("JSON", "*.txt")])
        if not file:
            return

        with open(file, "r") as f:
            data = json.load(f)

        self.bill.delete("1.0", tk.END)
        self.bill.insert(tk.END, str(data))


# ---------------- RUN ----------------
root = tk.Tk()
app = RajdhaniPOS(root)
root.mainloop()