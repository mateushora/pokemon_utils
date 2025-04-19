# 🐾 Pokémon Utils

This repository contains utilities for analyzing Pokémon battles, determining type advantages, and managing Pokémon data. It is designed to help players make informed decisions during battles by leveraging type effectiveness, move data, and cached information.

---

## 📦 Modules

### 1. **`pokemon.py`**
The main entry point of the application. This module provides different modes of operation:
- **`quiz`**: Conducts an interactive quiz to test your knowledge of Pokémon type effectiveness.
- **`types`**: Fetches and displays the types of specified Pokémon.
- **`current`**: Analyzes your current Pokémon team against specified enemy Pokémon and provides recommendations based on move effectiveness and type resistance.
- **`all`**: Similar to `current`, but analyzes all owned Pokémon instead of just the current team.
- **`ability`**: Fetches and displays information about specified Pokémon abilities.

### 2. **`info.py`**
Handles the core logic for analyzing Pokémon battles:
- **`find_best_pokemon`**: Determines the best Pokémon to use against specified enemies based on move effectiveness and type resistance.
- **`get_best_moves`**: Calculates the best moves for a Pokémon against an enemy, considering move power, accuracy, and type effectiveness.

### 3. **`api.py`**
Handles fetching Pokémon data from the PokéAPI:
- **`get_pokemon_types`**: Fetches the types of specified Pokémon. If the data is already cached locally, it uses the cache instead of querying the API.
- **`get_ability_type`**: Fetches the type or effect of a specified Pokémon ability from a local cache.

> **Note**: The API will only consult the internet once for each Pokémon. After storing the information in the local cache, it will always use the cached data.

### 4. **`configs.py`**
Loads and manages configuration data for the application:
- **`POKEMON_TYPE_CHART`**: A dictionary representing type effectiveness (e.g., which types are strong, weak, or immune to others).
- **`ALL_POKEMONS_OWNED`**: A dictionary containing all owned Pokémon and their moves.
- **`MOVE_TYPES`**: A dictionary mapping moves to their types, power, and accuracy.
- **`CURRENT_POKEMON_TEAM`**: A list of Pokémon names representing the current team.

### 5. **`learn.py`**
Provides an interactive quiz to test your knowledge of Pokémon type effectiveness:
- Prompts the user to guess which types are strong, weak, immune, or not very effective against a randomly selected type.
- Evaluates the user's answers and provides feedback on correct, incorrect, and missed answers.

---

## 📂 JSON Files

All JSON files are located in the `data` folder.

### 1. **`data/pokemon_types_cache.json`**
- **Purpose**: Stores the types of Pokémon fetched from the PokéAPI.
- **When to Change**: 
  - If new Pokémon are added to the game or if you want to update the types of existing Pokémon.
  - If the cache becomes outdated or corrupted, you can delete it to force the application to fetch fresh data from the API.

### 2. **`data/pokemon_all_pokemons_owned.json`**
- **Purpose**: Stores all owned Pokémon and their moves.
- **When to Change**:
  - When you acquire new Pokémon or update the moves of existing Pokémon.
  - This file should be manually updated to reflect your current collection.

### 3. **`data/pokemon_ability_types_cache.json`**
- **Purpose**: Stores information about Pokémon abilities, including their type, power, and accuracy.
- **When to Change**:
  - If new abilities are introduced or if you want to update the data for existing abilities.
  - This file is used as a local cache and should be updated manually if needed.

### 4. **`data/pokemon_type_chart.json`**
- **Purpose**: Represents the type effectiveness chart, detailing which types are strong, weak, or immune to others.
- **When to Change**:
  - If the type effectiveness rules are updated (e.g., in a new game generation).
  - This file should only be modified if there are changes to the official type effectiveness chart.

---

## 🚀 How to Use

1. **Run the Application**:
   Use the following command to run the application:
   ```bash
   python pokemon.py <mode> [arguments]
   ```
