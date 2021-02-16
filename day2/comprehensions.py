names = ["john", "jake", "jack", "george", "jenny", "jason"]

# without comp
filtered_names = []
for name in names:
    if len(name) < 5 and 'e' not in name:
        filtered_names.append(name)

# with comp
f_names = [ name for name in names if len(name) < 5 and 'e' not in name ]

print(filtered_names)
print(f_names)