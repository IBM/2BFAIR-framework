// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';
import { GlossaryComponent as LibGlossaryComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-glossary',
  standalone: true,
  imports: [LibGlossaryComponent],
  templateUrl: './glossary.component.html',
  styleUrl: './glossary.component.css',
})
export class GlossaryComponent {}
