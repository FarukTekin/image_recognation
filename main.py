import ollama

res = ollama.chat(
    model = "llava:13b",
    messages=[
        {
            "role": "user",
            "content": "Describe this image",
            "images": ["./fil.jpg"]
        }
    ]
)

print(res["message"]["content"])
