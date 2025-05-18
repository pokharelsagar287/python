#taking necessary inputs

def get_input():
    beam_length = float(input("Enter the length of the beam (in meters): "))
    load1 = float(input("Enter the load on the beam (in kN): "))
    a1 = float(input("Enter the distance from the left end (A) to the load (in meters): "))
    load2 = float(input("Enter the load on the beam (in kN): "))
    a2 = float(input("Enter the distance from the left end (A) to the load (in meters): "))
    return beam_length, load1, a1, load2, a2


#function to calculate the reactions at supports
def calculate_reactions(beam_length, load1, a1, load2, a2):
    # Calculate the total load
    total_load = load1 + load2

    # Calculate the moment about point A
    moment_A = (load1 * a1) + (load2 * a2)

    # Calculate the reaction at support A
    reaction_B = moment_A / beam_length

    # Calculate the reaction at support B
    reaction_A = total_load - reaction_B

    return reaction_A, reaction_B

#function to display the results
def display_results(reaction_A, reaction_B):
    print(f"\nReaction at support A: {reaction_A:.2f} kN")
    print(f"Reaction at support B: {reaction_B:.2f} kN")



#main function to run the program
if __name__ == "__main__":
    print("Beam Load Calculator")
    beam_length, load1, a1, load2, a2 = get_input()
    reaction_A, reaction_B = calculate_reactions(beam_length, load1, a1, load2, a2)
    display_results(reaction_A, reaction_B)




