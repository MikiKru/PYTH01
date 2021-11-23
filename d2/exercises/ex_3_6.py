org_name = "United Nations Educational, Scientific and Cultural Organization"

acronim = "".join(word[0] for word in org_name.split() if word[0].isupper())
print(acronim)

