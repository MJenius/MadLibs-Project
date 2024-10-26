import tkinter as tk
from tkinter import messagebox

class StoryGeneratorGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Mad Libs Generator")
        self.choice_var = tk.IntVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Choose a Story Template:").pack()
        choices = [("Unexpected Vacation Adventure", 1), ("The Silly Adventure", 2), ("Professor's Misadventures", 3),
                   ("Superhero's Day Out", 4), ("Great Baking Disaster", 5)]
        for text, choice_value in choices:
            tk.Radiobutton(self.master, text=text, variable=self.choice_var, value=choice_value).pack()
        tk.Button(self.master, text="Generate Story", command=self.generate_story).pack()
        self.continue_button = tk.Button(self.master, text="End", command=self.continue_story)
        self.continue_button.pack()

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
                story_text = tk.Text(story_window, wrap=tk.WORD)
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
            2: [("Enter an adjective for activities: ", "adjective1"),
                ("Enter a noun that goes on the adventure: ", "noun1"),
                ("Enter an adjective for an adventure: ", "adjective2"), ("Enter an animal: ", "animal"),
                ("Enter a snack: ", "noun2"), ("Enter a colour: ", "colour"),
                ("Enter an adjective for flowers: ", "adjective3"), ("Enter an adjective for joy: ", "adjective4")],
            3: [("Enter a name for the Professor: ", "name"), ("Enter a job: ", "job"),
                ("Enter an invention: ", "noun1"), ("Enter an adjective for the invention: ", "adjective1"),
                ("Enter an object: ", "noun2"), ("Enter an adjective for the object: ", "adjective2"),
                ("Enter its colour: ", "colour"), ("Enter another object: ", "noun3")],
            4: [("Enter the name of a superhero: ", "name1"),
                ("Enter an adjective for the superhero: ", "adjective1"),
                ("Enter a verb for his power: ", "verb1"), ("Enter a noun the hero saves: ", "noun1"),
                ("Enter the name of the supervillain: ", "name2"), ("Enter an adjective for moves: ", "adjective2"),
                ("Enter an object: ", "noun2"), ("Enter a verb the hero does: ", "verb2"),
                ("Enter an adjective for a situation: ", "adjective3")],
            5: [("Enter an adjective for a kitchen: ", "adjective1"), ("Enter a name: ", "name"),
                ("Enter a food that is a flavour: ", "noun1"), ("Enter an adjective for a cake: ", "adjective2"),
                ("Enter a holiday: ", "holiday"), ("Enter an adjective affecting the ingredients: ", "verb1"),
                ("Enter an unnecessary ingredient: ", "noun2"), ("Enter an adjective for laughter: ", "adjective3"),
                ("Enter a colour: ", "colour"), ("Enter a bad-tasting item: ", "noun3"),
                ("Enter an adjective for a memory: ", "adjective4")]
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
        self.results = {}
        
        for prompt, var_name in prompts:
            tk.Label(self.top, text=prompt).pack()
            entry = tk.Entry(self.top)
            entry.pack()
            self.results[var_name] = entry
        tk.Button(self.top, text="OK", command=self.ok).pack()

    def ok(self):
        for var_name, entry in self.results.items():
            self.results[var_name] = entry.get()
        self.top.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGeneratorGUI(root)
    root.mainloop()
