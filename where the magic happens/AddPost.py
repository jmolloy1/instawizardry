from appJar import gui
import AddRow

app = gui()

app.addLabel("title", "what up?")
app.setLabelBg("title", "red")

app.addLabelEntry("File Path")
app.addLabelEntry("Caption")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        file = app.getEntry("File Path")
        caption = app.getEntry("Caption")
        user = app.getEntry("Username")
        password = app.getEntry("Password")

        row = user + "," + password + "," + file + "," + caption

        AddRow.AddRow(row)


app.addButtons(["Go!","Cancel"],press)












app.go()
