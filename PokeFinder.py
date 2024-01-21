import requests

def get_pokemon_info_by_english_name(english_name):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{english_name.lower()}/"
    response = requests.get(pokemon_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print("Pokemon Information:")
        print("Name:", pokemon_data.get("name", "N/A"))
        print("Type:", ", ".join([t["type"]["name"] for t in pokemon_data.get("types", [])]))
        print("Abilities:", ", ".join([a["ability"]["name"] for a in pokemon_data.get("abilities", [])]))

        # Show effectiveness against and resistance to other types
        show_type_effectiveness(pokemon_data.get("types", []))

        # Display base stats and total base stat
        base_stats = pokemon_data.get("stats", [])
        print("\nBase Stats:")
        for stat in base_stats:
            print(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")
        print(f"Total Base Stat: {sum(stat['base_stat'] for stat in base_stats)}")

        return

    print(f"Pokemon with English name '{english_name}' not found.")

def show_type_effectiveness(types):
    for target_type in types:
        print(f"\nType Effectiveness against {target_type['type']['name'].capitalize()}:")
        type_url = target_type['type']['url']
        type_data = requests.get(type_url).json()

        damage_relations = type_data.get('damage_relations', {})
        for relation_type, target_types in damage_relations.items():
            print(f"{relation_type.capitalize()}:")
            for target_type in target_types:
                print(f"  - {target_type['name'].capitalize()}")

if __name__ == "__main__":
    while True:
        english_name = input("Enter the English name of a Pokémon (type 'exit' to quit): ")
        if english_name.lower() == 'exit':
            break
        get_pokemon_info_by_english_name(english_name)

# End of program
