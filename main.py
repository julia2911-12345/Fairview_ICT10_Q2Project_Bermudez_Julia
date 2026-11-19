
# Imports the document function to access HTML elements
from pyscript import document


# List of students who are official Dance Club members
club_members = [
    "AUDREY TAN",
    "CHELSI SIBAL",
    "CHLOE ADLAWAN",
    "DANIELLE SANDOVAL",
    "DEANDRE FAIYAZ",
    "ELISHA ANNE O. IGLOSO",
    "ENZO JOSH MACARANAS",
    "FRANCESCA MEYER CRUZ",
    "GEORGINA FLORENCE BANAL",
    "GEORGINA MANDY LAINE CAJANDING",
    "JILLIAN MAIA EUSEBIO",
    "MARC CATU",
    "NATHANIA PARAYNO",
    "SABINE AGACITA",
    "SAMANTHA BAUTISTA",
    "VIKTOR PENA",
    "ERIN RIOFLORIDO",
    "JULIA BERMUDEZ",
    "ALEYNAH CASSEDINE REDILLAS",
    "AMBRIEL GWENAELLE LEE"
]


# Function that checks if the entered candidate is a member
def check_candidate(e):

    # Gets the first name entered by the user
    first_name = document.getElementById(
        "first_name").value

    # Gets the last name entered by the user
    last_name = document.getElementById(
        "last_name").value

    # Combines both names, removes extra spaces, and converts them to uppercase
    full_name = " ".join((first_name + " " + last_name).split()).upper()

    # Checks if the full name exists in the club members list
    is_member = full_name in club_members

    # Stores the possible messages for members and non-members
    messages = [
        "Sorry " + full_name.title() +
        ", your name is not on the list.",

        "Congratulations " + full_name.title() +
        "! You are now part of the Dance Club!"
    ]

    # Selects the correct message based on the membership result
    result = messages[is_member]

    # Displays the final message on the webpage
    document.getElementById("result").innerHTML = result

