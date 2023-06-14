import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Doctor } from '../../models/doctor.model';

@Component({
  selector: 'app-available-physician',
  templateUrl: './available-physician.component.html',
  styleUrls: ['./available-physician.component.css']
})
export class AvailablePhysicianComponent implements OnInit {
  loading: boolean = true;
  doctors: Doctor[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit() {
    // Make API call to fetch the list of doctors
    const token = localStorage.getItem('token');
    if (token) {
      const headers = new HttpHeaders({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
      });

      this.http.get<any>('https://2378-49-36-137-22.ngrok-free.app/doctors', { headers })
        .subscribe(
          (response) => {
            this.doctors = response.data;
            this.loading = false;
          },
          (error) => {
            alert('Failed to fetch doctors');
            this.loading = false;
          }
        );
    } else {
      alert('Invalid token');
      this.loading = false;
    }
  }

  requestConsultation(doctor: Doctor) {
    // Handle request consultation logic and navigation
    console.log('Requesting consultation for doctor:', doctor);
  }
}
