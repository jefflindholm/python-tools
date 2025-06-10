# import git
# import openai

# # Initialize OpenAI API (set your API key as an environment variable or paste directly—caution!)
# openai.api_key = "366f9134136b4d6fbbdb0ed4a38e56eb"

# # Path to your local Git repo
# repo_path = "/path/to/your/repo"
# repo = git.Repo(repo_path)

# # Get the diff of staged changes
# diff_text = repo.git.diff('--cached')

# # Submit the diff to OpenAI's API for commit message generation
# def generate_commit_message(diff):
#     prompt = f"Generate a concise, clear commit message for the following Git diff:\n\n{diff}"
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=60,
#         temperature=0.7
#     )
#     return response['choices'][0]['message']['content'].strip()

# # Generate commit message
# commit_message = generate_commit_message(diff_text)
# print("Suggested commit message:", commit_message)

# # Commit with the generated message
# repo.git.commit('-m', commit_message)
# print("Committed changes to repo.")

import os
import sys
import git
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = os.environ["MISTRAL_MODEL"]

client = Mistral(api_key=api_key)

# Path to your local Git repo
repo_path = sys.argv[1]
repo = git.Repo(repo_path)

# Get the diff of staged changes
diff_text = repo.git.diff("HEAD")
print(diff_text)

# Submit the diff to OpenAI's API for commit message generation
def generate_commit_message(diff):
    prompt = f"Generate a concise, clear commit message for the following Git diff:\n\n{diff}"

    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    return chat_response.choices[0].message.content


# Generate commit message
commit_message = generate_commit_message(diff_text)
print("-------------------------------")
print("Suggested commit message:", commit_message)

# Commit with the generated message
repo.git.commit('-m', commit_message)
print("Committed changes to repo.")
