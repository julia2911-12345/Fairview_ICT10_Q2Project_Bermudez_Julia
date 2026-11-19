

# Imports the document function to access HTML elements
from pyscript import document


# Stores the Grade 7 Dance Club members
Grade7_Members = {
    "DEANDRE FAIYAZ",
    "NATHANIA PARAYNO",
}


# Stores the Grade 8 Dance Club members
Grade8_Members = {
    "SAMANTHA BAUTISTA",
}


# Stores the Grade 9 Dance Club members
Grade9_Members = {
    "JILLIAN MAIA EUSEBIO",
    "CHELSI SIBAL",
    "CHLOE ADLAWAN",
    "ELISHA ANNE O. IGLOSO",
    "ALEYNAH CASSEDINE REDILLAS",
    "AMBRIEL GWENAELLE LEE",
    "VIKTOR PENA"
}


# Stores the Grade 10 Dance Club members
Grade10_Members = {
    "GEORGINA FLORENCE BANAL",
    "GEORGINA MANDY LAINE CAJANDING",
    "JULIA BERMUDEZ",
    "ERIN RIOFLORIDO",
    "MARC CATU",
    "DANIELLE SANDOVAL",
    "SABINE AGACITA",
}


# Stores the Grade 11 Dance Club members
Grade11_Members = {
    "AUDREY TAN",
    "ENZO JOSH MACARANAS",
    "FRANCESCA MEYER CRUZ",
}


# Combines all grade-level member sets into one set
All_Members = (
    Grade7_Members.union(Grade8_Members)
    .union(Grade9_Members)
    .union(Grade10_Members)
    .union(Grade11_Members)
)


# Function to display all registered members
def display_members():

    # Sorts the member names alphabetically and separates them with line breaks
    result = "<br>".join(sorted(All_Members))

    # Displays the complete member list on the webpage
    document.getElementById("result").innerHTML = result

    # Counts the members and displays the total number
    document.getElementById("total").innerHTML = (
        "Total Members: " + str(len(All_Members))
    )


# Function to add a new member to the list
def add_candidate(e):

    # Gets the first name entered in the input field
    first_name = document.getElementById(
        "first_name").value

    # Gets the last name entered in the input field
    last_name = document.getElementById(
        "last_name").value

    # Combines the names, removes extra spaces, and converts them to uppercase
    full_name = " ".join(
        (first_name + " " + last_name).split()
    ).upper()

    # Adds the new member's name to the combined member set
    All_Members.add(full_name)

    # Updates the webpage to show the new member list
    display_members()


# Displays the original member list when the page first loads
display_members()

