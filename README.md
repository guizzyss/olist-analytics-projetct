## 🚀 Como Executar

**1. Clone o repositório:**

```bash
git clone [url-do-seu-repositorio]
cd Olist_ECommerce_ETL

**2. Crie e ative um Ambiente Virtual:**

```python -m venv .venv
source .venv/bin/activate   #Linux/MacOS
.\.venv\Scripts\activate    #Windows

**3. Instale as dependências:**

pip install -r requirements.txt

**4. Configure as Variáveis de Ambiente:**

cp .env.example .env

**5. Executando a Pipeline:**

python src/main.py