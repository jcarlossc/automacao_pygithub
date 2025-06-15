from github import Github

class AutomacaoGithub:
    
    def __init__(self, TOKEN) -> None:
        self.token = TOKEN
        self.github_objeto = Github(TOKEN)

    def listar_repositorios(self) -> None:    
        usuario = self.github_objeto.get_user()
        for i, repositorio in enumerate(usuario.get_repos(), start = 1):
            print(f"{i}. {repositorio.name} | {'Privado' if repositorio.private else 'Público'} | {repositorio.html_url}")

    def criar_repositorio(self, nome: str, descricao: str) -> None:
        usuario = self.github_objeto.get_user()
        novo_repositorio = usuario.create_repo(
            name = nome,
            description = descricao,
            private = False
        )
        print(f"Repositório criado: {novo_repositorio.html_url}")
