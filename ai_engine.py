import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_code(image_bytes, framework, project_structure):

    api_key = os.getenv("OPENAI_API_KEY")

    # If no API key → return mock demo code
    if not api_key:
        return f"""
// MOCK MODE (No API Key Provided)

// Framework: {framework}

export default function NewScreen() {{
  return (
    <div style={{padding: "20px"}}>
      <h1>Generated Screen (Mock Mode)</h1>
      <p>This is a demo output without OpenAI API.</p>
    </div>
  );
}}
"""

    client = OpenAI(api_key=api_key)

    base64_image = base64.b64encode(image_bytes).decode("utf-8")
    project_context = "\n".join(project_structure) if project_structure else "No existing project."

    prompt = f"""
You are a senior frontend architect.

Framework: {framework}

Existing project structure:
{project_context}

Instructions:
- Analyze the uploaded UI image.
- Generate a new screen component.
- Follow same naming conventions.
- Match project folder style.
- Keep consistent coding style.
- Make responsive.
- Return only code.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ],
            }
        ],
    )

    return response.choices[0].message.content
