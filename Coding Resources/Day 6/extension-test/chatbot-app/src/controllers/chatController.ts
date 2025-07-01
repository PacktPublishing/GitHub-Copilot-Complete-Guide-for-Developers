import { Request, Response } from 'express';
import OpenAIService from '../services/openaiService';

class ChatController {
    private openAIService: OpenAIService;

    constructor() {
        this.openAIService = new OpenAIService();
    }

    public async handleChatRequest(req: Request, res: Response): Promise<void> {
        const { message } = req.body;

        try {
            const responseMessage = await this.openAIService.sendMessage(message);
            res.json({ response: responseMessage });
        } catch (error) {
            res.status(500).json({ error: 'An error occurred while processing your request.' });
        }
    }
}

export default ChatController;