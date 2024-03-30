import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay about penguins "}])
print(completion.choices[0].message.content)