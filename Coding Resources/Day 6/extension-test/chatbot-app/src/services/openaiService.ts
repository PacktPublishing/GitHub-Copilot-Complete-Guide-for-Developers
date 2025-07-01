import axios from 'axios';

class OpenAIService {
    private apiKey: string;
    private apiUrl: string;

    constructor(apiKey: string) {
        this.apiKey = apiKey;
        this.apiUrl = 'https://api.openai.com/v1/responses';
    }

    public async sendMessage(message: string): Promise<string> {
        try {
            const response = await axios.post(this.apiUrl, {
                model: 'gpt-3.5-turbo',
                messages: [{ role: 'user', content: message }],
            }, {
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json',
                },
            });

            return response.data.choices[0].message.content;
        } catch (error) {
            throw new Error('Error communicating with OpenAI API: ' + error.message);
        }
    }
}

export default OpenAIService;