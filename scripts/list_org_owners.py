import csv
import requests
import os

def get_org_admins(org_name, token, role=None):
    url = f"https://api.github.com/orgs/{org_name}/members?role={role}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    admins = []

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        members = response.json()
        admins.extend([{'login': member['login'], 'role': role} for member in members])

        # Check for pagination
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    return admins

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['login', 'role'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    org_name = os.getenv('GITHUB_ORG_NAME')
    token = os.getenv('GITHUB_TOKEN')
    role = os.getenv('ROLE')
    if not org_name:
        raise ValueError("GITHUB_ORG_NAME environment variable is not set")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")
    admins = get_org_admins(org_name, token, role)
    save_to_csv(admins, 'org_members.csv')