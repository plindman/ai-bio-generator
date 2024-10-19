# AI GitHub Bio Generator

This Python project automatically generates a professional bio by combining information from your GitHub and LinkedIn profiles. It uses a local Language Model (LLM) to create a markdown-formatted bio that showcases both your developer and professional sides.

## Features

- Fetches profile information from GitHub using the GitHub API
- Retrieves data from LinkedIn (placeholder implementation)
- Combines information from both profiles
- Uses a local LLM to generate a personalized bio
- Outputs the bio in markdown format

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- Access to your GitHub and LinkedIn profiles
- A local LLM set up on your machine (implementation not included)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/github-bio-generator.git
   cd github-bio-generator
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

   Note: You'll need to create a `requirements.txt` file with the following content:
   ```
   python-dotenv
   PyGithub
   # Add any other required libraries here
   ```

3. Create a `.env` file in the project root directory with your profile URLs:
   ```
   GITHUB_PROFILE_URL=https://github.com/yourusername
   LINKEDIN_PROFILE_URL=https://www.linkedin.com/in/yourprofile
   ```

## Usage

1. Ensure your local LLM is set up and running.

2. Implement the LinkedIn data retrieval function in the script. You may need to use a third-party library or implement web scraping, as LinkedIn doesn't provide an official API for personal accounts.

3. Integrate your local LLM in the `generate_bio_markdown` function.

4. Run the script:
   ```
   python github_bio_generator.py
   ```

5. The generated bio will be saved as `generated_bio.md` in the project directory.

## Customization

- Modify the `get_github_info` function to fetch additional information from your GitHub profile.
- Adjust the `get_linkedin_info` function to retrieve the LinkedIn data you're interested in.
- Update the `generate_bio_markdown` function to change the prompt sent to your local LLM.

## Contributing

Contributions to the GitHub Bio Generator are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyGithub](https://github.com/PyGithub/PyGithub) for GitHub API interactions
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management

## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.
