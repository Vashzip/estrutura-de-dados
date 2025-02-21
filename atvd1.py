class Musica:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.proxima = None


class Playlist:
    def __init__(self):
        self.atual = None

    def adicionar_musica(self, titulo, autor):
        nova_musica = Musica(titulo, autor)
        if self.atual is None:
            self.atual = nova_musica
            self.atual.proxima = self.atual
        else:
            temp = self.atual
            while temp.proxima != self.atual:
                temp = temp.proxima
            temp.proxima = nova_musica
            nova_musica.proxima = self.atual

    def tocar_playlist(self, repetir=False, limite=10):
        if self.atual is None:
            print("Playlist vazia!")
            return

        print("Tocando playlist:")
        temp = self.atual
        count = 0
        while count < limite:
            print(f"Título: {temp.titulo}, Autor: {temp.autor}")
            temp = temp.proxima
            count += 1
            if temp == self.atual and not repetir:
                break
        print("...")

    def display(self, limit=0):
        if self.atual is None:
            print("Lista vazia!")
            return
        current = self.atual
        count = 0
        while count < limit:
            print(f"{current.titulo}", end=" -> ")
            current = current.proxima
            count += 1
        print("...")


playlist = Playlist()
playlist.adicionar_musica("A Praia", "Mastruz Com Leite")
playlist.adicionar_musica("Anjo Querubim", "Limão com Mel")
playlist.adicionar_musica("Saga de um Vaqueiro", "Catuaba com Amendoim")
playlist.adicionar_musica("Minha herança", "Ana Castela")
playlist.adicionar_musica("Brigas", "Lagosta Bronzeada")
playlist.adicionar_musica("Dois Triste", "Simone Mendes")

playlist.display(limit=6)

playlist.tocar_playlist(repetir=True, limite=10)
