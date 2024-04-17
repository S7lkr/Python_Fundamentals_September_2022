text = input()

# encrypted_message = []
# for ch in text:
#     replaced_ch = chr(ord(ch)+3)
#     encrypted_message.append(ch.replace(ch, replaced_ch))

encrypted_message = [ch.replace(ch, chr(ord(ch)+3)) for ch in text]
print("".join(encrypted_message))