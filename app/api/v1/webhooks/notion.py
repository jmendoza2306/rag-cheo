from fastapi import APIRouter, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from typing import Optional
import json

from app.core.logging_config import logger

from app.api.v1.webhooks.signature_notion import verify_signature
from app.api.v1.webhooks.handlers import process_notion_event

router = APIRouter()
VERIFICATION_TOKEN = None

BUTTONS_TO_PROCESS = ["tz%5EW"]

@router.post("/webhook")
async def handle_notion_webhook(
    request: Request,
    x_notion_signature: Optional[str] = Header(None, alias="X-Notion-Signature")
):
    global VERIFICATION_TOKEN

    try:
        payload_body = await request.body()
        try:
            payload_data = json.loads(payload_body.decode('utf-8'))
        except json.JSONDecodeError:
            logger.error("Invalid JSON payload")
            raise HTTPException(status_code=400, detail="Invalid JSON payload")

        if "verification_token" in payload_data:
            verification_token = payload_data["verification_token"]
            VERIFICATION_TOKEN = verification_token
            logger.info(f"🔥 COPY THIS TOKEN INTO NOTION: {verification_token}")
            return JSONResponse(status_code=200, content={"message": "Verification token received", "verification_token": verification_token})

        if VERIFICATION_TOKEN and x_notion_signature:
            if not verify_signature(payload_body, x_notion_signature, VERIFICATION_TOKEN):
                logger.warning("Invalid signature for webhook event")
                raise HTTPException(status_code=401, detail="Invalid signature")

        event_type = payload_data.get("type", "unknown")
        button_clicked = payload_data.get("data", {}).get("updated_properties", None)

        logger.info(f"🔄 Payload data: {payload_data}")
        if button_clicked:
            if button_clicked[0] in BUTTONS_TO_PROCESS:
                logger.info(f"🔘 Button clicked: {button_clicked}")
                
            else:
                logger.info(f"We are not pulling the from this event: {button_clicked}")

        logger.info(f"📥 Received webhook: {event_type}")
        return JSONResponse(status_code=200, content={"message": "Webhook processed successfully"})

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "verification_token_received": VERIFICATION_TOKEN is not None
    }

@router.get("/verification-token")
async def get_verification_token():
    if VERIFICATION_TOKEN:
        return {"verification_token": VERIFICATION_TOKEN}
    else:
        return {"message": "No verification token received yet"}
