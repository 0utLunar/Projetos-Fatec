from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Programa Lava a Jato")
root.geometry("1024x768")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Lista para armazenar os labels dos resultados
resultado_labels = []

def limpar_resultados():
    """Remove os resultados antigos da tela."""
    for label in resultado_labels:
        label.destroy()
    resultado_labels.clear()

def calcular():
    limpar_resultados()  # Remove os resultados antigos antes de exibir os novos
    
    preco = precoValue.get()
    salario = salarioValue.get()
    custoFixo = custoFixoValue.get()
    comissao = comissaoValue.get()
    produtosLimpeza = produtosLimpezaValue.get()
    funcionarios = funcionariosValue.get()
    imposto = impostoValue.get()
    carros = carrosValue.get()

    receitaTotal = preco * carros
    salarioTotal = (salario * funcionarios) + (comissao * carros)
    impostoSalario = salarioTotal * (imposto / 100)
    custoVariavel = produtosLimpeza * carros
    custoTotal = custoFixo + salarioTotal + impostoSalario + custoVariavel
    lucroFinal = receitaTotal - custoTotal

    corText = "red" if lucroFinal < 0 else "blue" if lucroFinal == 0 else "green"
    
    labels_info = [
        ("Receita Total:", receitaTotal, "green", 700, 150),
        ("Custo Total:", custoTotal, "red", 700, 300),
        ("Lucro:", lucroFinal, corText, 700, 450)
    ]
    
    for texto, valor, cor, x, y in labels_info:
        label_texto = Label(root, text=texto, fg=cor, font=("Arial", 20, "bold"), bg="#f0f0f0")
        label_texto.place(x=x, y=y)
        resultado_labels.append(label_texto)
        
        label_valor = Label(root, text=f"R$ {valor:.2f}", fg=cor, font=("Arial", 20, "bold"), bg="#f0f0f0")
        label_valor.place(x=x+50, y=y+50)
        resultado_labels.append(label_valor)

# Adicionando um logo menor ao lado do título
titulo_frame = Frame(root, bg="#f0f0f0")
titulo_frame.place(relx=0.5, anchor="center", y=40)  # Centraliza o frame no topo

logo_original = PhotoImage(file="logo.png")  # Carrega a logo original
logo = logo_original.subsample(5, 5)  # Reduz o tamanho da imagem (ajuste conforme necessário)

Label(titulo_frame, image=logo, bg="#f0f0f0").pack(side=LEFT, padx=5)
Label(titulo_frame, text="Lava a Jato: Lava que Passa", font=("Arial", 25, "bold"), bg="#f0f0f0", fg="#333").pack(side=LEFT)

campos = [
    ("Preço por Lavagem (R$)", 150, DoubleVar()),
    ("Custo dos Produtos de Limpeza (R$)", 200, DoubleVar()),
    ("Comissão por Carro (R$)", 250, DoubleVar()),
    ("Salário dos Funcionários (R$)", 300, DoubleVar()),
    ("Porcentagem de Impostos (%)", 350, DoubleVar()),
    ("Custos Fixos da Empresa (R$)", 400, DoubleVar()),
    ("Quantidade de Funcionários", 450, IntVar()),
    ("Quantidade de Carros Lavados", 500, IntVar()),
]

variaveis = []
for texto, y, var in campos:
    Label(root, text=texto, font=("Arial", 14), bg="#f0f0f0").place(x=50, y=y)
    entry = ttk.Entry(root, textvariable=var, width=15, font=("Arial", 14))
    entry.place(x=400, y=y)
    variaveis.append(var)

(precoValue, produtosLimpezaValue, comissaoValue, salarioValue, 
impostoValue, custoFixoValue, funcionariosValue, carrosValue) = variaveis

Button(text="Calcular", font=("Arial", 16, "bold"), width=15, height=2, bg="#4CAF50", fg="white", command=calcular).place(x=400, y=600)

root.mainloop()
