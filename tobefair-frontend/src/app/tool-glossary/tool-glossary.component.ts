// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';
import { ToolGlossaryComponent as LibToolGlossaryComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'aap-tool-glossary',
  standalone: true,
  imports: [LibToolGlossaryComponent],
  templateUrl: './tool-glossary.component.html',
  styleUrl: './tool-glossary.component.css',
})
export class ToolGlossaryComponent {}
