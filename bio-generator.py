import os
import requests
from dotenv import load_dotenv
from github import Github
from linkedin_api import Linkedin

# Import your local LLM library here
# from your_local_llm_library import LocalLLM

def load_env_variables():
    load_dotenv()
    github_url = os.getenv('GITHUB_PROFILE_URL')
    linkedin_url = os.getenv('LINKEDIN_PROFILE_URL')
    return github_url, linkedin_url

def get_github_info(github_url):
    # Extract username from URL
    username = github_url.split('/')[-1]
    
    # Initialize Github API client
    g = Github()
    user = g.get_user(username)
    
    # Fetch relevant information
    github_info = {
        'name': user.name,
        'bio': user.bio,
        'public_repos': user.public_repos,
        'followers': user.followers,
        'languages': get_top_languages(user),
    }
    return github_info

def get_top_languages(user):
    languages = {}
    for repo in user.get_repos():
        lang = repo.language
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]

def get_linkedin_info(linkedin_url):
    # Note: LinkedIn doesn't provide an official API for personal accounts.
    # You may need to use a third-party library or implement web scraping.
    # This is a placeholder function.
    
    # Extract profile ID from URL
    profile_id = linkedin_url.split('/in/')[-1]
    
    # Initialize Linkedin API client (you'll need to handle authentication)
    api = Linkedin()
    profile = api.get_profile(profile_id)
    
    linkedin_info = {
        'name': profile.get('firstName', '') + ' ' + profile.get('lastName', ''),
        'headline': profile.get('headline', ''),
        'current_position': profile.get('experience', [{}])[0].get('title', ''),
        'skills': profile.get('skills', [])[:5],
    }
    return linkedin_info

def generate_bio_markdown(github_info, linkedin_info):
    # Combine the information into a context for the LLM
    context = f"""
    GitHub Information:
    Name: {github_info['name']}
    Bio: {github_info['bio']}
    Public Repositories: {github_info['public_repos']}
    Followers: {github_info['followers']}
    Top Languages: {', '.join([lang for lang, _ in github_info['languages']])}

    LinkedIn Information:
    Name: {linkedin_info['name']}
    Headline: {linkedin_info['headline']}
    Current Position: {linkedin_info['current_position']}
    Top Skills: {', '.join(linkedin_info['skills'])}

    Create a professional bio in markdown format that combines the GitHub (developer) and LinkedIn (professional) aspects.
    """

    # Initialize your local LLM here
    # llm = LocalLLM()
    
    # Generate the bio using the local LLM
    # bio_markdown = llm.generate(context)
    
    # For now, we'll just return a placeholder
    bio_markdown = "# Generated Bio\n\nThis is where the generated bio would appear."
    
    return bio_markdown

def main():
    github_url, linkedin_url = load_env_variables()
    github_info = get_github_info(github_url)
    linkedin_info = get_linkedin_info(linkedin_url)
    bio_markdown = generate_bio_markdown(github_info, linkedin_info)
    
    # Save the generated bio to a file
    with open('generated_bio.md', 'w') as f:
        f.write(bio_markdown)
    
    print("Bio generated and saved to 'generated_bio.md'")

if __name__ == "__main__":
    main()
