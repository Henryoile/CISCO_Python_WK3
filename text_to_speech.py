from gtts import gTTS

text = (
    "Ready to transform your body and elevate your mind? "
    "At Delight Hot Yoga, we bring you the energy, passion, and power of original hot yoga. "
    "Build strength, boost your confidence, and feel amazing from the inside out. "
    "Step into a healthier, happier lifestyle and unleash your full potential today."
)

tts = gTTS(text=text, lang='en', slow=False, tld='com')

tts.save("delight_hot_yoga.mp3")

print("Audio saved successfully")



