import random
from textwrap import fill

# ================ QUESTION BANK (100 total) ================
# Each entry: {"q": "...", "choices": ["A) ...","B) ...","C) ...","D) ..."], "answer":"A","explain":"..."}
#develop by kirubel
CHEMISTRY = [
    {"q":"Which subatomic particle has a negative charge?", "choices":["A) Proton","B) Neutron","C) Electron","D) Positron"], "answer":"C","explain":"Electrons carry a negative charge."},
    {"q":"Atomic number equals the number of __.", "choices":["A) Neutrons","B) Protons","C) Electrons + Neutrons","D) Nucleons"], "answer":"B","explain":"Atomic number is the number of protons."},
    {"q":"Which bond involves sharing of electrons?", "choices":["A) Ionic","B) Covalent","C) Metallic","D) Hydrogen"], "answer":"B","explain":"Covalent bonds form by sharing electron pairs."},
    {"q":"pH < 7 indicates a(n) __ solution.", "choices":["A) Basic","B) Neutral","C) Acidic","D) Buffer"], "answer":"C","explain":"Acids have pH less than 7."},
    {"q":"Avogadro’s number is approximately:", "choices":["A) 3.14×10^8","B) 6.02×10^23","C) 9.81","D) 1.38×10^-23"], "answer":"B","explain":"One mole contains 6.02×10^23 entities."},
    {"q":"Which gas law relates pressure and volume at constant T?", "choices":["A) Charles’s law","B) Boyle’s law","C) Avogadro’s law","D) Gay-Lussac’s law"], "answer":"B","explain":"Boyle’s law: P ∝ 1/V at constant T."},
    {"q":"Which is an alkaline earth metal?", "choices":["A) Na","B) Mg","C) Al","D) Fe"], "answer":"B","explain":"Group 2 metals include Mg, Ca, etc."},
    {"q":"Oxidation is defined as:", "choices":["A) Gain of electrons","B) Loss of electrons","C) Gain of neutrons","D) Loss of protons"], "answer":"B","explain":"LEO: Loss of Electrons is Oxidation."},
    {"q":"Which intermolecular force is strongest?", "choices":["A) London dispersion","B) Dipole–dipole","C) Hydrogen bonding","D) Ion–dipole"], "answer":"D","explain":"Ion–dipole is typically stronger than H-bonding."},
    {"q":"The shape of methane (CH4) is:", "choices":["A) Linear","B) Bent","C) Trigonal planar","D) Tetrahedral"], "answer":"D","explain":"Four electron pairs around C → tetrahedral."},
    {"q":"Endothermic reactions __ heat.", "choices":["A) Release","B) Absorb","C) Neither release nor absorb","D) Destroy"], "answer":"B","explain":"Endo = absorbs heat from surroundings."},
    {"q":"Which is a strong acid?", "choices":["A) HF","B) HCl","C) CH3COOH","D) H2CO3"], "answer":"B","explain":"HCl fully ionizes in water."},
    {"q":"In water, the oxygen atom is more __ than hydrogen.", "choices":["A) Electropositive","B) Electronegative","C) Massive","D) Metallic"], "answer":"B","explain":"O has greater electronegativity than H."},
    {"q":"Which separation uses different boiling points?", "choices":["A) Filtration","B) Chromatography","C) Distillation","D) Decanting"], "answer":"C","explain":"Distillation separates based on volatility."},
    {"q":"Molarity is moles of solute per __ of solution.", "choices":["A) Gram","B) Liter","C) Mole","D) Kelvin"], "answer":"B","explain":"M = mol/L."},
    {"q":"Catalysts work by lowering the __.", "choices":["A) Equilibrium constant","B) Activation energy","C) Enthalpy of products","D) Temperature"], "answer":"B","explain":"Catalysts reduce activation energy barrier."},
    {"q":"Which is a noble gas?", "choices":["A) N2","B) O2","C) Ne","D) Cl2"], "answer":"C","explain":"Neon is a Group 18 noble gas."},
    {"q":"Which orbital can hold up to 10 electrons?", "choices":["A) s","B) p","C) d","D) f"], "answer":"C","explain":"d subshell holds 10 electrons."},
    {"q":"The empirical formula is based on:", "choices":["A) Actual atoms per molecule","B) Simplest whole-number ratio","C) Molecular mass","D) Avogadro’s number"], "answer":"B","explain":"Empirical = simplest ratio."},
    {"q":"Which compound is ionic?", "choices":["A) CO2","B) H2O","C) NaCl","D) NH3"], "answer":"C","explain":"Metal + nonmetal → ionic, e.g., NaCl."},
]
#this part is done by kira

