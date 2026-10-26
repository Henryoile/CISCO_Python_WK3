import asyncio
import edge_tts

text = (
    "With an introductory beginners offer of 8000 Kenyan shillings for 30 days unlimited sessions, "
    "invest in your health, beauty, wellness, and overall fitness by practicing Original Hot Yoga at Delight Hot Yoga, "
    "located inside Lavington Mall, 4th Floor, Art Cafe Restaurant, Lavington Wing, "
    "along James Gichuru Road. Namaste!"
)

async def main():
    tts = edge_tts.Communicate(text, voice="en-US-AndrewNeural", rate="+8%", pitch="-3Hz")
    await tts.save("delight_hot_yoga.mp3")
    print("Audio saved successfully")

asyncio.run(main())