import openai

# main function from here
openai.api_key = "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"

def chat_with_chatgpt(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens = 250,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message