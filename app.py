from flask import Flask, render_template
import json

app = Flask(__my)

def get_top_three_batters():
        # Load the JSON data from the file
    with open('1373570.json', 'r') as file:
        match_data = json.load(file)

    # Extract innings data
    innings = match_data.get('innings', [])

    # Create a dictionary to store total runs for each batter
    batter_runs = {}

    # Iterate through innings
    for inning in innings:
        for over in inning['overs']:
            for delivery in over['deliveries']:
                batter = delivery['batter']
                runs = delivery['runs']['batter']

                # Update the runs for the batter
                batter_runs[batter] = batter_runs.get(batter, 0) + runs

    # Sort the batters by runs in descending order
    sorted_batters = sorted(batter_runs.items(), key=lambda x: x[1], reverse=True)

    # Get the top three batters
    top_three_batters = sorted_batters[:3]

    # Print the top three batters
    print("Top 3 Batters with Highest Scores:")
    for i, (batter, runs) in enumerate(top_three_batters):
        print(f"{i + 1}. {batter}: {runs} runs")

@app.route('/')
def display_stats():
    top_batters = get_top_three_batters()
    return render_template('my.html', top_batters=top_batters)

if __name__ == '__main__':
    app.run(debug=True)
