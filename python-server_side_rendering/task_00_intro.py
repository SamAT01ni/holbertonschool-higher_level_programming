#!/usr/bin/python3
"""
Generate personalised invite files from a template
Error handling
"""


def generate_invitations(template, attendees):
    """Check input types"""
    if not isinstance(template, str):
        print("Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        return
    
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print (f"{attendee} must be a dictionary")
            return

    """"Handle empty imputs"""
    if template == "":
        print ('Template is empty, no output files generated.')
        return
    if len(attendees) <= 0:
        print('No data provided, no output files generated.')
        return
    
    """"Change placeholders with attendee data"""
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i in range(len(attendees)):
        invite = template
        attendee = attendees[i]

        for data in placeholders:
            value = attendee.get(data)
            if value is None:
                value = "N/A"
            invite = invite.replace("{" + data + "}", str(value))
        
        filename = f'output_{i + 1}.txt'
        try:
            with open(filename, "w") as file:
                file.write(invite)
        except Exception:
            print(f"Error writing {filename}: {Exception}")