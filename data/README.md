# 📂 Data Folder

This folder contains all JSON files used by the application to store Pokémon-related data. These files include cached information fetched from the PokéAPI and manually updated data for your Pokémon collection.

---

## JSON Files

### 1. **`pokemon_types_cache.json`**
- **Purpose**: Stores the types of Pokémon fetched from the PokéAPI.
- **When to Change**: 
  - If new Pokémon are added to the game or if you want to update the types of existing Pokémon.
  - If the cache becomes outdated or corrupted, you can delete it to force the application to fetch fresh data from the API.

### 2. **`pokemon_all_pokemons_owned.json`**
- **Purpose**: Stores all owned Pokémon and their moves.
- **When to Change**:
  - When you acquire new Pokémon or update the moves of existing Pokémon.
  - This file should be manually updated to reflect your current collection.

### 3. **`pokemon_ability_types_cache.json`**
- **Purpose**: Stores information about Pokémon abilities, including their type, power, and accuracy.
- **When to Change**:
  - If new abilities are introduced or if you want to update the data for existing abilities.
  - This file is used as a local cache and should be updated manually if needed.

### 4. **`pokemon_type_chart.json`**
- **Purpose**: Represents the type effectiveness chart, detailing which types are strong, weak, or immune to others.
- **When to Change**:
  - If the type effectiveness rules are updated (e.g., in a new game generation).
  - This file should only be modified if there are changes to the official type effectiveness chart.

---

## Notes
- Ensure these files are kept up-to-date for accurate results.
- Cached files (i.e., `pokemon_types_cache.json`) can be deleted to force the application to fetch fresh data from the PokéAPI.
- Manually updated files (e.g., `pokemon_all_pokemons_owned.json`) should reflect your current Pokémon collection and moves.