from prettytable import PrettyTable

table = PrettyTable()

charmander1 = "Fire"

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", charmander1]
])
table.align = "l"

print(table)
