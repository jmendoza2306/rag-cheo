from notion_client import Client

from core.config import settings

def get_notion_client():
    notion_client = Client(auth=settings.NOTION_TOKEN)
    if not notion_client:
        raise ValueError("Notion client not found")
    return notion_client