import os
import requests
from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Client initiated")

# Read environment variables
token = os.getenv("GITHUB_TOKEN")
repo = os.getenv("GITHUB_REPOSITORY")
pr_number = os.getenv("PR_NUMBER")

# Prepare headers for GitHub API
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# GitHub API URL for listing PR files
api_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"

# Make the request
response = requests.get(api_url, headers=headers)

if response.status_code != 200:
    print(f"Error fetching PR files: {response.status_code}")
    print(response.text)
    exit(1)

# Process file list
files = response.json()
for file in files:
    filename = file["filename"]
    status = file["status"]  # 'added', 'modified', or 'removed'
    print(f"{status.upper()}: {filename}")

