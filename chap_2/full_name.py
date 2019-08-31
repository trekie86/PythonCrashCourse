first_name = "ada"
last_name = "lovelace"
#New way f-strings
full_name = f"{first_name} {last_name}"
#Old way format
#full_name = "{} {}".format(first_name, last_name)
message = f"Hello, {full_name.title()}!"
print(message)