 🛠 Ferramenta de Diagnóstico de Rede

Script em Python para diagnóstico de rede, permitindo testar ping, resolver DNS, verificar status de portas e exibir IP local e público. Ideal para analistas de suporte e iniciantes em redes que desejam automatizar verificações básicas.

 🚀 Funcionalidades

- Teste de ping
- Resolução de DNS
- Verificação de portas TCP
- Exibição de IP local
- Consulta de IP público

 📦 Requisitos

- Python 3.x
- Biblioteca `requests`

Instale com:

```bash
pip install requests
🖥️ Como usar
Execute o script com os argumentos desejados:

bash
Copiar
Editar
python Main.py --ping 8.8.8.8
python Main.py --dns google.com
python Main.py --portas 80,443,22
Se nenhum argumento for passado, ele exibe IP local e público por padrão.

💡 Exemplos
bash
Copiar
Editar
python Main.py --ping 8.8.8.8
python Main.py --dns google.com
python Main.py --portas 80,443 --dns google.com
python Main.py