#develop by nejat
PHYSICS = [
    {"q":"SI unit of force is:", "choices":["A) Joule","B) Pascal","C) Newton","D) Watt"], "answer":"C","explain":"Force unit is Newton (kg·m/s^2)."},
    {"q":"Speed with direction is called:", "choices":["A) Acceleration","B) Velocity","C) Displacement","D) Momentum"], "answer":"B","explain":"Velocity is a vector."},
    {"q":"Which law states F = ma?", "choices":["A) Newton’s 1st","B) Newton’s 2nd","C) Newton’s 3rd","D) Hooke’s law"], "answer":"B","explain":"Second law links force, mass, acceleration."},
    {"q":"Work is defined as:", "choices":["A) F/d","B) F×d (along displacement)","C) m×g","D) P×t"], "answer":"B","explain":"W = F·d·cosθ."},
    {"q":"Kinetic energy formula:", "choices":["A) mgh","B) 1/2 mv^2","C) qV","D) PΔV"], "answer":"B","explain":"Translational KE = 1/2 mv^2."},
    {"q":"Which wave needs a medium?", "choices":["A) Light","B) Radio","C) Sound","D) X-ray"], "answer":"C","explain":"Sound is mechanical; needs a medium."},
    {"q":"Ohm’s law is:", "choices":["A) P=IV","B) V=IR","C) Q=It","D) E=mc^2"], "answer":"B","explain":"Voltage = current × resistance."},
    {"q":"Unit of power:", "choices":["A) Joule","B) Watt","C) Newton","D) Coulomb"], "answer":"B","explain":"Power unit is Watt (J/s)."},
    {"q":"Refraction occurs when light:", "choices":["A) Changes medium","B) Reflects off mirror","C) Diffracts around edges","D) Interferes"], "answer":"A","explain":"Refraction is bending due to speed change."},
    {"q":"Density is mass per:", "choices":["A) Force","B) Volume","C) Area","D) Time"], "answer":"B","explain":"ρ = m/V."},
    {"q":"Momentum is:", "choices":["A) m/a","B) mv","C) ma^2","D) m/v"], "answer":"B","explain":"Linear momentum p = mv."},
    {"q":"Gravitational acceleration near Earth:", "choices":["A) 3.0 m/s^2","B) 9.8 m/s^2","C) 15 m/s^2","D) 1.6 m/s^2"], "answer":"B","explain":"g ≈ 9.8 m/s^2."},
    {"q":"Unit of frequency:", "choices":["A) Hertz","B) Tesla","C) Volt","D) Weber"], "answer":"A","explain":"1 Hz = 1/s."},
    {"q":"Coulomb’s law involves:", "choices":["A) Masses","B) Charges","C) Temperatures","D) Pressures"], "answer":"B","explain":"Electrostatic force between charges."},
    {"q":"Lens that converges light:", "choices":["A) Concave","B) Convex","C) Planar","D) Cylindrical"], "answer":"B","explain":"Convex (converging) lens."},
    {"q":"Thermodynamic temperature unit:", "choices":["A) °C","B) °F","C) K","D) R"], "answer":"C","explain":"Kelvin is SI base unit."},
    {"q":"In SHM, restoring force is proportional to:", "choices":["A) Velocity","B) Displacement","C) Acceleration","D) Time"], "answer":"B","explain":"F = -kx."},
    {"q":"Unit of electric charge:", "choices":["A) Ampere","B) Coulomb","C) Ohm","D) Farad"], "answer":"B","explain":"Charge is measured in coulombs."},
    {"q":"Transformer works on:", "choices":["A) DC","B) AC","C) Both","D) Neither"], "answer":"B","explain":"Transformers require changing magnetic flux (AC)."},
    {"q":"The slope of a velocity–time graph gives:", "choices":["A) Velocity","B) Displacement","C) Acceleration","D) Jerk"], "answer":"C","explain":"dv/dt = acceleration."},
]    
#developd by hawlet
MATH = [
    {"q":"Solve: 2x + 6 = 14. x = ?", "choices":["A) 3","B) 4","C) 5","D) 6"], "answer":"B","explain":"2x=8 → x=4."},
    {"q":"Area of a circle with r=3:", "choices":["A) 6π","B) 9π","C) 3π","D) 12π"], "answer":"B","explain":"A=πr^2=9π."},
    {"q":"Derivative of x^2 is:", "choices":["A) x","B) 2x","C) x^3","D) 2"], "answer":"B","explain":"d/dx x^2 = 2x."},
    {"q":"(3/4) + (1/2) =", "choices":["A) 1","B) 5/4","C) 3/8","D) 7/8"], "answer":"B","explain":"3/4 + 1/2 = 3/4 + 2/4 = 5/4."},
    {"q":"Solve: 3(x-1)=9 → x=?", "choices":["A) 2","B) 3","C) 4","D) 5"], "answer":"C","explain":"3x-3=9 → 3x=12 → x=4."},
    {"q":"Slope between (0,0) and (2,6):", "choices":["A) 2","B) 3","C) 4","D) 6"], "answer":"B","explain":"m=Δy/Δx=6/2=3."},
    {"q":"Mean of 2, 4, 6, 8:", "choices":["A) 4","B) 5","C) 6","D) 7"], "answer":"B","explain":"Average = (20)/4=5."},
    {"q":"Probability of heads (fair coin):", "choices":["A) 0","B) 1/4","C) 1/2","D) 1"], "answer":"C","explain":"Fair coin → 0.5."},
    {"q":"√81 =", "choices":["A) 7","B) 8","C) 9","D) 10"], "answer":"C","explain":"9×9=81."},
    {"q":"Log10(100) =", "choices":["A) 1","B) 2","C) 10","D) 100"], "answer":"B","explain":"10^2=100."},
    {"q":"Perimeter of square side 5:", "choices":["A) 10","B) 15","C) 20","D) 25"], "answer":"C","explain":"4×5=20."},
    {"q":"If y=3x+1, y when x=2:", "choices":["A) 5","B) 6","C) 7","D) 8"], "answer":"C","explain":"3*2+1=7."},
    {"q":"Solve: x^2=49 → x=?", "choices":["A) 6","B) 7","C) ±7","D) 14"], "answer":"C","explain":"x=±7."},
    {"q":"Median of 1,3,5,7,9:", "choices":["A) 3","B) 5","C) 7","D) 9"], "answer":"B","explain":"Middle value is 5."},
    {"q":"Simple interest I=Prt; I for P=1000,r=0.1,t=2:", "choices":["A) 100","B) 150","C) 200","D) 250"], "answer":"C","explain":"I=1000*0.1*2=200."},
    {"q":"(a+b)^2 =", "choices":["A) a^2+b^2","B) a^2+2ab+b^2","C) 2ab","D) a^2-2ab+b^2"], "answer":"B","explain":"Binomial expansion."},
    {"q":"1/0 is:", "choices":["A) 0","B) 1","C) Undefined","D) Infinity"], "answer":"C","explain":"Division by zero undefined."},
    {"q":"Integral of 1 dx =", "choices":["A) 0","B) x","C) x^2","D) 1/x"], "answer":"B","explain":"∫1 dx = x + C."},
    {"q":"GCD of 12 and 18:", "choices":["A) 2","B) 3","C) 6","D) 12"], "answer":"C","explain":"Common divisors → largest is 6."},
    {"q":"If a:b=2:3 and b:c=3:4, then a:c =", "choices":["A) 1:2","B) 2:4","C) 2:4.5","D) 2:4 (simplify 1:2)"], "answer":"A","explain":"a:b=2:3, b:c=3:4 → a:c=2:4=1:2."},
]
#developd by hikma
ENGLISH = [
    {"q":"Choose the correct form: She __ to school every day.", "choices":["A) go","B) goes","C) going","D) gone"], "answer":"B","explain":"3rd person singular takes -es."},
    {"q":"Pick the synonym of 'rapid':", "choices":["A) slow","B) quick","C) late","D) lazy"], "answer":"B","explain":"'Rapid' ≈ 'quick'."},
    {"q":"Identify the verb: The cat sleeps peacefully.", "choices":["A) cat","B) sleeps","C) peacefully","D) the"], "answer":"B","explain":"'Sleeps' is the action."},
    {"q":"'Their' is used to show:", "choices":["A) place","B) time","C) possession","D) comparison"], "answer":"C","explain":"'Their' is possessive pronoun."},
    {"q":"Correct sentence:", "choices":["A) He don't like tea.","B) She doesn't likes tea.","C) He doesn't like tea.","D) She don't like tea."], "answer":"C","explain":"Doesn't + base verb."},
    {"q":"Antonym of 'scarce':", "choices":["A) rare","B) abundant","C) little","D) slight"], "answer":"B","explain":"'Abundant' is opposite of 'scarce'."},
    {"q":"Fill in: I have lived here __ 2019.", "choices":["A) since","B) for","C) during","D) at"], "answer":"A","explain":"'Since' + starting point."},
    {"q":"Choose the correct word: It's __ book.", "choices":["A) you","B) your","C) you're","D) yours'"], "answer":"B","explain":"'Your' is possessive adjective."},
    {"q":"Plural of 'child' is:", "choices":["A) childs","B) childrens","C) childes","D) children"], "answer":"D","explain":"Irregular plural."},
    {"q":"Which is a noun?", "choices":["A) quickly","B) happiness","C) run","D) very"], "answer":"B","explain":"'Happiness' is a noun."},
    {"q":"Comparative of 'good':", "choices":["A) gooder","B) more good","C) better","D) best"], "answer":"C","explain":"Good → better → best."},
    {"q":"Choose correct: The books are on __ table.", "choices":["A) a","B) an","C) the","D) those"], "answer":"C","explain":"Specific table → 'the'."},
    {"q":"Past of 'go' is:", "choices":["A) goed","B) gone","C) went","D) going"], "answer":"C","explain":"Irregular verb: go → went."},
    {"q":"'They're' means:", "choices":["A) they are","B) their","C) there","D) they were"], "answer":"A","explain":"'They're' = they are."},
    {"q":"Choose the correct tag: You’re coming, __?", "choices":["A) are you","B) aren’t you","C) do you","D) don’t you"], "answer":"B","explain":"Positive statement → negative tag."},
    {"q":"Best word: She gave a __ speech.", "choices":["A) inspire","B) inspiration","C) inspiring","D) inspiredly"], "answer":"C","explain":"Adjective needed: 'inspiring'."},
    {"q":"Fill in: He is interested __ math.", "choices":["A) on","B) in","C) at","D) for"], "answer":"B","explain":"Interested in + noun."},
    {"q":"Correct spelling:", "choices":["A) accomodate","B) accommodate","C) acommodate","D) accomadate"], "answer":"B","explain":"Double c, double m."},
    {"q":"Choose clearer sentence:", "choices":["A) Me and him are friends.","B) He and I are friends.","C) Him and me are friends.","D) I and he are friends."], "answer":"B","explain":"Subject pronouns: He and I."},
    {"q":"'Few' vs 'a few': 'a few' means:", "choices":["A) almost none","B) none","C) some (positive)","D) many"], "answer":"C","explain":"'A few' = some; 'few' = not many (negative)."},
]

