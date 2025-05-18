def get_input():
    beam_length = float(input("Enter the length of the beam (in meters): "))
    load1 = float(input("Enter the load on the beam (in kN): "))
    a1 = float(input("Enter the distance from the left end (A) to the load (in meters): "))
    load2 = float(input("Enter the load on the beam (in kN): "))
    a2 = float(input("Enter the distance from the left end (A) to the load (in meters): "))
    return beam_length, load1, a1, load2, a2

#function to calculate shear force at section
def calculate_shear_force(load1, RA, a1, x):
    if x < a1:
        return RA
    elif x >= a1:
        return RA - load1
    else:
        return 0
#function to calculate bending moment at section
def calculate_bending_moment(load1, RA, a1, x):
    if x < a1:
        return RA*x
    elif x >= a1:
        return RA*x - load1*(x-a1)
    else:
        return 0
    
from Beam_Rxn_Calculator import calculate_reactions

if __name__ == "__main__":
    print("Beam Load Calculator")
    beam_length, load1, a1, load2, a2 = get_input()
    reaction_A, reaction_B = calculate_reactions(beam_length, load1, a1, load2, a2)
    
    # Get the section location from the user
    x = float(input("Enter the distance from the left end (A) to the section (in meters): "))
    
    # Calculate shear force and bending moment at the section
    shear_force = calculate_shear_force(load1, reaction_A, a1, x)
    bending_moment = calculate_bending_moment(load1, reaction_A, a1, x)
    print(f"reaction_A: {reaction_A:.2f} kN")
    print(f"reaction_B: {reaction_B:.2f} kN")
    # Display results
    print(f"\nShear Force at section {x} m: {shear_force:.2f} kN")
    print(f"Bending Moment at section {x} m: {bending_moment:.2f} kNm")