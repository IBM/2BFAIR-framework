// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';

import { DetailsComponent as LibDetailsComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [LibDetailsComponent],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css',
})
export class DetailsComponent {}
