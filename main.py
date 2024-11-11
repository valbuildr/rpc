import discordrpc
import classes
from datetime import datetime

# main variables, edit these!

# required
app_id = 1305412549738631199  # integer | example: 1305412549738631199
act_type = (
    classes.ActivityType.competing
)  # integer, class made to make easier | example: classes.ActivityType.playing

# optional
state = None  # string | example: "Hellow!"
details = None  # string | example: "Hellow!"
ts_start = None  # integer, converted from datetime | example: datetime(1997, 11, 9, 17, 30, 00) | year, month, day, hour, minute, second
ts_end = None  # integer, converted from datetime | example: datetime(1997, 11, 9, 17, 30, 00) | year, month, day, hour, minute, second
large_image = None  # string | example: "Hellow!"
large_text = None  # string | example: "Hellow!"
small_image = None  # string | example: "Hellow!"
small_text = None  # string | example: "Hellow!"
buttons = None  # discordrpc.button.Button | example: discordrpc.button.Button("Hellow!!!!!", "https://google.com", "Hai!!!", "https://google.com") | button 1 label, button 1 url, button 2 label, button 2 url

# dont continue if you don't know what you're doing
# as for me i hav eno fucking clue what im doing! :3

rpc = discordrpc.RPC(app_id=app_id)


if ts_start:
    ts_start = ts_start.to_timestamp()

if ts_end:
    ts_end = ts_end.to_timestamp()


rpc.set_activity(
    state=state,
    details=details,
    act_type=act_type,
    ts_start=ts_start,
    ts_end=ts_end,
    large_image=large_image,
    large_text=large_text,
    small_image=small_image,
    small_text=small_text,
    buttons=buttons,
)

rpc.run()
