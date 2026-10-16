from pathlib import Path

file_path = Path("note.txt")
print(file_path)  # notes.txt

# Write text; replace existing contents
file_path.write_text("Learning Python for machine learning. updated \n this is new line", encoding="utf-8")

# Read the entire file as a string
content = file_path.read_text(encoding="utf-8")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content,"oiouij")
print(content)