from openai import OpenAI

# O client já vai buscar a chave automaticamente nas variáveis de ambiente
client = OpenAI()

prompt = input('Prompt: ')

try:
    # O método correto é chat.completions.create
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Este é o modelo mais rápido e barato disponível
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # A forma de acessar o texto da resposta mudou nas versões recentes
    print("\nResposta da IA:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\nOcorreu um erro: {e}")