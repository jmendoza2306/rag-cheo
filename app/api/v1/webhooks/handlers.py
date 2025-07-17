from app.core.logging_config import logger

async def process_notion_event(page_id: str, event_type: str, event_data: dict):
    logger.info(f"🎯 Processing event: {event_type} for page: {page_id}")

    if event_type == "page.content_updated":
        logger.info(f"📝 Page content updated: {page_id}")
    elif event_type == "comment.created":
        logger.info(f"💬 Comment created on page: {page_id}")
    elif event_type == "database.schema_updated":
        logger.info(f"🗃️ Database schema updated: {page_id}")
    else:
        logger.info(f"❓ Unknown event type: {event_type}")
