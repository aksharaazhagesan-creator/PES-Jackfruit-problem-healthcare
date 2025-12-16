import pandas as pd

# 1. Load the CSV file
df = pd.read_csv("fake_patient.csv")
#print(df.head())

# 2. Define age group bins
bins = [0, 12, 19, 39, 59, 120]
labels = ["Child", "Teen", "Young Adult", "Middle Age", "Senior"]

# 3. Create the Age_Group column
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

# 4. Count how many patients are in each age group
age_counts = df["Age_Group"].value_counts().sort_index()

print("Age Group Distribution:")
print(age_counts)
percentages = (age_counts / len(df) * 100).round(2)

print(percentages.to_dict())





print(" ")
print(" ")
print(" ")
print(" ")
print("=== GENERAL ILLNESS SYMPTOM CHECKER ===")
print("⚠INSTRUCTIONS : NOT TO BE IGNORED⚠")
print("WARNING: NOT EQUAL TO VISITING DOCTOR  ")
print("(This symptom checker is NOT a medical diagnosis tool.It shows the closest illness that u might have according to the symptoms entered ")
print("It only provides general information based on the symptoms you enter.")
print("Do NOT rely on this program for medical decisions or emergencies.")
print("Always consult a qualified doctor for accurate diagnosis and treatment.")
print("If you experience severe symptoms or red flags, seek medical help immediately.)")
print(" ")
print(" ")
print(" ")
print(" ")
print("CHECKING STARTING......")
count=1
names = []
tokens = []
n = int(input("Enter number of patients: "))
for i in range(n):
    name = input(f"Enter name of patient {i+1}: ")
    names.append(name)
    tokens.append(i+1)
with open("AppointmentTokens.csv", "w") as file:
    file.write("Name,Token\n")
    for name, token in zip(names, tokens):
        file.write(f"{name},{token}\n")

