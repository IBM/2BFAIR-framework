import { Component, inject } from '@angular/core';
import {
  Router,
  RouterOutlet,
  RouterLink,
  RouterLinkActive,
} from '@angular/router';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { EvaluationService } from '@dwb/to-be-fair';

import { ButtonModule } from 'carbon-components-angular';

@Component({
  selector: 'app-evaluate',
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    ReactiveFormsModule,
    ButtonModule,
  ],
  templateUrl: './evaluate.component.html',
  styleUrl: './evaluate.component.css',
})
export class EvaluateComponent {
  public evaluationRequestForm = new FormGroup({
    digitalObjectURI: new FormControl(''),
    community: new FormControl(''),
    task: new FormControl(''),
  });

  evaluationService: EvaluationService = inject(EvaluationService);
  error: string | null | undefined;

  constructor(private router: Router) {}

  submitEvaluationRequest() {
    const { digitalObjectURI, community, task } =
      this.evaluationRequestForm.value;
    this.evaluationService.requestStandalone(
      digitalObjectURI ?? '',
      community ?? '',
      task ?? '',
    );
    this.evaluationService.error$.subscribe((error) => {
      this.error = error;
    });
    this.router.navigate(['/result']);
  }
}
