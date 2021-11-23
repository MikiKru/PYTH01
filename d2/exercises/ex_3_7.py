from math import ceil

text = "Kajak :-)"

clean_text = [char.upper() for char in text if char.isalnum()]
print(clean_text[: ceil((len(clean_text))/2)], clean_text[-1:-ceil((len(clean_text))/2) - 1:-1], clean_text[:] == clean_text[::-1])


