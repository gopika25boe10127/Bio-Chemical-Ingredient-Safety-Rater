# BIO-CHEMICAL INGREDIENT SAFETY RATER
# Bio-Chemical Ingredient Safety Rater 

## Problem Statement
Many commercial personal care products contain complex chemical ingredients that are difficult for the average consumer to decode. Several of these substances are linked to biological risks, such as **endocrine disruption, skin toxicity, and environmental harm**. 

There is currently a lack of accessible, computational tools that can instantly parse these ingredient lists and provide a simplified, evidence-based safety score. This project solves this by automating the cross-referencing of chemical data with known toxicological risks.

---

## Scope of the Project
This project provides a functional **Command-Line Interface (CLI)** tool designed to perform the following:

*   **Data Management:** Creates and maintains a local database (`toxins.csv`) of high-risk cosmetic ingredients.
*   **String Analysis:** Processes raw text input from product labels and breaks them into searchable tokens.
*   **Quantitative Evaluation:** Applies a mathematical algorithm to calculate a **"Hazard Rating"** based on the presence and severity of detected toxins.
*   **Educational Reporting:** Outputs a formatted table detailing the specific biological risks associated with flagged ingredients.

---

##  Target Users
*   **Bioengineering Students:** To understand the intersection of toxicology and computational logic.
*   **Health-Conscious Consumers:** Individuals looking for a quick way to screen products for "red-flag" ingredients.
*   **Environmental Advocates:** Users interested in identifying chemicals that contribute to issues like coral bleaching (e.g., Oxybenzone).

---

##  High-Level Features
1.  **Self-Contained Database:** Automatically generates a CSV file, demonstrating file I/O operations and data persistence.
2.  **Fuzzy Ingredient Matching:** The algorithm can detect a toxin even if it is part of a compound name (e.g., finding *"paraben"* in *"methylparaben"*).
3.  **Dynamic Safety Rating (1-10):** A logic-based scoring system that weights the severity of different chemicals to provide a final product grade.
4.  **Risk Categorization:** Uses conditional logic to sort products into **"Clean," "Caution,"** or **"Hazardous"** status.
5.  **Formatted Console Output:** Utilizes tabulating techniques to present biological risks in a clear, readable table format.

---

## ⚙️ Environment Setup & Execution

### **System Requirements**
*   Python 3.x
*   VS Code 

### **Execution Steps**
1.  **Initialize Database:** Run the Python script; it will automatically create the `toxins.csv` file in your session storage/folder.
2.  **Analyze Product:** 
    *   Find an ingredient list (e.g., from the back of a face wash or shampoo bottle).
    *   Copy and paste the raw text into the input prompt.
    *   Press **Enter** to receive the safety report, risk breakdown, and the **1-10 Hazard Rating**.

---
*Developed as part of the Digital Literacy Ambassador Project | VIT Bhopal University*
Users interested in identifying chemicals that contribute to issues like coral bleaching (e.g., Oxybenzone).

# High-Level Features:

Self-Contained Database: Automatically generates a CSV file, demonstrating file I/O operations and data persistence.
Fuzzy Ingredient Matching: The algorithm can detect a toxin even if it is part of a compound name (e.g., finding "paraben" in "methylparaben").
Dynamic Safety Rating (1-10): A logic-based scoring system that weights the severity of different chemicals to provide a final product grade.
Risk Categorization: Uses conditional logic to sort products into "Clean," "Caution," or "Hazardous" status.
Formatted Console Output: Utilizes tabulating techniques to present biological risks in a clear, readable table format.

# Environment Setup & Execution:

Execution Steps:
Python code: Code is typed in VS code.

Initialize Database: Run the code, it will automatically create toxins.csv in the session storage.

Analyze Product:
Find an ingredient list (e.g., from a face wash or shampoo).
Paste the list into the input prompt.
Press Enter to receive the safety report and 1-10 rating.
