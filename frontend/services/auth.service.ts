import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }

  login(email: string, password: string) {
    // Make API call to authenticate the user
    // Replace the API endpoint and payload with your authentication logic
    const body = { email, password };
    return this.http.post<any>('https://api.example.com/login', body);
  }
}
