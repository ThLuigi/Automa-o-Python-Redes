import socket
import os
import platform
import requests
import argparse

# Configuração baseada no sistema operacional
so = platform.system()
comando_ping = "ping -n 4" if so == "Windows" else "ping -c 4"

def testar_ping(host):
    """
    Testa a conectividade com um host via ping.
    """
    try:
        print(f"\n🔍 Testando ping em {host}...")
        resposta = os.system(f"{comando_ping} {host}")
        if resposta == 0:
            print("✅ Ping bem-sucedido!")
        else:
            print("❌ Falha no ping.")
    except Exception as e:
        print(f"⚠️ Erro ao testar ping: {e}")

def resolver_dns(dominio):
    """
    Resolve o endereço IP de um domínio.
    """
    try:
        print(f"\n🔍 Resolvendo DNS de {dominio}...")
        ip = socket.gethostbyname(dominio)
        print(f"🌐 IP de {dominio}: {ip}")
    except socket.gaierror:
        print("❌ Domínio não encontrado ou sem conexão com a internet.")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

def ip_local():
    """
    Exibe o IP local da máquina.
    """
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"\n🏠 IP local: {ip}")
    except Exception as e:
        print(f"⚠️ Erro ao obter IP local: {e}")

def ip_publico():
    """
    Obtém o IP público da conexão.
    """
    try:
        print("\n🔍 Buscando IP público...")
        ip = requests.get("https://api.ipify.org", timeout=5).text
        print(f"🌍 IP público: {ip}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Falha ao acessar api.ipify.org: {e}")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")

def testar_portas(host, portas):
    """
    Verifica o status de portas específicas em um host.
    """
    try:
        print(f"\n🔍 Testando portas em {host}...")
        for porta in portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, porta))
            status = "🟢 Aberta" if resultado == 0 else "🔴 Fechada"
            print(f"Porta {porta}: {status}")
            sock.close()
    except socket.gaierror:
        print("❌ Host inválido ou sem conexão.")
    except Exception as e:
        print(f"⚠️ Erro ao testar portas: {e}")

def main():
    """
    Função principal que processa os argumentos da linha de comando.
    """
    parser = argparse.ArgumentParser(
        description="🚀 Ferramenta de Diagnóstico de Rede - Teste ping, DNS, portas e IPs",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--ping",
        help="Testa a conectividade com um host (ex: --ping 8.8.8.8)"
    )
    parser.add_argument(
        "--dns",
        help="Resolve o DNS de um domínio (ex: --dns google.com)"
    )
    parser.add_argument(
        "--portas",
        help="Testa portas específicas (ex: --portas 80,443,22)"
    )
    
    args = parser.parse_args()

    # Executa as funções baseadas nos argumentos
    if args.ping:
        testar_ping(args.ping)
    if args.dns:
        resolver_dns(args.dns)
    if args.portas:
        portas = [int(p) for p in args.portas.split(",")]
        host = args.dns if args.dns else "localhost"
        testar_portas(host, portas)

    # Executa funções padrão se nenhum argumento for fornecido
    if not any(vars(args).values()):
        print("\nℹ️  Nenhum argumento fornecido. Executando diagnósticos básicos...")
        ip_local()
        ip_publico()

if __name__ == "__main__":
    main()
