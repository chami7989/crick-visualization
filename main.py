import json

# Load the JSON data from the file
with open('sample-data.json', 'r') as file:
    match_data = json.load(file)

# Extract innings data
innings = match_data.get('innings', [])

# Create dictionaries to store total runs and balls faced for each batter
batter_runs = {}
batter_balls_faced = {}

# Iterate through innings
for inning in innings:
    for over in inning['overs']:
        for delivery in over['deliveries']:
            batter = delivery['batter']
            runs = delivery['runs']['batter']

            # Update the runs and balls faced for the batter
            batter_runs[batter] = batter_runs.get(batter, 0) + runs
            batter_balls_faced[batter] = batter_balls_faced.get(batter, 0) + 1

# Sort the batters by runs in descending order
sorted_batters = sorted(batter_runs.items(), key=lambda x: x[1], reverse=True)

# Display the top batters with runs and balls faced
print("Top Batters with Highest Scores and Balls Faced:")
for i, (batter, runs) in enumerate(sorted_batters):
    balls_faced = batter_balls_faced.get(batter, 0)
    print(f"{i + 1}. {batter} - {runs} runs ({balls_faced} balls)")
