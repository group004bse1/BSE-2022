str = 'X-DSPAM-Confidence: 0.8475'
name = str.find(":")
print(float(str[(name + 1):]))
