censor = "CAMBRIDGE"

msg = input()
for c in censor:
    msg = msg.replace(c, "")
print(msg)