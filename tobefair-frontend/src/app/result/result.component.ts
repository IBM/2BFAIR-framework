// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';
import { ResultComponent as LibResultComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-result',
  standalone: true,
  imports: [LibResultComponent],
  templateUrl: './result.component.html',
  styleUrl: './result.component.css',
})
export class ResultComponent {}
