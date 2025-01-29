def encontrar_brinquedo(brinquedos, brinquedo): # Criando a função
    for item in brinquedos: # Percorrendo a lista
        if item == brinquedo: # Se achar o brinquedo carrinho
            return f"Achei o {brinquedo} " # Retorna o brinquedo
    return f"não achei" 

brinquedos = ["ursinho", "boneca", "carrinho", "bola", "lapis", "massinha", "caderno", "aquarela", "dino"] # Lista de brinquedos
print(encontrar_brinquedo(brinquedos, "carrinho"))
# Quanto maior a lista, mais tempo pode levar.
