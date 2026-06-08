# LLM Homework - LangChain + LlamaCpp + FastAPI

## Tổng quan

Dự án chatbot AI sử dụng:
- LangChain
- LlamaCpp
- TinyLlama GGUF
- FastAPI
- HTML/CSS/JavaScript Client

Kiến trúc:

Web Client (localhost:3000)
↓
FastAPI (localhost:8000)
↓
LangChain
↓
LlamaCpp
↓
TinyLlama GGUF

---

## Build Docker

```bash
docker compose build
```

Chạy hệ thống:

```bash
docker compose up
```

---

## API

Trang chủ:

http://localhost:8000

Swagger:

http://localhost:8000/docs

Endpoint:

POST /chat

---

## Frontend

Mở:

http://localhost:3000

Chức năng:
- Nhập câu hỏi
- Gọi API FastAPI
- Hiển thị câu trả lời
- Lưu lịch sử chat phía client

---

## Bài 1 - LLM Hello World

```bash
docker compose run --rm llm python hello_world.py
```

Nội dung:
- Input
- Output
- Parameters
- Inference

---

## Bài 2 - Application Context

File:

app/context.py

Mục tiêu:
- Ghi nhớ lịch sử chat
- Prompt Builder
- Stateless Design

---

## Bài 3 - FastAPI

File:

app/main.py

Chức năng:
- POST /chat
- Nhận lịch sử chat
- Gọi LLM
- Trả kết quả

---

## Bài 4 - Client

Client được xây dựng bằng:
- HTML
- CSS
- JavaScript
- Fetch API

Flow:

User
↓
Web Client
↓
POST /chat
↓
FastAPI
↓
LangChain
↓
LlamaCpp
↓
TinyLlama
↓
Response

---

## Demo

1. Mở http://localhost:3000
2. Nhập câu hỏi
3. Mở DevTools → Network
4. Kiểm tra request POST tới http://localhost:8000/chat
5. Mở http://localhost:8000/docs để test API

---

## Kết quả

✅ Bài 1 - LLM Hello World

✅ Bài 2 - Application Context

✅ Bài 3 - FastAPI Chat API

✅ Bài 4 - Client Chatbot
