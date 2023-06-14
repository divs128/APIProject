// src/app/chat-assistant.ts
import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { OpenAIAPI } from 'openai';

@Injectable({
  providedIn: 'root'
})
export class ChatAssistant {
  private openai: OpenAIAPI;

  constructor() {
    this.openai = new OpenAIAPI(environment.openaiApiKey);
  }

  async sendMessage(message: string): Promise<string> {
    const response = await this.openai.complete({
      engine: 'davinci',
      prompt: `You: ${message}\nAssistant:`,
      maxTokens: 50,
      temperature: 0.6,
      n: 1,
      stop: '\n'
    });

    const reply = response.choices[0].text.trim();
    return reply;
  }
}
