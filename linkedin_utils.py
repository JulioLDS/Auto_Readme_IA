import requests # pyright: ignore[reportMissingModuleSource]
from config import LINKEDIN_TOKEN

def postar_linkedin(texto, url=None, imagem_path=None):
    headers = {
        "Authorization": f"Bearer {LINKEDIN_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "author": "urn:li:person:SEU_ID_LINKEDIN",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": texto},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=data)
    return response.status_code, response.text
