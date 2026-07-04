TOOLS = """
Available tools:

browser.open

browser.search

app.open

file.search

project.resume

system.shutdown

system.restart

spotify.play

youtube.play

email.send

calendar.create

terminal.run

Return ONLY JSON.

Example:

{
    "steps":[
        {
            "tool":"browser",
            "action":"open",
            "target":"https://youtube.com"
        }
    ]
}
"""