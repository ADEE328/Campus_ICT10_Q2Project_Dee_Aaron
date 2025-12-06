from js import document

# FROM SKILLS TEST
clubs = {
    "Basketball": {
        "Name": "Basketball Club",
        "Description": "A club for students who enjoy basketball and team competition.",
        "Meeting time": "Mondays 2:00–5:00 PM",
        "Location": "Basketball Court",
        "Club Moderator": "Aaron Dee",
        "Members": "25"
    },
    "Volleyball": {
        "Name": "Volleyball Club",
        "Description": "A fun club focused on volleyball skills and teamwork.",
        "Meeting time": "Wednesdays 3:30–5:30 PM",
        "Location": "Gym",
        "Club Moderator": "Coach James",
        "Members": "18"
    },
    "Tennis": {
        "Name": "Tennis Club",
        "Description": "A club for tennis lovers of all skill levels.",
        "Meeting time": "Fridays 1:00–3:00 PM",
        "Location": "Tennis Courts",
        "Club Moderator": "Coach Dee",
        "Members": "14"
    }
}

def show_info(event=None):
    sel = document.getElementById("club_select").value
    out = document.getElementById("output")

    if sel == "":
        out.innerText = "Please select a club first."
        return

    info = clubs[sel]


    text = f"{info['Name']}\n\n"
    text += f"Description: {info['Description']}\n"
    text += f"Meeting Time: {info['Meeting time']}\n"
    text += f"Location: {info['Location']}\n"
    text += f"Club Moderator: {info['Club Moderator']}\n"
    text += f"Members: {info['Members']}\n"

    out.innerText = text

document.getElementById("show_btn").onclick = show_info
