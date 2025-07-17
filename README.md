# Cheo's RAG Service

A production-ready Retrieval-Augmented Generation (RAG) service that maintains real-time synchronization with Notion knowledge bases through intelligent webhook processing and vector storage.

## Architecture Overview

This service implements a complete RAG pipeline:

1. **Webhook Listener**: FastAPI service receives real-time updates from Notion
2. **Content Processing**: Smart chunking and preprocessing of updated documents
3. **Vector Storage**: Embedding generation and storage in Pinecone with rich metadata
4. **Retrieval Interface**: Query endpoint to feed the Cheo AI system

## Features

- **Real-time Sync**: Automatic updates when content team modifies Notion documents
- **Smart Chunking**: Intelligent text segmentation preserving semantic meaning
- **Vector Storage**: Optimized embedding storage with metadata in Pinecone
- **Scalable Architecture**: FastAPI-based service ready for production deployment

## Development Roadmap

### ✅ Completed
- [x] FastAPI webhook service implementation
- [x] Basic Notion webhook integration

### 🚧 In Progress
- [ ] Smart event filtering and page extraction
- [ ] Advanced chunking and vector storage pipeline
- [ ] Retrieval API for Cheo integration

### 🔮 Planned
- [ ] Semantic search optimization
- [ ] Multi-workspace support
- [ ] Performance monitoring and analytics

## Quick Start

### Prerequisites
- Python 3.8+
- Notion workspace with API access
- Pinecone account and API key
- ngrok (for local development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cheo-rag-service
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

### Development Setup

1. **Start the FastAPI service**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. **Expose local service with ngrok**
   ```bash
   ngrok http 8000
   ```

3. **Configure Notion webhook**
   - Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)
   - Follow the [Notion webhook setup guide](https://developers.notion.com/reference/webhooks)
   - Set webhook endpoint to: `https://your-ngrok-url.ngrok.io/api/v1/webhook/notion`

### Configuration

Create a `.env` file with the following variables:

```env
NOTION_TOKEN=your_notion_integration_token
NOTION_DATABASE_ID=your_knowledge_base_database_id
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX_NAME=cheo-knowledge-base
WEBHOOK_SECRET=your_webhook_secret
```

## API Endpoints

### Webhook Endpoints
- `POST /webhook/notion` - Receives Notion page updates
- `GET /health` - Service health check

### Retrieval Endpoints
- `POST /search` - Semantic search in knowledge base
- `GET /stats` - Vector database statistics


## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

## Monitoring and Logging

The service includes structured logging and metrics collection:
- Request/response logging
- Vector storage performance metrics
- Webhook processing statistics
- Error tracking and alerting


