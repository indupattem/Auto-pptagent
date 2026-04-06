import asyncio
import os
import time
from dotenv import load_dotenv
from google import genai
import requests

from mcp_servers.ppt_mcp_server import (
    create_presentation,
    add_slide,
    write_content,
    save_presentation
)

# -------------------- CONFIG --------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# -------------------- AI CONTENT (NO HARDCODING) --------------------

def get_slide_content(topic, title):
    try:
        # 🔥 Try Gemini first
        prompt = f"""
        Generate 6 accurate bullet points for a PowerPoint slide.

        Topic: {topic}
        Slide Title: {title}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text

        points = [
            line.strip("-• ").strip()
            for line in text.split("\n")
            if line.strip()
        ]

        if len(points) >= 5:
            return points[:6]

    except Exception as e:
        print("❌ Gemini failed:", e)

    # 🔥 FALLBACK = REAL DATA (NOT STATIC)
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + topic.replace(" ", "_")
        res = requests.get(url).json()

        text = res.get("extract", "")

        sentences = text.split(". ")

        points = [s.strip() for s in sentences if len(s) > 20][:6]

        if points:
            return points

    except:
        pass

    # 🔥 LAST fallback (dynamic, not fixed)
    words = topic.split()

    return [
        f"{topic} involves concepts related to {words[0] if words else 'technology'}",
        f"{title} explains important aspects of the topic",
        f"{topic} is widely used in different domains",
        f"It helps improve efficiency and decision making",
        f"{topic} is evolving with new advancements",
        f"It has significant real-world applications"
    ]
# -------------------- PLAN --------------------
def plan_slides(topic):
    return [
        f"Introduction to {topic}",
        f"Key Concepts of {topic}",
        f"Applications of {topic}",
        f"Advantages of {topic}",
        f"Future of {topic}"
    ]


# -------------------- MAIN AGENT --------------------
async def run_ppt_agent(user_request: str):

    print("🧠 Planning slides...")

    slides = plan_slides(user_request)

    filename = f"output_{int(time.time())}.pptx"

    create_presentation(filename)

    # 🎯 Title slide
    add_slide(filename, user_request)
    write_content(filename, 0, [
        "Auto-generated Presentation",
        "AI-powered Content Generation",
        "MCP Architecture",
        "Dynamic Slide Creation"
    ])

    # 🚀 Generate slides dynamically
    for i, title in enumerate(slides):
        print(f"➡ Adding slide: {title}")

        add_slide(filename, title)

        points = get_slide_content(user_request, title)

        # safety check
        if not points or len(points) < 3:
            points = [
                f"{title} overview",
                "Core ideas explained",
                "Applications and use cases",
                "Benefits",
                "Future scope",
                "Conclusion"
            ]

        write_content(filename, i + 1, points)

    save_presentation(filename)

    print(f"✅ PPT Generated Successfully: {filename}")