people = {
    "first": "Alice",
    "second": "Bob",
    "third": "Charlie"
}

new_key = input("Enter the key for new person: ")
new_name = input("Enter the name to add: ")
people[new_key] = new_name
print("After adding:", people)

del_key = input("Enter the key to delete: ")
if del_key in people:
    del people[del_key]
    print("After deletion:", people)
else:
    print(f"Key '{del_key}' not found")

print("Current dictionary:", people)