while count<=n:# ---------------- BASIC SYMPTOMS ----------------
    fever = input("Do you have fever? (Y/N): ")
    cough = input("Do you have cough? (Dry/Wet/None): ")
    runny_nose = input("Runny or blocked nose? (Y/N): ")
    sore_throat = input("Sore throat? (Y/N): ")
    body_ache = input("Body pain / muscle ache? (Y/N): ")
    sneezing = input("Sneezing frequently? (Y/N): ")
    itchy_eyes = input("Itchy/watery eyes? (Y/N): ")
    loss_smell = input("Loss of smell or taste? (Y/N): ")
    fatigue = input("Feeling very tired? (Y/N): ")
    # ---------------- GASTRIC INFECTION SYMPTOMS ----------------
    vomiting = input("Vomiting? (Y/N): ")
    diarrhea = input("Loose stools / diarrhea? (Y/N): ")
    stomach_pain = input("Stomach pain/cramps? (Y/N): ")
    # ---------------- DENGUE-LIKE SYMPTOMS ----------------
    rash = input("Skin rash? (Y/N): ")
    behind_eye_pain = input("Pain behind the eyes? (Y/N): ")
    severe_body_ache = input("Severe body pain (like bones hurting)? (Y/N): ")
    # ---------------- DEHYDRATION SYMPTOMS ----------------
    dry_mouth = input("Dry mouth? (Y/N): ")
    low_urine = input("Very little urine output? (Y/N): ")
    dizzy = input("Feeling dizzy/lightheaded? (Y/N): ")
    # ---------------- RED FLAGS ----------------
    breathing_issue = input("Breathing difficulty? (Y/N): ")
    chest_pain = input("Chest pain? (Y/N): ")
    high_fever_days = input("Fever >102°F for more than 3 days? (Y/N): ")

    diagnosis = ""
    advice = ""
    # ---------------- EMERGENCY CHECK ----------------
    if (breathing_issue == "Y" or high_fever_days) and chest_pain == "Y":
        diagnosis = "EMERGENCY"
        advice = "Seek emergency medical help IMMEDIATELY."
    # ---------------- SINUS INFECTION ----------------
    elif runny_nose == "Y" and (sore_throat == "Y" or fever == "Y") and cough == "Wet":
        diagnosis = "Sinus Infection"
        advice = "Warm steam, hydration, and consult doctor if fever persists."
    # ---------------- COMMON COLD ----------------
    elif runny_nose == "Y" and sneezing == "Y" and fever == "N":
        diagnosis = "Common Cold"
        advice = "Rest, warm fluids, and over the counter cold meds may help."
    # ---------------- ALLERGIES ----------------
    elif sneezing == "Y" and itchy_eyes == "Y" and fever == "N":
        diagnosis = "Allergies"
        advice = "Avoid triggers; antihistamines help."
    # ---------------- DENGUE CHECK----------------
    elif fever == "Y" and (rash == "Y" or behind_eye_pain == "Y" or severe_body_ache == "Y"):
        diagnosis = "Dengue-like Symptoms"
        advice = "HIGH RISK: Drink plenty of fluids & get tested for dengue IMMEDIATELY."
    # ------------GASTRIC INFECTION (Viral/food poisoning)------------
    elif vomiting == "Y" or diarrhea == "Y":
        if fever == "Y" or stomach_pain == "Y":
            diagnosis = "Gastric Infection (Viral/Food poisoning)"
            advice = "Hydrate with ORS; avoid oily food; consult doctor if symptoms worsen."
        else:
            diagnosis = "Mild Gastric Upset"
            advice = "Drink ORS and rest."
    # ------------DEHYDRATION------------
    elif dry_mouth == "Y" and low_urine == "Y":
        diagnosis = "Dehydration"
        advice = "Drink ORS / water immediately. Rest and monitor."
    elif dizzy == "Y" and dry_mouth == "Y":
        diagnosis = "Mild Dehydration"
        advice = "Drink water slowly and rest."
    # ----------------SINUS INFECTION----------------
    elif runny_nose == "Y" and (sore_throat == "Y" or fever == "Y") and cough == "Wet":
        diagnosis = "Sinus Infection"
        advice = "Warm steam, hydration, and consult doctor if fever persists."
    # --------------------ALLERGIES--------------------
    elif sneezing == "Y" and itchy_eyes == "Y" and fever == "N":
        diagnosis = "Allergies"
        advice = "Avoid triggers; antihistamines help."
    # ---------------- FEVER (GENERIC) ----------------
    elif fever == "Y" and cough == "None" and runny_nose == "N":
        diagnosis = "Simple Fever"
        advice = "Stay hydrated; paracetamol can reduce fever."
    # ---------------- FLU ----------------
    elif fever == "Y" and body_ache == "Y" and cough in ["Dry", "Wet"]:
        diagnosis = "Flu (Influenza)"
        advice = "Rest well, hydrate, take fever meds, consult doctor if worsening."
    # ---------------- COVID-LIKE ----------------
    elif loss_smell == "Y" or (fever == "Y" and cough == "Dry"):
        diagnosis = "COVID-Like Illness"
        advice = "Isolate, monitor symptoms, get tested if needed."
    # ---------------- FATIGUE-RELATED ----------------
    elif fatigue == "Y" and fever == "N" and cough == "None":
        diagnosis = "Fatigue / Mild Viral Infection"
        advice = "Sleep well, hydrate, take light food."
    # ---------------- UNKNOWN ----------------
    else:
        diagnosis = "Unclassified Illness"
        advice = "Symptoms don’t match a category. Rest and monitor."
    print("=== RESULT ===")
    print("Diagnosis:", diagnosis)
    print("Advice:", advice)




    #---------- COLORS ----------
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;208m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

    # ---------- BMI FUNCTIONS ----------
    def calculate_bmi(weight_kg, height_m):
        return round(weight_kg / (height_m ** 2), 2)

    def bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight", YELLOW
        elif bmi < 25:
            return "Normal weight", GREEN
        elif bmi < 30:
            return "Overweight", ORANGE
        else:
            return "Obese", RED

    def ideal_weight_range(height_m):
        """Returns (min_weight, max_weight) for BMI 18.5–24.9"""
        min_w = 18.5 * (height_m ** 2)
        max_w = 24.9 * (height_m ** 2)
        return round(min_w, 1), round(max_w, 1)

    # ---------- MAIN PROGRAM ----------
    def main():

        # Weight input
        weight = float(input("\nEnter your weight: "))
        unit_w = input("Is this in kg or lbs? (kg/lb): ").strip().lower()
        if unit_w in ("lb", "lbs"):
            weight *= 0.453592

        # Height input
        height = float(input("\nEnter your height: "))
        unit_h = input("Is this in meters or cm? (m/cm): ").strip().lower()
        if unit_h == "cm":
            height /= 100

        # Calculations
        bmi = calculate_bmi(weight, height)
        category, color = bmi_category(bmi)
        ideal_min, ideal_max = ideal_weight_range(height)

        # Output section
        print("\n" + MAGENTA + "----------------------------------------" + RESET)
        print(CYAN + f" Your BMI is: {bmi}" + RESET)
        print(color + f" Category: {category}" + RESET)
        print(GREEN + f" Ideal Weight Range: {ideal_min} kg – {ideal_max} kg" + RESET)
        print(MAGENTA + "----------------------------------------" + RESET)

        # Suggestions based on category
        print("\n" + CYAN + "Suggestions:" + RESET)

        if category == "Normal weight":
            print(GREEN +
                "• Maintain a balanced diet\n"
                "• Continue regular exercise\n"
                "• Keep up the healthy lifestyle" + RESET)

        elif category == "Underweight":
            print(YELLOW +
                "• Eat calorie-dense, nutritious foods\n"
                "• Include protein-rich meals\n"
                "• Strength training helps gain healthy weight\n"
                "• Increase meal frequency" + RESET)

        elif category == "Overweight":
            print(ORANGE +
                "• Reduce sugar and fried foods\n"
                "• Walk 30–45 minutes daily\n"
                "• Include more vegetables and fruits\n"
                "• Practice portion control" + RESET)

        else:  # Obese
            print(RED +
                "• Start with light exercises (walking, cycling)\n"
                "• Avoid sugary drinks and high-calorie junk food\n"
                "• Drink plenty of water\n"
                "• Consider consulting a nutritionist" + RESET)

    if __name__ == "__main__":
        main()
    count+=1