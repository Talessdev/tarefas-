import json
from pathlib import Path

ARQ = Path("tarefas.json")

def carregar():
    if ARQ.exists():
        return json.loads(ARQ.read_text(encoding="utf-8"))
    return []

def salvar(tarefas):
    ARQ.write_text(json.dumps(tarefas, ensure_ascii=False, indent=2), encoding="utf-8")

def listar(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return
    print("\nSuas tarefas:")
    for i, t in enumerate(tarefas, start=1):
        status = "[OK]" if t["done"] else "[..]"
        print(f"{i}. {status} {t['titulo']}")
    print()

def adicionar(tarefas):
    titulo = input("Digite a tarefa: ").strip()
    if not titulo:
        print("Tarefa vazia.\n")
        return
    tarefas.append({"titulo": titulo, "done": False})
    salvar(tarefas)
    print("Tarefa adicionada!\n")

def concluir(tarefas):
    listar(tarefas)
    if not tarefas:
        return
    try:
        n = int(input("Numero da tarefa para concluir: "))
        if 1 <= n <= len(tarefas):
            tarefas[n-1]["done"] = True
            salvar(tarefas)
            print("Concluida!\n")
        else:
            print("Numero invalido.\n")
    except ValueError:
        print("Digite um numero.\n")

def remover(tarefas):
    listar(tarefas)
    if not tarefas:
        return
    try:
        n = int(input("Numero da tarefa para remover: "))
        if 1 <= n <= len(tarefas):
            apagada = tarefas.pop(n-1)
            salvar(tarefas)
            print(f"Removida: {apagada['titulo']}\n")
        else:
            print("Numero invalido.\n")
    except ValueError:
        print("Digite um numero.\n")

def menu():
    tarefas = carregar()
    while True:
        print("=== Tarefas (CLI) ===")
        print("1) Listar tarefas")
        print("2) Adicionar tarefa")
        print("3) Concluir tarefa")
        print("4) Remover tarefa")
        print("0) Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            listar(tarefas)
        elif op == "2":
            adicionar(tarefas)
            tarefas = carregar()
        elif op == "3":
            concluir(tarefas)
            tarefas = carregar()
        elif op == "4":
            remover(tarefas)
            tarefas = carregar()
        elif op == "0":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida.\n")

if __name__ == "__main__":
    menu()
