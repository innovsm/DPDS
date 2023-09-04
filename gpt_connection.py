import openai

# main function from here
openai.api_key = "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"

def chat_with_chatgpt(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message