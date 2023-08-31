class Produto:
   def __init__(self,nome, preco, estoque):
      self.nome = nome
      self.estoque = estoque
      self.valor_estoque = estoque * preco
   def exibirinfo(self):
      print(f"{self.nome} tem {self.estoque} no estoque e o estoque está avaliado em {self.valor_estoque:.2f}")
   def descontoporc(self, pct_desconto):
      self.valor_estoque = self.valor_estoque * (1 -pct_desconto/100)    
produto1 = Produto("Abobora", 5, 10)
produto2 = Produto("Livro", 30 , 5 )
produto2.descontoporc(10)
produto1.descontoporc(50)
produto1.exibirinfo()
produto2.exibirinfo()
