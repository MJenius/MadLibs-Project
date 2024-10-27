A GUI-based Mad Libs story generator built with Python and Tkinter! This project lets users choose from multiple story templates and provides prompts to fill in the blanks for a fun, interactive storytelling experience.

Features
Multiple Story Templates: Choose from different templates, each offering a unique story format.
Interactive Input Form: Custom prompts guide users to fill in words for their story.
Story Preview: Displays the completed story in a new window.
Decorated GUI: Enhanced with colors, custom fonts, and a clean layout for an improved user experience.

Installation

1. Clone the repository:
    git clone https://github.com/your-username/mad-libs-generator.git
    cd mad-libs-generator

2. Install dependencies:
     python -m tkinter

3. Run the application:
     python madlibs_final_beautified.py

File Structure
mad_libs_generator.py: Main application file containing GUI logic and story generation.
storyX.txt: Text files with placeholders for each story template. Create files like story1.txt, story2.txt, etc., with placeholders like {name}, {place}, {adjective}, etc., to allow the program to replace them with user inputs.

Customization
To add more templates:

Create a new .txt file (e.g., story6.txt) and add placeholders.
Update the input_prompts dictionary in mad_libs_generator.py to include prompts for the new template.
Add the new template to the list in create_widgets function.


Most Importantly, Just have fun!


_______________________________________________________________________________
License
This project is open-source and available under the MIT License.

_______________________________________________________________________________

