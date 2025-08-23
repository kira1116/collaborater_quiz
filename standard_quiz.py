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
