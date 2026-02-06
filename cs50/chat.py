import google.generativeai as genai

# COLOQUE SUA CHAVE AQUI ENTRE AS ASPAS
minha_chave = "SUA_CHAVE_AQUI_DO_AI_STUDIO"

# Configuração da API
genai.configure(api_key=minha_chave)

# Inicializa o modelo (o 1.5-flash é ótimo para quem estuda CS50)
model = genai.GenerativeModel('gemini-1.5-flash')

print("--- Chat Gemini Iniciado ---")
prompt = input('Prompt: ')

try:
    # Gera a resposta
    response = model.generate_content(prompt)
    
    print("\nResposta do Gemini:")
    print(response.text)

except Exception as e:
    print(f"\nOcorreu um erro: {e}")