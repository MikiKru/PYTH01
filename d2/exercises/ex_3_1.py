org_name = "United Nations Educational, Scientiﬁc and Cultural Organization"

org_name_list = org_name.replace(",","").split(" ")
print(org_name_list)
acronim = ""
for word in org_name_list:
    if(word[0].isupper()):
        acronim += word[0]

print(f"Akronim: {acronim}")