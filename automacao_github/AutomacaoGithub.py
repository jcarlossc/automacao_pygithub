from github import Github

class AutomacaoGithub:
    
    def __init__(self, TOKEN):
        self.token = TOKEN
        self.github_objeto = Github(TOKEN)

    def listar_repositorio(self):    
        lista = self.github_objeto.get_user()
        for i, repositorio in enumerate(lista.get_repos(), start = 1):
            print(f"{i}. {repositorio.name} | {'Privado' if repositorio.private else 'Público'} | {repositorio.html_url}")



