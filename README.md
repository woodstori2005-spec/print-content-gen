# print-content-gen 🖨️✨

AI-powered caption and hashtag generator for 3D printing businesses.
Describe your print, get ready-to-post TikTok and Instagram content in seconds.

## What it generates

- **Short caption** — punchy 1-2 lines for TikTok
- **Long caption** — storytelling Instagram caption with a call to action
- **Hashtags** — 20 relevant tags (mix of big and niche)
- **Video hook** — the perfect opening line for your TikTok

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Anthropic API key:

```bash
cp .env.example .env
# edit .env and paste your key
```

## Usage

```bash
python generate.py
```

You'll be asked a few quick questions:

```
What did you make? Dragon figurine
Material & color? Black resin
Who's it for? Fantasy fans, gift
How long did it take? 14 hours
Anything special? Super detailed scales
```

Then your content is ready to copy and paste. Done. 🚀
