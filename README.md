# OrangeWoodTest

An image analysis tool that detects whether a robotic gripper is holding an object using Google's Gemini AI API.

## Overview

This project uses Google's Gemini multimodal AI to:
1. Describe objects in images
2. Determine whether a green robotic suction gripper is holding an object

## Setup

### Prerequisites

- Python 3.11+
- Poetry package manager

### Installation

1. Clone the repository
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
3. Copy the template environment file and add your API key:
   ```bash
   cp template.env .env
   ```
4. Edit the `.env` file and replace `'your_api_key'` with your actual Gemini API key

## Usage

Run the main script:

```bash
poetry run python main.py
```

The script will:
- Load an object image from `images/objectimage.jpg` and generate a description
- Load a gripper image from `images/gripper_image.jpg` and determine if it's holding an object

## Project Structure

- `main.py` - Core program logic
- `.env` - Configuration variables (API key and prompts)
- `images/` - Directory containing test images
  - `objectimage.jpg` - Generic object image
  - `gripper_image.jpg` - Robotic gripper image 

## Environment Variables

- `geminiApiKey` - Your Google Gemini API key
- `MainPrompt` - Prompt for gripper detection
- `DescriptionPrompt` - Prompt for object description