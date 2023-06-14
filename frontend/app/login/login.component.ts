import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';

  constructor(private authService: AuthService) { }

  submitLogin() {
    // Validate email and password
    if (!this.validateEmail(this.email)) {
      alert('Invalid email');
      return;
    }
    if (this.password.length < 6) {
      alert('Password must be at least 6 characters long');
      return;
    }

    // Call the login function from the auth service
    this.authService.login(this.email, this.password)
      .subscribe(
        (response) => {
          // Login successful, navigate to the Home screen
          // e.g., this.router.navigate(['/home']);
          console.log('Login successful');
        },
        (error) => {
          // Login failed, show error message
          alert('Invalid email or password');
        }
      );
  }

  validateEmail(email: string): boolean {
    // Validate email format using a regular expression
    // You can customize the regex pattern to fit your requirements
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
