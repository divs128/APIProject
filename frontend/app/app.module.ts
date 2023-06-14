// src/app/app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './Chat Assistant Chatbot.component';
import { ChatComponent } from './Chat Assistant Chatbot/chat-assistant.component';
import { ChatAssistant } from './chat-assistant';

@NgModule({
  declarations: [AppComponent, ChatComponent],
  imports: [BrowserModule, FormsModule],
  providers: [ChatAssistant],
  bootstrap: [AppComponent]
})
export class AppModule {}
