def enviar_cartas(amigos):
    for remetente in amigos:
        for destinatario in amigos:
            print(f"{remetente} enviou uma carta para {destinatario}")

amigos = ["Ana", "Beto", "Carlos"]
enviar_cartas(amigos)
# Quanto maior a lista, mais tempo pode levar.
