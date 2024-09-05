def on_on_chat():
    player.say(":)")
    player.teleport(pos(0, 0, 0))
player.on_chat("run", on_on_chat)
