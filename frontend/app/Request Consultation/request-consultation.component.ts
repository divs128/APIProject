import { Component } from '@angular/core';

@Component({
  selector: 'app-request-consultation',
  templateUrl: './request-consultation.component.html',
  styleUrls: ['./request-consultation.component.css']
})
export class RequestConsultationComponent {
  name: string = '';
  insuranceId: string = '';

  submitRequest() {
    // Validate name and insurance ID
    if (this.name.trim() === '') {
      alert('Please enter your name');
      return;
    }
    if (this.insuranceId.trim() === '') {
      alert('Please enter your insurance ID');
      return;
    }

    // Handle request submission logic
    console.log('Submitting request for consultation');
  }
}
