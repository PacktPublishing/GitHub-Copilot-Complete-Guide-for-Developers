import express from 'express';
import bodyParser from 'body-parser';
import { ChatController } from './controllers/chatController';

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

const chatController = new ChatController();

app.post('/chat', (req, res) => chatController.handleChatRequest(req, res));

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});