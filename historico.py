class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return self.insertPosition
        
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    
    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    def clear(self):
        self.elements = [None] * self.SIZE
        self.insertPosition = 0
    
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return ""
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:  
            self.elements[index] = self.elements[index+1]
            index += 1
        self.insertPosition -= 1
        return removedElement
        
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:  
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1   
        
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]

class PilhaHistorico:
    def __init__(self):
        self.historico = PersonalArray()
    
    def navegar_para(self, pagina):
        """Adiciona uma nova página ao topo do histórico"""
        self.historico.insertAt(0, pagina)
        print(f"\nNavegou para: {pagina}")
    
    def voltar(self):
        """Remove a página atual (topo) e retorna para a anterior"""
        if self.historico.isEmpty():
            print("\nHistórico vazio - não é possível voltar")
            return None
        
        pagina_atual = self.historico.removePosition(0)
        
        if not self.historico.isEmpty():
            print(f"\nVoltou para: {self.historico.elementAt(0)}")
        else:
            print("\nVoltou para a página inicial")
        
        return pagina_atual
    
    def pagina_atual(self):
        """Retorna a página atual (topo da pilha)"""
        if self.historico.isEmpty():
            return "Nenhuma página no histórico"
        return self.historico.elementAt(0)
    
    def mostrar_historico(self):
        """Exibe todo o histórico de navegação"""
        if self.historico.isEmpty():
            print("\nHistórico vazio")
            return
        
        print("\nHistórico de Navegação (do mais recente para o mais antigo):")
        for i in range(self.historico.size()):
            print(f"{i+1}º: {self.historico.elementAt(i)}")

# Simulação do Histórico de Navegação
print("=== SIMULAÇÃO DE HISTÓRICO DE NAVEGAÇÃO ===")

navegador = PilhaHistorico()

# Usuário começa a navegar
navegador.navegar_para("Página Inicial")
navegador.navegar_para("Produtos")
navegador.navegar_para("Smartphones")
navegador.navegar_para("iPhone 15")
navegador.navegar_para("Carrinho de Compras")

navegador.mostrar_historico()

# Usuário clica em voltar
navegador.voltar()
navegador.mostrar_historico()

# Usuário navega para nova página
navegador.navegar_para("Meu Perfil")
navegador.mostrar_historico()

# Usuário clica em voltar várias vezes
navegador.voltar()
navegador.voltar()
navegador.voltar()
navegador.mostrar_historico()

# Tentando voltar além do histórico
navegador.voltar()
navegador.voltar()
navegador.mostrar_historico()