import secrets
import string

def gerando_senha(tamnho):

    if tamnho < 4:
        return ValueError("Tamanho insuficiente para gerar uma senha segura. Tamanho minimo é de 4 caracteres.")
    
    senha = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha += [secrets.choice(caracteres) for _ in range(tamnho - 4)]

    secrets.SystemRandom().shuffle(senha)
    return ''.join(senha)

print("<---------- Bem vindo ao gerador de senhas! ---------->")
print("Aqui você pode gerar senhas segurar e aleatorias.")
tamanho = input("Digite o tamanho da senha desejada (minimo 4 caracteres):")
print(gerando_senha(int(tamanho)))