#develop by kira
SAT = [
    {"q":"Math: If 5x+10=0, x=?", "choices":["A) -2","B) -5","C) 2","D) 5"], "answer":"A","explain":"5x=-10 → x=-2."},
    {"q":"Reading: In context, 'robust' most nearly means:", "choices":["A) fragile","B) strong","C) narrow","D) quiet"], "answer":"B","explain":"'Robust' = strong."},
    {"q":"Writing: Choose correct: The data __ conclusive.", "choices":["A) is","B) are","C) was","D) be"], "answer":"B","explain":"'Data' (plural) → 'are' in formal usage."},
    {"q":"Math: Slope of line through (1,2) & (3,6):", "choices":["A) 2","B) 3","C) 4","D) 5"], "answer":"A","explain":"(6-2)/(3-1)=4/2=2."},
    {"q":"Math: If a∝b and a=6 when b=3, then a when b=9:", "choices":["A) 12","B) 18","C) 6","D) 3"], "answer":"B","explain":"Direct proportion: a=k b. k=2 → a=18."},
    {"q":"Reading: 'Mitigate' most nearly means:", "choices":["A) worsen","B) soften","C) measure","D) ignore"], "answer":"B","explain":"'Mitigate' = make less severe."},
    {"q":"Writing: Choose correct: Neither the coach nor the players __ ready.", "choices":["A) was","B) were","C) is","D) be"], "answer":"B","explain":"Verb agrees with nearer subject 'players'."},
    {"q":"Math: Median of 2,4,9,10,11:", "choices":["A) 4","B) 9","C) 10","D) 11"], "answer":"B","explain":"Ordered list → middle is 9."},
    {"q":"Math: If x^2=16, x could be:", "choices":["A) -4 or 4","B) 4 only","C) -4 only","D) 8"], "answer":"A","explain":"Square roots give ± solutions."},
    {"q":"Reading: 'Ambiguous' means:", "choices":["A) clear","B) vague","C) certain","D) trivial"], "answer":"B","explain":"'Ambiguous' = open to multiple meanings."},
    {"q":"Writing: Choose concise: 'At this point in time' →", "choices":["A) currently","B) time now","C) at time point","D) at presently"], "answer":"A","explain":"'Currently' is concise."},
    {"q":"Math: Simple interest on $500 at 8% for 3 years:", "choices":["A) $40","B) $80","C) $120","D) $150"], "answer":"C","explain":"I=Prt=500*0.08*3=120."},
    {"q":"Math: If 2(x-3)=x+1, x=?", "choices":["A) 5","B) 6","C) 7","D) 8"], "answer":"C","explain":"2x-6=x+1 → x=7."},
    {"q":"Reading: Tone 'sarcastic' is best described as:", "choices":["A) sincere praise","B) ironic mockery","C) factual neutrality","D) fearful anxiety"], "answer":"B","explain":"Sarcasm uses irony to mock."},
    {"q":"Writing: Correct pronoun: Everyone must bring __ own book.", "choices":["A) his","B) their","C) they","D) them"], "answer":"B","explain":"Singular 'they' is accepted in SAT style."},
    {"q":"Math: If f(x)=3x-2, f(5)=", "choices":["A) 13","B) 15","C) 17","D) 11"], "answer":"A","explain":"3*5-2=13."},
    {"q":"Math: 30% of 200 is:", "choices":["A) 40","B) 50","C) 60","D) 80"], "answer":"C","explain":"0.3*200=60."},
    {"q":"Reading: 'Pragmatic' means:", "choices":["A) idealistic","B) practical","C) poetic","D) random"], "answer":"B","explain":"'Pragmatic' = practical."},
    {"q":"Writing: Place comma: After dinner we went home.", "choices":["A) After dinner, we went home.","B) After, dinner we went home.","C) After dinner we, went home.","D) After dinner we went, home."], "answer":"A","explain":"Introductory phrase → comma."},
    {"q":"Math: If 3x+2=17, then x=?", "choices":["A) 3","B) 4","C) 5","D) 6"], "answer":"C","explain":"3x=15 → x=5."},
]

