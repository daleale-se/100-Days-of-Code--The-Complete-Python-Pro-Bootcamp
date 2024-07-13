from prettytable import PrettyTable

def main():

    table = PrettyTable()

    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])

    table.align = "l"

    print(table)

    return 0


main()
