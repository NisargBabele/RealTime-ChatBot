import os
from openai import OpenAI

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("User: ")
        if not user_input.strip():
            print("Exiting chat.")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            reply = response.choices[0].message.content
            print("ChatGPT:", reply)
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("API Error:", e)

if __name__ == "__main__":
    main()
