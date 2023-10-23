# Define list of animals, 2 of which we are given the value for
Animals = {
    'Snail': 17, 'Spider': 0, 'Green': 0,
    'Brown': 2, 'Bee': 0, 'Fly': 0,
    'Ladybird': 0, 'Butterfly': 0, 'Hopper': 0
}

# Define list of letters
Letters = {
    1: "A", 2: "B", 3: "L", 4: "T", 7: "W", 8: "X", 10: "P", 12: "G", 13: "V",
    14: "R", 15: "O", 16: "S", 17: "I", 18: "E", 19: "U", 20: "Z"
}

# Define all other possible values for animals
values = [1, 3, 4, 7, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20]

# Introduced this to track progress
iterations = 0

# From the diagram, the value of the LadyBird should be easily calculatable
Animals['Ladybird'] = 26 - (Animals['Snail'] + Animals['Brown'])

# Loop through possible values for spider
for spider_val in values:
    Animals['Spider'] = spider_val

    # Loop through possible values for green
    for green_val in values:
        Animals['Green'] = green_val

        # Skip to next iteration of green if this one doesn't satisfy the first equation
        if Animals['Snail'] + Animals['Spider'] + Animals['Green'] != 37:
            continue

        # Loop through possible values for bee
        for bee_val in values:
            Animals['Bee'] = bee_val

            # Loop through possible values for fly
            for fly_val in values:
                Animals['Fly'] = fly_val

                # Skip to next iteration of fly if this one doesn't work
                if Animals['Brown'] + Animals['Bee'] + Animals['Fly'] != 19:
                    continue

                # Loop through possible values for butterfly
                for butterfly_val in values:
                    Animals['Butterfly'] = butterfly_val

                    # Calculate the value for Hopper directly to satisfy the constraints
                    Animals['Hopper'] = 38 - (Animals['Ladybird'] + Animals['Butterfly'])

                    # Count the steps
                    iterations += 1

                    if Animals['Hopper'] not in values:
                        continue

                    # Check if totals are correct
                    if (
                            Animals['Snail'] + Animals['Spider'] + Animals['Green'] == 37 and
                            Animals['Brown'] + Animals['Bee'] + Animals['Fly'] == 19 and
                            Animals['Ladybird'] + Animals['Butterfly'] + Animals['Hopper'] == 38 and
                            Animals['Snail'] + Animals['Brown'] + Animals['Ladybird'] == 26 and
                            Animals['Spider'] + Animals['Bee'] + Animals['Butterfly'] == 41 and
                            Animals['Green'] + Animals['Fly'] + Animals['Hopper'] == 27
                    ):
                        # Set word
                        # word = Letters[Animals['Butterfly']] + Letters[Animals['Snail']] + Letters[Animals['Hopper']] + Letters[Animals['Ladybird']] + Letters[Animals['Bee']]
                        word = Letters[Animals['Butterfly']] + Letters[Animals['Snail']] + Letters[Animals['Hopper']] + \
                               Letters[Animals['Ladybird']] + Letters[Animals['Bee']]

                        # Print word and values of each animal
                        print(word + " - Spider = " + str(Animals['Spider']) + ", Green = " + str(
                            Animals['Green']) + ", Bee = " + str(Animals['Bee']) + ", Fly = " + str(
                            Animals['Fly']) + ", Ladybird = " + str(Animals['Ladybird']) + ", Butterfly = " + str(
                            Animals['Butterfly']) + ", Hopper = " + str(Animals['Hopper']))

print("The end...")
print("Took " + str(iterations) + " iterations")

# Process
# 1. Eliminate a loop completely by calculating Ladybird outside the loop
# 2. Eliminate more loops by skipping on first wrong value
# 3. Eliminate another loop by calculating the last two values with just a loop
