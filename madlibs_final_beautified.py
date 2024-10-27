import tkinter as tk
from tkinter import messagebox, font

class StoryGeneratorGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Mad Libs Generator")
        self.master.geometry("400x400")
        self.master.configure(bg="#dfe6e9")
        self.choice_var = tk.IntVar()
        
        # Set custom fonts
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        
        # Create widgets with additional styling
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Choose a Story Template:", font=self.title_font, bg="#dfe6e9")
        title_label.pack(pady=10)
        
        choices_frame = tk.Frame(self.master, bg="#dfe6e9")
        choices = [("Unexpected Vacation Adventure", 1), ("The Silly Adventure", 2), ("Professor's Misadventures", 3),
                   ("Superhero's Day Out", 4), ("Great Baking Disaster", 5)]
        
        for text, choice_value in choices:
            tk.Radiobutton(
                choices_frame, text=text, variable=self.choice_var, value=choice_value, font=("Arial", 10),
                bg="#dfe6e9", fg="#2d3436", activebackground="#b2bec3"
            ).pack(anchor="w", padx=10, pady=2)
        choices_frame.pack(pady=10)

        button_frame = tk.Frame(self.master, bg="#dfe6e9")
        tk.Button(button_frame, text="Generate Story", command=self.generate_story, font=self.button_font,
                  bg="#74b9ff", fg="white", activebackground="#0984e3").pack(side="left", padx=10)
        
        self.continue_button = tk.Button(button_frame, text="End", command=self.continue_story, font=self.button_font,
                                         bg="#d63031", fg="white", activebackground="#e17055", state=tk.DISABLED)
        self.continue_button.pack(side="left", padx=10)
        
        button_frame.pack(pady=10)

    def generate_story(self):
        choice = self.choice_var.get()
        if choice:
            story_file = f"story{choice}.txt"
            try:
                with open(story_file, "r") as storyfile:
                    story_template = storyfile.read()
                inputs = self.get_user_inputs()
                story_window = tk.Toplevel(self.master)
                story_window.title("Generated Story")
                story_text = tk.Text(story_window, wrap=tk.WORD, font=("Arial", 12), bg="#ffeaa7", fg="#2d3436")
                story_text.insert(tk.END, story_template.format(**inputs))
                story_text.pack(expand=True, fill=tk.BOTH)
                self.continue_button.config(state=tk.NORMAL)
            except FileNotFoundError:
                messagebox.showerror("Error", "Story template file not found.")
        else:
            messagebox.showerror("Error", "Please choose a story template.")

    def get_user_inputs(self):
        input_dict = {}
        input_prompts = {
            1: [("Enter a Name: ", "name1"), ("Enter another Name: ", "name2"),
                ("Enter an adjective for a vacation: ", "adjective1"), ("Enter a place: ", "place"),
                ("Enter an adjective for an adventure: ", "adjective2"), ("Enter an animal: ", "animal"),
                ("Enter an adjective about the animal: ", "adjective3"), ("Enter an object: ", "noun2"),
                ("Enter an adjective for surprises: ", "adjective4")],
            # Add other templates here as needed
        }
        input_prompts_for_choice = input_prompts.get(self.choice_var.get(), [])
        form_dialog = FormDialog(self.master, input_prompts_for_choice)
        self.master.wait_window(form_dialog.top)
        input_dict = form_dialog.results
        return input_dict

    def continue_story(self):
        self.choice_var.set(0)
        self.continue_button.config(state=tk.DISABLED)
        self.master.destroy()

class FormDialog:

    def __init__(self, parent, prompts):
        self.top = tk.Toplevel(parent)
        self.top.title("Input Form")
        self.top.configure(bg="#ffeaa7")
        self.results = {}
        
        for prompt, var_name in prompts:
            tk.Label(self.top, text=prompt, bg="#ffeaa7", fg="#2d3436").pack(pady=5)
            entry = tk.Entry(self.top)
            entry.pack(pady=5)
            self.results[var_name] = entry
        tk.Button(self.top, text="OK", command=self.ok, bg="#55efc4", fg="white", activebackground="#00b894").pack(pady=10)

    def ok(self):
        for var_name, entry in self.results.items():
            self.results[var_name] = entry.get()
        self.top.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGeneratorGUI(root)
    root.mainloop()
