import ollama

res = ollama.chat(
    model = "llava:13b",
    messages=[
        {
            "role": "user",
            "content": "How many elephants are in this image?",
            "images": ["./fil.jpg"]
        }
    ]
)

print(res["message"]["content"])
