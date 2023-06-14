import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { AvailablePhysicianComponent } from './components/available-physician/available-physician.component';
import { RequestConsultationComponent } from './components/request-consultation/request-consultation.component';
import { ChatAssistantComponent } from './components/chat-assistant/chat-assistant.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AvailablePhysicianComponent,
    RequestConsultationComponent,
    ChatAssistantComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
