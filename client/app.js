const history = [];

async function sendMessage() {

    const input =
        document.getElementById("message");

    const message =
        input.value.trim();

    if (!message) {
        return;
    }

    const chatBox =
        document.getElementById("chat-box");

    chatBox.innerHTML +=
        `<div class="user">
            <b>Bạn:</b> ${message}
        </div>`;

    history.push({
        role: "user",
        content: message
    });

    input.value = "";

    try {

        const response =
            await fetch(
                "http://localhost:8000/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        session_id: "user1",
                        messages: history
                    })
                }
            );

        const data =
            await response.json();

        history.push({
            role: "assistant",
            content: data.answer
        });

        chatBox.innerHTML +=
            `<div class="bot">
                <b>Bot:</b>
                ${data.answer}
            </div>`;

        chatBox.scrollTop =
            chatBox.scrollHeight;

    } catch (error) {

        chatBox.innerHTML +=
            `<div class="bot">
                Lỗi kết nối API
            </div>`;
    }
}