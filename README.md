# URL Shortener CLI (Python)

This is a simple Python command-line tool to shorten URLs using multiple providers, including Bit.ly, TinyURL, and Da.gd. The tool supports saving Bit.ly API keys securely in a local file for future use.

## Features

- 🔗 Shorten URLs using:
  - Bit.ly (requires API key)
  - TinyURL
  - Da.gd
- 🗝️ Automatically prompt for Bit.ly API key and save it for reuse
- 📁 Stores credential in a local file (`cred.txt`)
- ✅ Basic URL validation (adds `https://` if missing)

## Requirements

- Python 3.x
- [pyshorteners](https://pypi.org/project/pyshorteners/)

Install the required package:

```bash
pip install pyshorteners
```

## Usage

Run the script:

```bash
python main.py
```

Then follow the CLI prompts:

1. Choose your URL shortening provider.
2. Enter the URL you want to shorten.

If Bit.ly is selected, you will be asked to input your API key (only once, saved locally).

## Bit.ly API Key

You can get your Bit.ly API key here: [https://bitly.com/a/oauth_apps](https://bitly.com/a/oauth_apps)

Once you enter the key during the first run, it will be saved in `cred.txt` and reused in future runs.

## File Structure

- `main.py` - The main Python script
- `cred.txt` - Stores the Bit.ly API key securely in JSON format

## Example Output

```
=== URL Shortener ===
Select URL shortening provider:
1. Bit.ly (requires API key)
2. TinyURL
3. Da.gd
Enter your choice (1-3): 2
Enter the URL to shorten: https://dacent.vercel.app/

Result:
Original URL: https://dacent.vercel.app/
Shortened URL: https://tinyurl.com/2xk536xt
```

## License

This project is licensed under the MIT License.
