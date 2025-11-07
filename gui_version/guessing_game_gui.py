import tkinter as tk
from tkinter import messagebox
import random
import os

HIGHSCORE_FILE = "gui_version/highscore.txt"


def get_high_score():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return None
    return None


def save_high_score(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game  - GUI Version")
        self.root.geometry("450x500")
        self.root.config(bg="#f683db")

        self.number = random.randint(1, 100)
        self.tries = 0
        self.max_tries = 10
        self.high_score = get_high_score()

        # === MENU ===
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=game_menu)
        game_menu.add_command(label="🎮 Play", command=self.reset_game)
        game_menu.add_command(label="💡 Help", command=self.show_help)
        game_menu.add_separator()
        game_menu.add_command(label="🚪 Exit", command=self.root.quit)

        self.title_label = tk.Label(
            root,
            text="🎯 Number Guessing Game 🎯",
            font=("Arial", 18, "bold"),
            bg="#f683db",
            fg="#007acc"
        )
        self.title_label.pack(pady=15)

        self.info_label = tk.Label(
            root,
            text="I'm thinking of a number between 1 and 100.\nYou have 10 guesses.",
            font=("Arial", 12),
            bg="#f683db"
        )
        self.info_label.pack(pady=10)

        self.high_score_label = tk.Label(
            root,
            text=self.get_high_score_text(),
            font=("Arial", 11, "italic"),
            bg="#f683db",
            fg="#228B22"
        )
        self.high_score_label.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(
            root,
            text="Guess",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.check_guess
        )
        self.guess_button.pack(pady=5)

        self.feedback_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            bg="#f683db"
        )
        self.feedback_label.pack(pady=10)

        self.reset_button = tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 10, "bold"),
            bg="#e67e22",
            fg="white",
            command=self.reset_game
        )
        self.reset_button.pack(pady=5)

        self.remaining_label = tk.Label(
            root,
            text=f"Remaining tries: {self.max_tries}",
            font=("Arial", 11),
            bg="#f5f5f5"
        )
        self.remaining_label.pack(pady=5)

    def get_high_score_text(self):
        if self.high_score:
            return f"🏆 Current High Score: {self.high_score} guesses"
        return "No high score yet — be the first!"
    



    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        self.tries += 1
        remaining = self.max_tries - self.tries

        if guess < self.number:
            self.feedback_label.config(text="Too low! 📉", fg="orange")
        elif guess > self.number:
            self.feedback_label.config(text="Too high! 📈", fg="red")
        else:
            messagebox.showinfo(
                "Correct!",
                f"🎉 You guessed the number in {self.tries} tries!"
            )
            self.show_confetti()

            if self.high_score is None or self.tries < self.high_score:
                save_high_score(self.tries)
                self.high_score = self.tries
                messagebox.showinfo("🏆 New High Score!", "You set a new record!")

            self.root.after(2000, self.reset_game)
            return

        if remaining <= 0:
            messagebox.showerror("Out of Guesses", f"❌ You ran out of guesses! The number was {self.number}.")
            self.reset_game()
            return

        self.remaining_label.config(text=f"Remaining tries: {remaining}")
        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.tries = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.remaining_label.config(text=f"Remaining tries: {self.max_tries}")
        self.high_score_label.config(text=self.get_high_score_text())

    def show_help(self):
        messagebox.showinfo(
            "📘 HOW TO PLAY:\n\n"
            "The computer picks a number between 1 and 100.You have 10 guesses to find it.\n"
        )


#adding confetti feature
    def show_confetti(self):
        """Show confetti animation when player wins."""
        confetti_canvas = tk.Canvas(self.root, width=450, height=200, bg="#f5f5f5", highlightthickness=0)
        confetti_canvas.pack()

        confetti = []
        colors = ["#FF5733", "#33FF57", "#3357FF", "#FFD700", "#FF33A8", "#00FFFF"]

        # Create confetti pieces
        for _ in range(50):
            x = random.randint(0, 450)
            y = random.randint(0, 200)
            color = random.choice(colors)
            size = random.randint(5, 10)
            shape = confetti_canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
            confetti.append((shape, random.randint(-3, 3), random.randint(1, 5)))

        # Animate confetti falling
        def animate():
            for i, (shape, dx, dy) in enumerate(confetti):
                confetti_canvas.move(shape, dx, dy)
                pos = confetti_canvas.coords(shape)
                if pos[1] > 200:
                    confetti_canvas.move(shape, 0, -200)
            self.root.after(50, animate)

        animate()

        # Remove confetti after 2 seconds
        self.root.after(2000, confetti_canvas.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameGUI(root)
    root.mainloop()
