import os
import random
from datetime import datetime

import pandas as pd

from groq import Groq

from dotenv import load_dotenv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load environment variables
load_dotenv()


# Create solutions folder
os.makedirs("solutions", exist_ok=True)


# Load dataset
df = pd.read_csv("tasks.csv")


# Create ML features
df["features"] = (
    df["category"] + " " + df["difficulty"]
)


# Convert text to vectors
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(
    df["features"]
)


# User preference
user_interest = "String Easy"


# Convert user interest into vector
user_vector = vectorizer.transform(
    [user_interest]
)


# Find similarity
similarity = cosine_similarity(
    user_vector,
    feature_vectors
)


# Add scores
df["score"] = similarity[0]


# Sort tasks
recommended = df.sort_values(
    by="score",
    ascending=False
)


# Select top tasks
selected_tasks = recommended.head(5)


# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# Generate README
today = datetime.now().strftime("%Y-%m-%d")

readme_content = (
    f"# Daily AI Python Tasks ({today})\n\n"
)


# Generate solutions
for index, row in selected_tasks.iterrows():

    task = row["task"]

    category = row["category"]

    difficulty = row["difficulty"]


    print(f"Generating solution for: {task}")


    # Prompt Engineering
    prompt = f"""
Generate ONLY executable Python code.

Do NOT use markdown.
Do NOT include ```python.
Do NOT include explanations.
Add comments.

Problem:
{task}
"""


    # Call LLM
    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1024
    )


    generated_code = (
        response.choices[0]
        .message.content
    )

    
    
    # Clean filename
    filename = (
        task.lower()
        .replace(" ", "_")
        .replace("-", "_")
        + ".py"
    )


    filepath = os.path.join(
        "solutions",
        filename
    )


    # Save Python solution
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(generated_code)


    # Update README
    readme_content += (
        f"## {task}\n"
        f"- Category: {category}\n"
        f"- Difficulty: {difficulty}\n"
        f"- Solution: solutions/{filename}\n\n"
    )


# Save README
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)


print("Daily tasks generated successfully")