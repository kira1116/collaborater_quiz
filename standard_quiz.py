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
