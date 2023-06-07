text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
# print(pos)
newtext = text[pos+1:]
# print(newtext)
floattext = float(newtext)
print(floattext)