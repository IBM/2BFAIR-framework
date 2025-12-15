// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

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
import { LinkButtonComponent } from "../link-button/link-button.component";

const badgeSources: string[] = [
  "../assets/badge3.png",
  "../assets/badge2.png",
  "../assets/badge1.png"
];

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    ReactiveFormsModule,
    ButtonModule,
    LinkButtonComponent
],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
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

  submitTestEvaluationRequest() {
    this.evaluationService.requestStandalone(
      '10.5281/zenodo.8255910', '', '',
    );
    this.evaluationService.error$.subscribe((error) => {
      this.error = error;
    });
    this.router.navigate(['/result']);
  }
}
