import os
import shutil

def adicionar_imagens(repo_path, imagens):
    repo_images_path = os.path.join(repo_path, "images")
    os.makedirs(repo_images_path, exist_ok=True)
    caminhos_para_readme = []
    for img in imagens:
        nome = os.path.basename(img)
        destino = os.path.join(repo_images_path, nome)
        shutil.copy(img, destino)
        caminhos_para_readme.append(f"images/{nome}")
    return caminhos_para_readme

def criar_readme(repo_path, conteudo, url_pages=None):
    readme_path = os.path.join(repo_path, "README.md")
    with open("repo/README.md", "w", encoding="utf-8") as f:
        f.write(conteudo)

        if url_pages:
            #link github Pages
            f.write(f"\n\n🌐 **Veja a página online:** [{url_pages}]({url_pages})\n") 
            #Link rodando na Web
            #f.write(f"\n\n🌐 **Veja a página online:** [{url_pages}]({url_pages})\n") 