from google import genai

# COLOQUE SUA CHAVE AQUI
minha_chave = ""

# Inicializa o cliente novo
client = genai.Client(api_key=minha_chave)

print("--- Chat Gemini Iniciado (Versão Atualizada) ---")
prompt = input('Prompt: ')

try:
    # No modelo novo, usamos apenas 'gemini-1.5-flash' ou 'gemini-2.0-flash'
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    
    print("\nResposta do Gemini:")
    print(response.text)

except Exception as e:
    print(f"\nOcorreu um erro: {e}")