QUESTION_BANK = {
    "Chemistry": CHEMISTRY,
    "Physics": PHYSICS,
    "Math": MATH,
    "English": ENGLISH,
    "SAT": SAT,
}
#developed by group memeber
# Sanity check counts:
# 5 subjects × 20 each = 100
assert all(len(v) == 20 for v in QUESTION_BANK.values())

# ================== QUIZ ENGINE ==================

def ask_question(i, item):
    print(f"\nQ{i}. {fill(item['q'], width=90)}")
    for ch in item["choices"]:
        print(ch)
    while True:
        user = input("Your answer (A/B/C/D): ").strip().upper()
        if user in ["A","B","C","D"]:
            break
        print("Please enter A, B, C, or D.")
    correct = (user == item["answer"])
    if correct:
        print(" Correct!")
    else:
        print(f" Incorrect. Correct answer: {item['answer']}")
    print("Note:", fill(item["explain"], width=90))
    return 1 if correct else 0

def run_quiz(categories):
    # categories: list of subject names to include
    pool = []
    for cat in categories:
        pool.extend(QUESTION_BANK[cat])
    random.shuffle(pool)
    score = 0
    print("="*80)
    title = " & ".join(categories) if len(categories) <= 2 else f"{len(categories)} Subjects"
    print(f" QUIZ START — {title} — {len(pool)} questions")
    print("="*80)
    for i, q in enumerate(pool, start=1):
        score += ask_question(i, q)
    print("\n" + "-"*80)
    percent = round(100*score/len(pool), 1)
    print(f"Final Score: {score}/{len(pool)}  ({percent}%)")
    if len(pool) == 100:
        # Game rule: if score <= 30, auto retry
        if score <= 30:
            print(" Score is 30 or below. Let's train more! Restarting the 100-question game...\n")
            return "retry"
        else:
            print(" Nice work! You beat the 30-point threshold for the full game.")
    else:
        print(" Good effort! Try to improve your score next round.")
    return "done"

def choose_categories():
    print("\nChoose a subject:")
    print("  1) Chemistry")
    print("  2) Physics")
    print("  3) Math")
    print("  4) English")
    print("  5) SAT")
    print("  6) All (100 questions)")
    while True:
        choice = input("Enter 1-6: ").strip()
        if choice in list("123456"):
            choice = int(choice)
            break
        print("Please enter a number from 1 to 6.")
    if choice == 1:
        return ["Chemistry"]
    if choice == 2:
        return ["Physics"]
    if choice == 3:
        return ["Math"]
    if choice == 4:
        return ["English"]
    if choice == 5:
        return ["SAT"]
    return ["Chemistry","Physics","Math","English","SAT"]

def main():
    print("="*80)
    print(" welcome to panda QUIZ (100 question across 5 subjects)")
    # panda is our group name
    print("Choose one subject or play ALL 100 as a game.")
    print("Game rule: In ALL mode, if your score is 30 or less, the game restarts.")
    print("="*80)
    while True:
        cats = choose_categories()
        result = run_quiz(cats)
        if result == "retry":
            # Automatically restart ALL mode
            continue
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print(" Thanks for playing! Keep practicing and come back soon.")
            break

if __name__ == "__main__":
    main()
