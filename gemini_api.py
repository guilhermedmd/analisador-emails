import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

def avaliar_email(conteudo_email):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(f"Abaixo há um texto que pertence a um email. Preciso que avalie ele com base nos critérios:" \
    "Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema)." \
    "Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos). É importante também elaborar uma resposta, mas apenas caso seja necessário." \
    "É importante dizer, em que caso do arquivo recebido não ser um email, que ele não é uma email."\
    "Se o arquivo for um email, durante a resposta é necessário informar a categoria em que se enquadra esse email, um breveresumo em pouquissímas linhas e, somente se for necessário, a resposta que deve ser enviada. "\
    "Segue abaixo o email:\n"+conteudo_email)
    return response.text

