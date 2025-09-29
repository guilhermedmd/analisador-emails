# Analisador de Emails✉🔍
Projeto consiste em uma aplicação que recebe o conteúdo de um email, por .txt ou .pdf, faz a análise do conteúdo com auxílio de uma API do Google Gemini e retorna 
a classificação do e-mail com base nos critérios:
  <br>
- Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema)

- Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).
<br>
Além disso, para que você saiba sobre o que se trata o e-mail a IA entrega um pequeno resumo e em caso da necessidade de uma resposta ela a gera de forma automática.  

## Como executar
Para utilizar a aplicação de forma local é necessário possuir uma IDE instalada na sua máquina, além de possuir todas as dependências do Python também instaladas
- Primeiro dê o comando git clone para clonar esse repositório dentro de um diretório de sua preferência:
  ```bash
  git clone https://github.com/guilhermedmd/analisador-emails.git
  ```
- Após isso dentro do mesmo diretório utilize o comando abaixo para criar um ambiente virtual, isso serve para que as dependências não sejam instaladas diretamente na sua máquina, mas somente no ambiente do projeto:
- ```bash
  python -m venv venv
  ```
- Depois ainda dentro desse mesmo diretório utilize o comando abaixo para instalar todas as dependências do projeto:
  ```bash
  pip install -r requirements.txt
  ```
- Nesse momento o projeto já está pronto para rodar, porém falta um detalhe para que ele funcione 100% que é a chave de API do gemini. Para isso você pode acessar o link para pegar a sua chave de API: https://aistudio.google.com/

- Agora substitua a API_KEY presente na linha 8 do arquivo gemini_api.py pela sua chave de API.
  
- Depois disso tudo o projeto está pronto para ser executado através do comando:
```bash
python main.py
```

### Caso você não queira executar todos esses comandos basta apenas acessar o projeto pelo link: https://analisadoremails.onrender.com/
Divirta-se

## Tecnologias utilizadas no desenvolvimento
<div align=center>
<img height="90" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
<img height="90" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original-wordmark.svg" />
<img height="90" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" />
<img height="90" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" />
<img height="75" width="75" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
</div>
          
          
          
                  

## Tela
