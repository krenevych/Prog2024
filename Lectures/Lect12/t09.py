from dataclasses import replace

with open("t09.txt") as f:
    content = f.read()

# print(content)

replace_what = "the"
replace_with = "a"
new_content = content.replace(replace_what, replace_with)

replace_what = "The"
replace_with = "A"
new_content = new_content.replace(replace_what, replace_with)

# print(new_content)

with open("t09.txt", "w") as f:
    f.write(new_content)