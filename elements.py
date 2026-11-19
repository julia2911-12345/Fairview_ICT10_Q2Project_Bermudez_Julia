from pyscript import document


# Stores the non-metal elements and their corresponding properties
# Each element contains its name, atomic number, and atomic mass
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}


# Function that searches for a non-metal element
def find_nonmetal(e):

    # Clears the previous search result
    document.getElementById("show").innerHTML = ""

    # Gets the entered symbol, removes extra spaces, and capitalizes it correctly
    elements = document.getElementById(
        "Symbol").value.strip().capitalize()

    # Searches the dictionary for the element's properties
    # Displays a default message if the symbol is not found
    result = nonmetals.get(
        elements, ("Element not found", "-", "-"))

    # Organizes the element information into HTML format
    output_html = f"""
    <b>Symbol:</b> {elements} <br>
    <b>Element Name:</b> {result[0]} <br>
    <b>Atomic Number:</b> {result[1]} <br>
    <b>Atomic Mass:</b> {result[2]} <br>
    """

    # Displays the element information on the webpage
    document.getElementById("show").innerHTML = output_html
