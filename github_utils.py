import shutil
import os
from git import Repo # type: ignore
from github import Github # type: ignore
import stat

def remover_arquivo(func, path, excinfo):
    # Remove arquivo somente se for readonly
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clonar_repo(repo_url, pasta_destino="repo"):
    if os.path.exists(pasta_destino):
        shutil.rmtree(pasta_destino, onerror=remover_arquivo)  # força remoção mesmo no Windows
    return Repo.clone_from(repo_url, pasta_destino)

def configurar_github_pages(repo_name, usuario, token):
    g = Github(token)
    repo = g.get_repo(f"{usuario}/{repo_name}")

    branch = "gh-pages"
    branch_names = [b.name for b in repo.get_branches()]
    if branch not in branch_names:
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=repo.get_branch("main").commit.sha)

    repo.edit(name=repo_name, homepage=f"https://{usuario}.github.io/{repo_name}/")
    return f"https://{usuario}.github.io/{repo_name}/"

def commit_push(repo, msg="Atualização automática"):
    repo.git.add(all=True)
    repo.index.commit(msg)
    origin = repo.remote(name="origin")
    origin.push()
