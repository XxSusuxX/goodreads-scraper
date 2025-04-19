# Goodreads Scraper

Este projeto é um scraper para extrair citações do site [Goodreads](https://www.goodreads.com/quotes). Ele utiliza o framework **Scrapy** para realizar a extração e possui uma interface gráfica desenvolvida em **Tkinter** para facilitar a configuração e execução.

---

## **Funcionalidades**
- Interface gráfica moderna e estilizada.
- Validação de entrada para o número de páginas (1 a 100).
- Campo para o nome do arquivo de saída.
- Menu suspenso para selecionar o formato do arquivo (JSON ou CSV).
- Mensagens de sucesso e erro claras para o usuário.
- Link para o portfólio do desenvolvedor.

---

## **Requisitos**
- **Python 3.10 ou superior**
- Bibliotecas necessárias:
  - `scrapy`
  - `tkinter` (nativo no Python)
  - `Pillow`

---

## **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/goodreads-scraper.git
   cd goodreads-scraper
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # No Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python ui/app.py
   ```

---

## **Como usar**
1. Insira o número de páginas a serem extraídas (entre 1 e 100).
2. Digite o nome do arquivo de saída (sem extensão).
3. Escolha o formato do arquivo (JSON ou CSV).
4. Clique no botão **Iniciar** para executar o Scrapy.
5. Após a conclusão, uma mensagem será exibida com o caminho do arquivo gerado.

---

## **Estrutura do Projeto**
```plaintext
goodreads-scraper/
├── assets/
│   └── icon.ico          # Ícone da aplicação
├── spiders/
│   └── goodreads.py      # Spider do Scrapy para extrair citações
├── ui/
│   └── app.py            # Interface gráfica (Tkinter)
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

---

## **Exemplo de Uso**
### **Entrada**
- Número de páginas: `5`
- Nome do arquivo: `citacoes`
- Formato: `json`

### **Saída**
- Arquivo gerado: `citacoes.json`
- Local: Diretório atual do projeto.

---

## **Próximos passos**
- Teste o script `app.py` para garantir que ele está capturando o número de páginas corretamente.
- Certifique-se de que o pipeline do Scrapy está configurado para salvar os dados no formato desejado (JSON, CSV, etc.).
- Adicione suporte a internacionalização (i18n) para tornar o programa acessível a usuários de diferentes idiomas.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.