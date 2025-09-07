from config import GITHUB_TOKEN, GITHUB_USER, IMAGES_FOLDER
from github_utils import clonar_repo, configurar_github_pages, commit_push
from screenshot import tirar_screenshot
from readme_utils import adicionar_imagens, criar_readme
from ia_utils import gerar_readme
import time

# Inputs do usuário
repo_url = "https://github.com/JulioLDS/Calculadora-JS"
tipo = "frontend"  # ou "backend"
imagens_backend = ["images/img1.png"]  # se for backend

repo = clonar_repo(repo_url)
repo_name = repo_url.rstrip("/").split("/")[-1]

if tipo.lower() == "frontend":
    main_html = input("Digite o nome do arquivo HTML inicial (ex: index.html, login.html): ").strip()
    url_pages = f"https://{GITHUB_USER.lower()}.github.io/{repo_name}/{main_html}"
    configurar_github_pages(repo_name, GITHUB_USER, GITHUB_TOKEN)
    # Aguarda o GitHub Pages atualizar
    time.sleep(15)
    tirar_screenshot(url_pages, f"{IMAGES_FOLDER}/screenshot.png")
    imagens_para_readme = adicionar_imagens(
        repo.working_tree_dir,
        [
            f"{IMAGES_FOLDER}/screenshot.png",
        ]
    )
else:
    imagens_para_readme = adicionar_imagens(repo.working_tree_dir, imagens_backend)

# Gerar README com IA
conteudo_readme = gerar_readme(imagens_para_readme)
criar_readme(repo.working_tree_dir, conteudo_readme, url_pages if tipo=="frontend" else None)

# Commit + push
commit_push(repo)
print("Agente finalizou!")
print(f"Link da página (se FrontEnd): {url_pages if tipo=='frontend' else repo_url}")