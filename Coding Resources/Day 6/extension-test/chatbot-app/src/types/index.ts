export interface ChatRequest {
    message: string;
    userId: string;
}

export interface ChatResponse {
    response: string;
    timestamp: Date;
}