from pyscript import display, document 

def teamRegistry (e):
    document.getElementById('output').innerHTML = ""

    section = document.getElementById('sectionSelector').value
    gradelevel = document.getElementById('gradelevelSelector').value

    answer = document.querySelector('input[name="onlineRegistry_check"]:checked]').value
    status_clear = document.querySelector('input[name="permissionApproved"]:checked]').value
    status_unclear = document.querySelector('input[name="permissionDenied"]:checked]').value

    if section == "EM10E" and gradelevel == "ten":
        display("Yellow Tigers Upper Division", target ='output')
        document.getElementById('output').innerHTML += "<img src='tiger.png' alt='Tiger'>"
    elif section == "EM10E" and gradelevel == "nine":
        display("Yellow Tigers Lower Division", target ='output')
        document.getElementById('output').innerHTML += "<img src='tiger.png' alt='Tiger'>"
    elif section == "EM10E" and gradelevel == "eight":
        display("Yellow Tigers Lower Division", target ='output')
        document.getElementById('output').innerHTML += "<img src='tiger.png' alt='Tiger'>"
    elif section == "EM10E" and gradelevel == "seven":
        display("Yellow Tigers Lower Division", target ='output')
        document.getElementById('output').innerHTML += "<img src='tiger.png' alt='Tiger'>"
    elif section == "RM10R" and gradelevel == "ten":
        display("Blue Bear Upper Division.", target ='output')
        document.getElementById('output').innerHTML += "<img src='bear.png' alt='Bear'>"
    elif section == "RM10R Lower Division" and gradelevel == "nine":
        display("Blue Bear Lower Division.", target ='output')
        document.getElementById('output').innerHTML += "<img src='bear.png' alt='Bear'>"
    elif section == "RM10R" and gradelevel == "eight":
        display("Blue Bears Lower Division.", target ='output')
        document.getElementById('output').innerHTML += "<img src='bear.png' alt='Bear'>"
    elif section == "RM10R" and gradelevel == "seven":
        display("Blue Bears Lower Division.", target ='output')
        document.getElementById('output').innerHTML += "<img src='bear.png' alt='Bear'>"
    elif section == "SP10S" and gradelevel == "ten":
        display("Green Hornets", target ='output')
        document.getElementById('output').innerHTML += "<img src='greenhornet.png' alt='Hornet'>"
    elif section == "TP10T" and gradelevel == "ten":
        display("The other team i forgot", target ='output')
        document.getElementById('output').innerHTML += "<img src='greenhornet.png' alt='Hornet'>"

    if answer == "yes":
        display(" You have registered for the team.", target ='output')
    elif answer == "no":
        display(" You have not registered for the team.", target ='output')

    if status_clear == "studentCleared":
        display("Fit", target ='output')
    elif status_unclear == "student_NotCleared":
        display("Unfit", target ='output')

    else:
        display("Not OB student.", target ='output')

