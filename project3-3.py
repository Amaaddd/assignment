import tkinter as tk
from tkinter import messagebox

class ElectionApp(tk.Tk):
    def __init__(self, candidate1, candidate2):
        super().__init__()
        self.title("Election")
        
        self.candidate1 = candidate1
        self.candidate2 = candidate2
        self.cand1_votes = 0
        self.cand2_votes = 0
        self.voters_id = [101, 102, 103, 104, 105, 106]
        self.voted = []

        self.create_widgets()

    def create_widgets(self):
        self.id_label = tk.Label(self, text="Enter your ID:")
        self.id_label.pack()

        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

        self.choice_label = tk.Label(self, text="Enter your choice:")
        self.choice_label.pack()

        self.choice_entry = tk.Entry(self)
        self.choice_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_vote)
        self.submit_button.pack()

    def submit_vote(self):
        try:
            voter = int(self.id_entry.get())

            if voter in self.voted:
                messagebox.showwarning("Invalid Vote", "You have already voted.")
            elif voter in self.voters_id:
                chosen_candidate = self.vote()

                if chosen_candidate:
                    if chosen_candidate == self.candidate1:
                        self.cand1_votes += 1
                        messagebox.showinfo("Vote Successful", f"You voted for {self.candidate1}.")
                    elif chosen_candidate == self.candidate2:
                        self.cand2_votes += 1
                        messagebox.showinfo("Vote Successful", f"You voted for {self.candidate2}.")
                    self.voters_id.remove(voter)
                    self.voted.append(voter)
                    self.id_entry.delete(0, tk.END)
                    self.choice_entry.delete(0, tk.END)
                else:
                    messagebox.showwarning("Invalid Vote", "Invalid choice. Skipping your vote.")
            else:
                messagebox.showwarning("Invalid Voter", "You are not allowed to vote. Sorry.")
        except ValueError:
            messagebox.showwarning("Invalid Voter", "Please enter a valid ID.")

        if not self.voters_id:
            self.print_results()

    def vote(self):
        try:
            choice = int(self.choice_entry.get())
            if choice == 1:
                return self.candidate1
            elif choice == 2:
                return self.candidate2
            else:
                return None
        except ValueError:
            return None

    def print_results(self):
        if self.cand1_votes > self.cand2_votes:
            winner = self.candidate1
            votes = self.cand1_votes
        elif self.cand2_votes > self.cand1_votes:
            winner = self.candidate2
            votes = self.cand2_votes
        else:
            winner = "None (Tie)"
            votes = self.cand1_votes
        
        messagebox.showinfo("Election Results", f"Voting is over.\n\n{self.candidate1}: {self.cand1_votes} votes\n{self.candidate2}: {self.cand2_votes} votes\n\nWinner: {winner} with {votes} votes")
        self.destroy()


# Main program
candidate1 = input("Enter the name of the 1st candidate: ")
candidate2 = input("Enter the name of the 2nd candidate: ")

app = ElectionApp(candidate1, candidate2)
app.mainloop()
