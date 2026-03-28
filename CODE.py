import csv

# STEP 1: Create the expanded Toxin Database file
# This includes common cosmetic toxins, allergens, and irritants
csv_content = """ingredient,risk,score
paraben,Endocrine disruptor; mimics estrogen,7
phthalate,Reproductive system toxicity,8
formaldehyde,Known human carcinogen,10
triclosan,Thyroid hormone disruption,6
sodium lauryl sulfate,Skin and eye irritant,3
toluene,Immune system toxin,9
oxybenzone,Hormone disruption; coral bleaching,6
fragrance,Potential hidden allergens/phthalates,5
lead,Heavy metal; neurotoxicity,10
hydroquinone,Skin bleacher; organ system toxicity,9
polyethylene glycol,"Can be contaminated with 1,4-dioxane",4
bha,Potential endocrine disruptor and carcinogen,8
bht,Skin irritant and potential hormone disruptor,5
coal tar,Known human carcinogen,10
synthetic colors,Derived from petroleum; skin irritant,4
"""

with open('toxins.csv', 'w') as f:
    f.write(csv_content)

def load_toxin_database(filename):
    """Syllabus Unit 5: Load compound data into a Dictionary"""
    database = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                database[row['ingredient'].lower()] = {
                    'risk': row['risk'],
                    'score': int(row['score'])
                }
        return database
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

def analyze_and_rate():
    toxin_db = load_toxin_database('toxins.csv')
    if not toxin_db: return

    print("=== 🔬 Bio-Chemical Ingredient Safety Rater ===")
    print("Paste ingredients from your product label (separated by commas).")
    raw_input = input("\nIngredients: ")

    # Syllabus Unit 5: List operations
    user_list = [item.strip().lower() for item in raw_input.split(',')]

    total_hazard_score = 0
    flagged_items = []

    print("\n" + "="*65)
    print(f"{'DETECTED INGREDIENT':<25} | {'SCORE':<5} | {'BIOLOGICAL RISK'}")
    print("-" * 65)

    # Syllabus Unit 3: Iteration (for loops) and Conditionals (if)
    for item in user_list:
        for toxin, data in toxin_db.items():
            if toxin in item:
                print(f"{item.title():<25} | {data['score']}/10 | {data['risk']}")
                total_hazard_score += data['score']
                flagged_items.append(item)
                break

    # --- FINAL RATING CALCULATION ---
    if len(user_list) > 0:
        # We calculate the weighted hazard based on the whole formula
        # Final Rating = (Sum of Toxin Scores) / (Total Ingredients)
        product_rating = (total_hazard_score / len(user_list)) * 1.5

        # Cap the rating between 0 and 10
        final_score = round(min(max(product_rating, 0.5), 10), 1)

        print("-" * 65)
        print(f"TOTAL INGREDIENTS ANALYZED: {len(user_list)}")
        print(f"FLAGGED TOXINS FOUND: {len(flagged_items)}")
        print(f"OVERALL PRODUCT HAZARD RATING: {final_score} / 10")

        # Syllabus Unit 3: Conditional flow (if-elif-else)
        if final_score <= 2.5:
            print("STATUS: ✅ CLEAN - Minimal to no toxic ingredients found.")
        elif 2.5 < final_score <= 5.5:
            print("STATUS: ⚠️ CAUTION - Moderate levels of irritants or disruptors.")
        else:
            print("STATUS: ❌ HAZARDOUS - High concentration of toxic substances.")
    else:
        print("Error: No ingredients detected for analysis.")

# Execute the program
if __name__ == "__main__":
    analyze_and_rate()


    