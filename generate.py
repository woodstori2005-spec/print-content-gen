#!/usr/bin/env python3
"""
generate.py - AI content generator for 3D printing businesses

Generates TikTok/Instagram captions and hashtags from a quick description
of your print.

Usage:
    python generate.py
"""

import os
import sys
from dotenv import load_dotenv
import anthropic

# Ensure Unicode output works on Windows terminals
sys.stdout.reconfigure(encoding="utf-8")

_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path=_env_path, override=True)

_api_key = os.environ.get("ANTHROPIC_API_KEY") or __import__("dotenv").dotenv_values(_env_path).get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=_api_key)

DIVIDER = "─" * 50


def ask(prompt, required=True):
    """Prompt the user for input."""
    while True:
        value = input(f"  {prompt}: ").strip()
        if value or not required:
            return value
        print("  (this one is required, give it a go!)")


def build_prompt(details):
    return f"""You are a social media expert for a 3D printing small business that sells on TikTok and Instagram.

A customer just finished a print with these details:
- What they made: {details['item']}
- Material & color: {details['material']}
- Who it's for / use case: {details['audience']}
- Print time: {details['time']}
- Anything special or unique: {details['special']}

Generate the following — be engaging, authentic, and fun. Match the vibe of successful 3D printing creators:

1. SHORT CAPTION (1-2 punchy lines, great for TikTok, under 150 chars)
2. LONG CAPTION (3-5 lines for Instagram, tells a story, ends with a call to action)
3. HASHTAGS (20 relevant hashtags, mix of big and niche ones)
4. VIDEO HOOK (one killer opening line to say in the first 2 seconds of a TikTok)

Format your response with clear headers like:
SHORT CAPTION:
LONG CAPTION:
HASHTAGS:
VIDEO HOOK:"""


def generate_content(details):
    """Call the Claude API and return the generated content."""
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": build_prompt(details)}
        ]
    )
    return message.content[0].text


def main():
    print(f"\n{DIVIDER}")
    print("  🖨️  3D Print Content Generator")
    print(f"{DIVIDER}\n")
    print("  Answer a few quick questions about your print:\n")

    details = {
        "item":     ask("What did you make? (e.g. dragon figurine, phone stand)"),
        "material": ask("Material & color? (e.g. black resin, rainbow PLA)"),
        "audience": ask("Who's it for / what's it used for? (e.g. gift, desk decor)"),
        "time":     ask("How long did it take to print? (e.g. 8 hours)", required=False) or "unknown",
        "special":  ask("Anything special about it? (e.g. super detailed, glows in dark)", required=False) or "nothing extra",
    }

    print(f"\n  ✨ Generating your content...\n")

    try:
        content = generate_content(details)
        print(f"{DIVIDER}")
        print(content)
        print(f"{DIVIDER}\n")
    except anthropic.AuthenticationError:
        print("  ❌ API key invalid. Check your .env file.")
    except Exception as e:
        print(f"  ❌ Something went wrong: {e}")


if __name__ == "__main__":
    main()
