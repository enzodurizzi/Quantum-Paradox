import random

def inicializar_jogo():
    cientistas = ["Ana", "Bruno", "Carlos"]
    elementos = ["Plutônio", "Urânio", "Tório"]
    setores = ["Laboratório", "Reator", "Oficina"]
    anos = [2042, 2088, 2150]

    # Embaralha para gerar uma solução única a cada partida
    random.shuffle(cientistas)
    random.shuffle(elementos)
    random.shuffle(setores)
    random.shuffle(anos)

    solucao = {}
    for i in range(3):
        solucao[cientistas[i]] = {
            "elemento": elementos[i],
            "setor": setores[i],
            "ano": anos[i]
        }
    return cientistas, elementos, setores, anos, solucao

def gerar_pistas(solucao):
    pistas = []
    cientistas = list(solucao.keys())
    
    # Pista 1: Lógica direta
    c1 = cientistas[0]
    pistas.append(f"O cientista {c1} estava trabalhando no setor {solucao[c1]['setor']}.")
    
    # Pista 2: Exclusão
    c2 = cientistas[1]
    el_errado = solucao[cientistas[2]]['elemento']
    pistas.append(f"O pesquisador que usou {solucao[c2]['elemento']} NÃO é quem estava estudando o {el_errado}.")
    
    # Pista 3: Relação temporal
    c3 = cientistas[2]
    ano_c3 = solucao[c3]['ano']
    pistas.append(f"A fenda temporal aberta na {solucao[c3]['setor']} ocorreu no ano de {ano_c3}.")
    
    return pistas

def jogar():
    print("=" * 60)
    print("      QUANTUM PARADOX: O ENIGMA DA SINGULARIDADE")
    print("=" * 60)
    print("Um paradoxo temporal misturou cientistas, elementos e setores!")
    print("Sua missão como agente temporal é reorganizar a linha do tempo.\n")

    cientistas, elementos, setores, anos, solucao = inicializar_jogo()
    pistas = gerar_pistas(solucao)

    print("📋 SUAS PISTAS ENCONTRADAS:")
    for pista in pistas:
        print(f" - {pista}")
    print("\n" + "-" * 60)

    opcoes_cientistas = sorted(cientistas)
    opcoes_elementos = sorted(elementos)
    opcoes_setores = sorted(setores)
    opcoes_anos = sorted(anos)

    print("\n🔍 ELEMENTOS PARA DEDUÇÃO:")
    print(f"Cientistas: {', '.join(opcoes_cientistas)}")
    print(f"Elementos: {', '.join(opcoes_elementos)}")
    print(f"Setores: {', '.join(opcoes_setores)}")
    print(f"Anos: {', '.join(map(str, opcoes_anos))}\n")

    print("Falta pouco! Para testar sua hipótese, onde estava um dos cientistas?")
    alvo = input(f"Escolha um cientista ({', '.join(opcoes_cientistas)}): ").strip()
    
    if alvo not in solucao:
        print("Cientista inválido!")
        return

    chute_setor = input(f"Em qual setor {alvo} estava? ({', '.join(opcoes_setores)}): ").strip()

    if solucao[alvo]['setor'].lower() == chute_setor.lower():
        print(f"\n✨ CORRETO! Você decifrou essa conexão cósmica. O setor de {alvo} era realmente o {solucao[alvo]['setor']}.")
    else:
        print(f"\n❌ INCORRETO. A flutuação temporal colapsou. O setor correto era {solucao[alvo]['setor']}.")
        
    print("\n📜 SOLUÇÃO COMPLETA DO PARADOXO:")
    for c, dados in solucao.items():
        print(f"• {c} -> Elemento: {dados['elemento']} | Setor: {dados['setor']} | Ano: {dados['ano']}")

if __name__ == "__main__":
    jogar()
