import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class TicTacToeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.geometry("400x500")
        self.resizable(False, False)
        self.mode = ctk.StringVar(value="2 Player")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(self, text="Tic-Tac-Toe", font=("Arial", 28, "bold"))
        title.pack(pady=10)

        mode_frame = ctk.CTkFrame(self)
        mode_frame.pack(pady=5)
        ctk.CTkLabel(mode_frame, text="Mode:").pack(side="left", padx=5)
        ctk.CTkOptionMenu(mode_frame, variable=self.mode, values=["1 Player", "2 Player"], command=self.reset_game).pack(side="left")

        board_frame = ctk.CTkFrame(self)
        board_frame.pack(pady=20)
        for i in range(9):
            btn = ctk.CTkButton(board_frame, text="", width=80, height=80, font=("Arial", 24), command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        self.status_label = ctk.CTkLabel(self, text="Player X's turn", font=("Arial", 18))
        self.status_label.pack(pady=10)

        reset_btn = ctk.CTkButton(self, text="Reset", command=self.reset_game)
        reset_btn.pack(pady=5)

    def on_click(self, idx):
        if self.board[idx] or self.check_winner():
            return
        self.board[idx] = self.current_player
        self.buttons[idx].configure(text=self.current_player)
        winner = self.check_winner()
        if winner:
            self.status_label.configure(text=f"Player {winner} wins!")
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        elif "" not in self.board:
            self.status_label.configure(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            self.switch_player()
            if self.mode.get() == "1 Player" and self.current_player == "O":
                self.after(500, self.computer_move)

    def computer_move(self):
        available = [i for i, v in enumerate(self.board) if v == ""]
        if available:
            idx = random.choice(available)
            self.on_click(idx)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.configure(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for a,b,c in wins:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def reset_game(self, *args):
        self.board = ["" for _ in range(9)]
        for btn in self.buttons:
            btn.configure(text="")
        self.current_player = "X"
        self.status_label.configure(text="Player X's turn")

if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop() 