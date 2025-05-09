from lida import Manager, TextGenerationConfig, llm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set your Generative Language API Key as an environment variable
os.environ["PALM_API_KEY"] = "PALM_API_KEY"

# Initialize LIDA with PaLM (Gemini via the Generative Language API)
lida = Manager(text_gen=llm(provider="palm", api_key=os.environ["PALM_API_KEY"]))

# Define text generation configuration
textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="models/gemini-1.5-flash")

# Load a sample dataset
data_url = "https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv"
try:
    df = pd.read_csv(data_url)
    print("Data loaded successfully:")
    print(df.head())
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Summarize the data
summary = lida.summarize(df, summary_method="default", textgen_config=textgen_config)
print("\nData Summary:")
print(summary)

# Generate a visualization goal
goals = lida.goals(summary, n=1, textgen_config=textgen_config)
print("\nGenerated Goal:")
print(goals[0])

# Generate a visualization
charts = lida.visualize(summary=summary, goal=goals[0], textgen_config=textgen_config, library="seaborn")

if charts:
    chart_code = charts[0].code
    print("\nGenerated Visualization Code:")
    print(chart_code)

    # Try to execute and display the visualization
    try:
        exec(chart_code)
        plt.show()
    except Exception as e:
        print(f"\nError executing visualization code: {e}")
        print("You might need a more interactive environment (like Jupyter Notebook) for complex visualizations.")
else:
    print("\nNo visualization generated.")