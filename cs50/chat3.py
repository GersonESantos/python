from openai import OpenAI

# Substitua pela sua chave real entre aspas
client = OpenAI(api_key="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")

prompt = input('Prompt: ')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)