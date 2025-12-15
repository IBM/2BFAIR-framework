// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';
import { UserGuideComponent as LibUserGuideComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-user-guide',
  standalone: true,
  imports: [LibUserGuideComponent],
  templateUrl: './user-guide.component.html',
  styleUrl: './user-guide.component.css',
})
export class UserGuideComponent {}
