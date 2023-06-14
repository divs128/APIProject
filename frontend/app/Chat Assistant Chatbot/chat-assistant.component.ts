// src/app/chat/chat.component.ts
import { Component } from '@angular/core';
import { ChatAssistant } from '../chat-assistant';

@Component({
  selector: 'app-chat',
  templateUrl: './chat-assistant.component.html',
  styleUrls: ['./chat-assistant.component.css']
})
export class ChatComponent {
  messages: string[] = [];
  userInput: string = '';

  constructor(private chatAssistant: ChatAssistant) {}

  async sendMessage(): Promise<void> {
    const userMessage = this.userInput.trim();
    if (userMessage) {
      this.messages.push(`You: ${userMessage}`);
      this.userInput = '';

      const reply = await this.chatAssistant.sendMessage(userMessage);
      this.messages.push(`Assistant: ${reply}`);
    }
  }
}
